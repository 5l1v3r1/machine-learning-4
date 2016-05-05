#!/usr/bin/python

'''@model_predict

This file receives data (i.e. settings) required to query from the NoSQL
datastore, a previously stored SVM model, generated from 'model_generate.py'.
The determined SVM Model, is then used for analysis, based on the input data
provided during the current session, which generates an SVM prediction.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.session.base import Base
from brain.session.predict.svm import svm_prediction


class Model_Predict(Base):
    '''@Model_Predict

    This class provides an interface to generate a prediction, based on a
    specified model. Specifically, a prediction can be obtained by using the
    provided prediction feature input(s), and the stored corresponding model,
    within the NoSQL datastore.

    Note: inherit base methods from superclass 'Base'

    '''

    def __init__(self, prediction_input):
        '''@__init__

        This constructor is responsible for defining class variables, using the
        superclass 'Base' constructor, along with the
        constructor in this subclass.

        @super(), implement 'Base', and 'Base_Data' superclass constructor
            within this child class constructor.

        @self.predictors, a list of arguments (floats) required to make a
            corresponding prediction, against the respective model.

        Note: the superclass constructor expects the same 'prediction_input'
              argument.

        '''

        super(Model_Predict, self).__init__(prediction_input)
        self.prediction_input = prediction_input
        self.prediction_settings = self.prediction_input['data']['settings']
        self.model_id = self.prediction_settings['model_id']
        self.predictors = self.prediction_settings['prediction_input[]']
        self.list_error = []

    def predict(self):
        '''@predict

        This method generates a prediction with respect to the implemented
        model, using the provided prediction feature input(s), and the stored
        corresponding model, within the NoSQL datastore.

        '''

        return svm_prediction('svm', 'rbf', self.model_id, self.predictors)
