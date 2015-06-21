'''
Created on Jun 18, 2015

@author: blumag
'''

from flask import Flask
from flaskext.mysql import MySQL


def startdb(inapp):
    mysql = MySQL()
    inapp.config['MYSQL_DATABASE_USER'] = 'root'
    inapp.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    inapp.config['MYSQL_DATABASE_DB'] = 'EmpData'
    inapp.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(inapp)