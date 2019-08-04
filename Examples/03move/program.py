#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import gflags
import logging
import db_util

Flags = gflags.FLAGS

gflags.DEFINE_boolean("debug", True, "whether debug")


def main(argv):
    Flags(argv)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S",
        filename="logger.log",
        filemode="w",
    )

    logging.warning(Flags.debug)
    client = db_util.MongoDBManager(lazy_connection=True)
    #result = client.find_match("courses", "")

    # 按照类型查找
    category_key = "爱情"
    query = {"category": {"$regex": category_key, "$options": "i"}}
    result = client.find_match("SyncmovieItem", query)
    print(list(result))


if __name__ == "__main__":
    main(sys.argv)
