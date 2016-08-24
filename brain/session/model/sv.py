#!/usr/bin/python

'''@sv

This file generates an sv model.

'''

from flask import current_app
from brain.database.retrieve_entity import Retrieve_Entity
from brain.cache.cache_hset import Cache_Hset
from brain.cache.cache_model import Cache_Model
from sklearn import svm, preprocessing
from log.logger import Logger
import numpy
import json


def sv_model(model, kernel_type, session_id, feature_request, list_error):
    '''@sv_model

    This method generates an sv model (i.e. svm, or svr) using feature data,
    retrieved from the database. The generated model, is then stored within the
    NoSQL datastore.

    @grouped_features, a matrix of observations, where each nested vector,
        or python list, is a collection of features within the containing
        observation.

    @encoded_labels, observation labels (dependent variable labels),
        encoded into a unique integer representation.

    '''

    # local variables
    dataset = feature_request.get_dataset(session_id)
    get_feature_count = feature_request.get_count(session_id)
    list_model_type = current_app.config.get('MODEL_TYPE')
    label_encoder = preprocessing.LabelEncoder()
    logger = Logger(__name__, 'error', 'error')

    # get dataset
    if dataset['error']:
        logger.log(dataset['error'])
        list_error.append(dataset['error'])
        dataset = None
    else:
        dataset = numpy.asarray(dataset['result'])

    # get feature count
    if get_feature_count['error']:
        logger.log(get_feature_count['error'])
        list_error.append(get_feature_count['error'])
        feature_count = None
    else:
        feature_count = get_feature_count['result'][0][0]

    # check dataset integrity, build model
    if len(dataset) % feature_count == 0:
        features_list = dataset[:, [[0], [2], [1]]]
        current_features = []
        grouped_features = []
        observation_labels = []
        feature_labels = []

        # group features into observation instances, record labels
        for index, feature in enumerate(features_list):
            if not (index+1) % feature_count == 0:
                # observation labels
                current_features.append(feature[1][0])

                # general feature labels in every observation
                if not len(feature_labels) == feature_count:
                    feature_labels.append(feature[2][0])
            else:
                # general feature labels in every observation
                if not len(feature_labels) == feature_count:
                    feature_labels.append(feature[2][0])

                current_features.append(feature[1][0])
                grouped_features.append(current_features)
                observation_labels.append(feature[0][0])
                current_features = []

        # convert observation labels to a unique integer representation
        label_encoder = preprocessing.LabelEncoder()
        label_encoder.fit(dataset[:, 0])
        encoded_labels = label_encoder.transform(observation_labels)

        # case 1: create svm model
        if model == list_model_type[0]:
            clf = svm.SVC(kernel=kernel_type)
            model_prefix = 'svm'

        # case 2: create svr model
        elif model == list_model_type[1]:
            clf = svm.SVR(kernel=kernel_type)
            model_prefix = 'svr'

        # fit model
        clf.fit(grouped_features, encoded_labels)

        # get svm title
        entity = Retrieve_Entity()
        title = entity.get_title(session_id)['result'][0][0]

        # cache model, encoded labels, title
        Cache_Model(clf).cache(
            model_prefix + '_model',
            str(session_id) + '_' + title
        )
        Cache_Model(label_encoder).cache(model_prefix + '_labels', session_id)
        Cache_Hset().cache(model_prefix + '_title', session_id, title)

        # cache feature labels, with respect to given session id
        Cache_Hset().cache(
            model_prefix + '_feature_labels',
            str(session_id),
            json.dumps(feature_labels)
        )

        # return error(s) if exists
        return {'error': list_error}
