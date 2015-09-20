#!/usr/bin/python

## @validate_mime.py
#  This script performs validation on the 'mime' type for file upload(s), and returns the
#      validated temporary file references(s), along with the corresponding file extension
#      for each file upload(s).
import sys
import os.path
from brain.converter.calculate_md5 import calculate_md5

## Class: Validate_Mime, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'base_data.py'
class Validate_Mime(object):

    ## constructor: saves a subset of the passed-in form data
    def __init__(self, svm_data, svm_session=None):
        self.svm_data    = svm_data
        self.svm_session = svm_session

    ## validate: this method validates the MIME type of 'file upload(s)', provided during
    #            a 'training' session. If any of the 'file upload(s)' fails validation,
    #            this method will return False. Otherwise, the method will return a list
    #            of unique 'file upload(s)', discarding duplicates.
    def validate(self):
        # local variables
        list_error      = []

        dataset         = self.svm_data['data']['dataset']
        acceptable_type = ['csv', 'xml', 'json']

        unique_hash     = set()
        dataset_keep    = []

        if (dataset.get('file_upload', None)):

            for index, filedata in enumerate(dataset['file_upload']):
                try:
                    filehash = calculate_md5(filedata['file'])
                    # add 'hashed' value of file reference(s) to a list
                    if filehash not in unique_hash:
                        unique_hash.add(filehash)
                        file_extension = os.path.splitext(filedata['filename'])[1][1:].strip().lower()

                        # validate file_extension
                        if (file_extension not in acceptable_type):
                            msg = '''Problem: Uploaded file, \'''' + filedata['filename'] + '''\', must be one of the formats:'''
                            msg += '\n ' + ', '.join(acceptable_type)
                            list_error.append(msg)

                        # keep non-duplicated file uploads
                        else:
                            dataset_keep.append({'type': file_extension, 'file': filedata['file'], 'filename': filedata['filename']})
                except:
                    msg = 'Problem with file upload #' + filedata['filename'] + '. Please re-upload the file.'
                    list_error.append(msg)

            # replace portion of dataset with unique 'file reference(s)'
            dataset['file_upload'][:] = dataset_keep

        else:
            msg = 'No file(s) were uploaded'
            list_error.append(msg)

        # return error
        if len(list_error) > 0:
            return {'error': list_error, 'dataset': None}
        else:
            return {'error': None, 'dataset': dataset}
