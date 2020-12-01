test = {   'name': 'ffnn_ppl',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> ppl_madison_model_madison_document>1 and ppl_hamilton_model_madison_document>1 and ppl_madison_model_hamilton_document>1 and '
                                               'ppl_hamilton_model_hamilton_document>1\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> ppl_madison_model_madison_document < ppl_hamilton_model_madison_document and ppl_hamilton_model_hamilton_document < '
                                               'ppl_madison_model_hamilton_document\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> ppl_madison_model_madison_document < ppl_madison_model_hamilton_document and ppl_hamilton_model_hamilton_document < '
                                               'ppl_hamilton_model_madison_document\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
