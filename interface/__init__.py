"""@__init__
This file allows the containing directory to be considered a python package,
consisting of python module(s). Also, this file initializes flask object, which
allows each module to import it.

Note: the last 'views' import is required to be after initializing flask.
"""

from flask import Flask

# initialize flask instance
 app = Flask(__name__)

# required circular import
import interface.views    # noqa
