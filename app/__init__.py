from flask import Flask
from Logger import log
import os

app = Flask(__name__)

"""     Import all view's    """
for f_name in os.listdir('.\\app\\view'):
    if "__" in f_name:
        continue

    log('app.__init__', f"Import package app.view.{f_name[:-3]}")
    __import__('app.view.' + f_name[:-3])
