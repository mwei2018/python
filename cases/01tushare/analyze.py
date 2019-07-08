# -*-coding:utf-8-*-

"""
    auth: mason
    desc: 2019趣味实战4-如何选股
    version：1.0
    create date：2019.7.1

 2 首先要用tushare获取股票的数据
        2-1.我们先拿到所有券商股的列表

        2-2.接着我们获取所有券商股的历史数据，比如我们可以拿到它近1年的200多个交易日的数据

3.进行简单的数据预处理
我们主要是保留成交量，涨幅


4.数据可视化
我们把所有的数据数据进行对比分析，用不同的可视化图像进行对比
比如可用用直方图，散点图，折线图和箱体图进行对比
"""

import tushare as ts
import mongodb
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Scatter

token = 'ae1bdf8e1a53c0b0be2983572d828be03a6ae034323a5d8751c2822c'


def get_all_securities(token):
    pro = ts.pro_api(token)
    mongo_trades = mongodb.MongoBase('trades')
    mongo = mongodb.MongoBase('securities')

    count = mongo.collection.count_documents({})
    print(count)
    if count == 0:
        print("查询当前所有正常上市交易的股票列表")
        df_all = pro.query(
            'stock_basic',
            exchange='',
            list_status='L',
            fields='ts_code,symbol,name,area,industry,list_date')

        print(df_all)
        # print(df_all.loc[:,['industry']])
        # print(df_all[df_all.industry=='环境保护'])
        part_securities = df_all[df_all['industry'].isin(
            ['环境保护', '医疗保健'])].head()  # top 5
        print(part_securities)
        mongo_trades.dataframe_to_mongo(part_securities)
        for index, row in part_securities.iterrows():
            df_row = pro.query(
                'daily',
                ts_code=row['ts_code'],
                start_date='20180701',
                end_date='20190701')
            print(df_row)
            res = mongo.dataframe_to_mongo(df_row)
            print(res)

    print("从db拿数据分析准备绘制图像")

    trades = list(mongo_trades.collection.find())
    results = list(mongo.collection.find())

    mongo.close_db()
    df_results = pd.DataFrame(results)
    df_trades = pd.DataFrame(trades)
    df = pd.merge(df_results, df_trades, on='ts_code', how='inner')

    #环境保护和医疗保健股票成交额和涨幅分析图表
    grid_vertical(df)

    #股票月涨幅对比图
    month_line(df)


def month_line(df):
    date = pd.date_range('20180701', periods=12, freq='BM').to_period('M')
    xis_label = [str(x) for x in date]
    line = Line()
    line.add_xaxis(xis_label)
    line.set_global_opts(title_opts=opts.TitleOpts(title="股票月涨幅对比图"))
    for name, group in df.groupby('name'):
        group_df = group.reset_index() # reset_index否则下句有时报错
        group_df['trade_date'] = pd.to_datetime(
            group_df['trade_date'])  # 将数据类型转换为日期类型
        group_df = group_df.set_index('trade_date')  # 将date设置为index

        month_date = group_df.resample('M', convention='end').sum().to_period('M') # 按月统计
        dt = [round(x, 2) for x in month_date['pct_chg']]
        line.add_yaxis(group_df.head(1)['name'][0], dt)

    line.render("month.html")


def grid_vertical(df):
    df_amount = df.groupby(by=['ts_code'])['amount'].sum()
    df_amount = df_amount.reset_index(name='amount')

    df_pct_chg = df.groupby(by=['ts_code'])['pct_chg'].sum()
    df_pct_chg = df_pct_chg.reset_index(name='Range')

    yaxis = [round(d / 100000, 2) for d in df_amount['amount'].tolist()]
    yaxis2 = [round(d, 2) for d in df_pct_chg['Range'].tolist()]

    bar = (
        Bar()
        .add_xaxis(set(df['name'].tolist()))
        .add_yaxis("成交金额(亿)", yaxis)
        .add_yaxis("涨幅", yaxis2)
        .set_global_opts(title_opts=opts.TitleOpts(title="环境保护和医疗保健股票成交额和涨幅分析图表"))
    )

    line = Line()
    line.add_xaxis(set(df['trade_date'].tolist()))
    # 分组显示线
    for name, group in df.groupby('name'):
        #print(name, group, "\n")
        line.add_yaxis(name, group['pct_chg'].tolist(), is_smooth=True)

    line.set_global_opts(
        title_opts=opts.TitleOpts(title="日涨幅", pos_top="48%"),
        legend_opts=opts.LegendOpts(pos_top="48%"),
    )
    grid = (
        Grid()
        .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
        .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    grid.render()


def main():
    get_all_securities(token)


if __name__ == '__main__':
    main()
