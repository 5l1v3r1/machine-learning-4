"""@views

This file contains the (view) route decorators, which execute a defined
function assigned to the URL within the route decorator.

"""

import json
from interface import app
from flask import render_template, request
from brain.load_data import Load_Data
from brain.converter.restructure_data import Restructure_Data
from brain.database.retrieve_session import Retrieve_Session
from brain.cache.cache_model import Cache_Model
from brain.cache.cache_hset import Cache_Hset

## index: render 'index.html'
@app.route('/')
def index():
    return render_template('index.html')

## load_data: return computed data
@app.route('/load-data/', methods=['POST', 'GET'])
def load_data():
    if request.method == 'POST':

        # load programmatic-interface
        if request.get_json():
            # get necessary components from the dataset
            if 'dataset' in request.get_json():
                dataset = request.get_json()['dataset']
            else:
                dataset = None
            settings = request.get_json()['properties']

            # restructure the dataset
            sender = Restructure_Data(settings, dataset)
            data_formatted = sender.restructure()

            # send reformatted data to brain
            loader = Load_Data(data_formatted)
            if loader.get_session_type()['session_type']:
                session_type = loader.get_session_type()['session_type']

                if session_type == 'data_new': response = loader.load_data_new()
                elif session_type == 'data_append': response = loader.load_data_append()
                elif session_type == 'model_generate': response = loader.load_model_generate()
                elif session_type == 'model_predict': response = loader.load_model_predict()
                else: response = loader.get_errors()

            else: response = loader.get_errors()

            # return response
            return json.dumps(response)

        # load web-interface
        else:
            # local variables
            files = None

            # get uploaded form files
        if request.files:
            print 'jeff'
            files = request.files

        # get submitted form data
        if request.form:
            settings       = request.form
            sender         = Restructure_Data(settings, files)
            data_formatted = sender.restructure()

            # send reformatted data to brain
            loader = Load_Data(data_formatted)
            if loader.get_session_type()['session_type']:
                session_type = loader.get_session_type()['session_type']

                if session_type == 'data_new': response = loader.load_data_new()
                elif session_type == 'data_append': response = loader.load_data_append()
                elif session_type == 'model_generate': response = loader.load_model_generate()
                elif session_type == 'model_predict': response = loader.load_model_predict()
                else: response = loader.get_errors()

            else: response = loader.get_errors()

            # return response
            return json.dumps(response)

## retrieve_session: retrieve all sessions stored in the database
@app.route('/retrieve-session/', methods=['POST', 'GET'])
def retrieve_session():
    if request.method == 'POST':
        # get all sessions
        session_list = Retrieve_Session().get_all_sessions()

        # return all sessions
        if session_list['result']: return json.dumps(session_list['result'])
        else: return json.dumps({'error': session_list['error']})

## retrieve_model: retrieve all models stored in the hashed redis cache
@app.route('/retrieve-model/', methods=['POST', 'GET'])
def retrieve_model():
    if request.method == 'POST':
        # get all models
        model_list = Cache_Model().get_all_titles('svm_rbf_model')

        # return all models
        if model_list['result']: return json.dumps(model_list['result'])
        else: return json.dumps({'error': model_list['error']})

## retrieve_feature_properties: retrieve generalized features properties
#                               that can be expected for any given observation
#                               within the supplied dataset.
#
#  @label_list, this value will be a json object, since it was originally cached
#      into redis using 'json.dumps'.
@app.route('/retrieve-feature-properties/', methods=['POST', 'GET'])
def retrieve_feature_properties():
    if request.method == 'POST':
        label_list = Cache_Hset().uncache('svm_rbf_feature_labels', request.form['session_id'])

        # return all feature labels
        if label_list['result']: return json.dumps(label_list['result'])
        else: return json.dumps({'error': label_list['error']})