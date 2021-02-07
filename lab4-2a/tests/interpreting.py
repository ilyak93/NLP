test = {   'name': 'interpreting',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> isinstance(interpret(list(parser.parse('flights'.split()))[0], augmentations), str) \\\n"
                                               "... and 'SELECT' in interpret(list(parser.parse('flights'.split()))[0], augmentations)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
