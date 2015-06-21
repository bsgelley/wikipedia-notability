'''
Created on Jun 18, 2015

@author: blumag
'''

from flask import Flask
import dbconfig

app = Flask(__name__)

dbconfig.startdb(app)
from app import views