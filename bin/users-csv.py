#!/usr/bin/python

import argparse
import sys
import os
import csv

from ec3_cloud_users.log import Logger
from ec3_cloud_users.cache import load, update
from ec3_cloud_users.userutils import UserUtils
from ec3_cloud_users.config import parse_config
from ec3_cloud_users.userutils import gen_username

conf_opts = parse_config()


def main():
    parser = argparse.ArgumentParser(description="""Load users from csv""")
    parser.add_argument('-f', dest='csvfile', metavar='users.csv', help='path to csv file with users', type=str, required=False)
    args = parser.parse_args()
    logger = Logger(os.path.basename(sys.argv[0]))
    lobj = Logger(sys.argv[0])
    logger = lobj.get()

    usertool = UserUtils(logger)
    users, usernames = list(), set()
    cdb = conf_opts['settings']['cache']
    cache = load(cdb, logger)

    with open(args.csvfile) as fp:
        reader = csv.reader(fp.readlines(), delimiter=',')
        for row in reader:
            users.append(row)

    users = users[1:]
    allusernames_db = set([u['username'] for u in cache['users']])

    for user in users:
        usernames.update([gen_username(user[0], user[1], allusernames_db)])

    diff = usernames.difference(allusernames_db)

    for users in diff:
        print(users)


if __name__ == '__main__':
    main()