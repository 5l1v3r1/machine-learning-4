#!/usr/bin/python

'''@base

This file serves as the superclass for 'data_xx.py', and 'model_xx.py' files.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

import sys
from brain.validator.validate_settings import Validate_Settings


class Base(object):
    '''@Base

    This class provides a general base class, used for the following sessions,
    and within their corresponding classes:

        - data_new
        - data_append
        - model_generate
        - model_predict

    Note: this class is invoked within 'data_xx.py', 'model_xx.py'

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data):
        '''@__init__

        This constructor is responsible for defining class variables.

        '''

        self.premodel_data = premodel_data
        settings = self.premodel_data['data']['settings']
        self.session_type = settings['session_type']
        self.list_error = []

    def validate_arg_none(self):
        '''validate_arg_none

        This method checks if the class variable 'premodel_data' is defined.

        '''

        if self.premodel_data is None:
            return True
        else:
            return False

    def validate_premodel_settings(self):
        '''@validate_premodel_settings

        This method validates the provided settings (not the dataset), that
        describe the session.

        '''

        validate = Validate_Settings(
            self.premodel_data,
            self.session_type
        )

        validated = validate.validate()

        if validated['error'] is not None:
            self.list_error.append(validated['error'])

    def get_errors(self):
        '''@get_errors

        This method returns all current errors associated with this class.

        '''

        return self.list_error

    def check(self):
        '''@check

        This method checks if current class instance contains any errors. If
        any error(s) exists, it is printed, and the program exits.

        '''

        if len(self.list_error) > 0:
            for error in self.list_error:
                print error
            sys.exit()
