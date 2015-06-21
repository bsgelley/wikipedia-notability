'''
Created on Jun 18, 2015

@author: blumag
'''
from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World!"
    return render_template('index.html')