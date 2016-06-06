#!/usr/bin/python

'''@save_entity

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.database.save_entity import Save_Entity


def entity(dataset, session_type):
    '''@entity

    This method saves the current entity into the database, then returns the
    corresponding entity id.

    '''

    list_error = []
    premodel_settings = dataset['data']['settings']
    premodel_entity = {
        'title': premodel_settings.get('session_name', None),
        'uid': self.uid,
        'id_entity': None
    }
    db_save = Save_Entity(premodel_entity, session_type)

    # save dataset element
    db_return = db_save.save()

    # return error(s)
    if not db_return['status']:
        list_error.append(db_return['error'])
        return {'id': None, 'error': list_error}

    # return session id
    elif db_return['status'] and session_type == 'data_new':
        return {'id': db_return['id'], 'error': None}
