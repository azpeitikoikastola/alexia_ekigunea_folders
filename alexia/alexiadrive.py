# -*- coding: utf-8 -*-
from gappsconnect.google_apps import AppsObject
import sys
import getopt

SERVICE_NAME = 'drive'
SERVICE_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.file']


class SystemObject(object):

    def __init__(self):
        config = {}
        execfile("config.conf", config)
        config['scopes'] = SCOPES
        config['service_name'] = SERVICE_NAME
        config['service_version'] = SERVICE_VERSION
        self.domain = config.get('domain')
        self.ao = AppsObject(api_key=config['service_key'], scopes=SCOPES,
                              delegation_email=config['delegation_email'],
                              service_name=SERVICE_NAME,
                              service_version=SERVICE_VERSION)
        self.grade = config.get('grade')


def main():
    sysconf = SystemObject()
    argv = sys.argv
    options, args = getopt.getopt(argv[1:], 'csg', [])
    created_users = []
    # if not options:
    #     created_users = create_apps_users_db_add_email(sysconf)
    #     sync_apps_users(sysconf, ignore=created_users)
    #     create_apps_group_add_members(sysconf)
    # else:
    #     for opt, value in options:
    #         if opt in ['-c']:
    #             created_users = create_apps_users_db_add_email(sysconf)
    #             break
    #     for opt, value in options:
    #         if opt in ['-s']:
    #             sync_apps_users(sysconf, ignore=created_users)
    #             break
    #     for opt, value in options:
    #         if opt in ['-g']:
    #             create_apps_group_add_members(sysconf)
    #             break

    #TODO clean groups and org units

if __name__ == "__main__":
    main()