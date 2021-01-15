test = {   'name': 'table_addition_rest_back',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> functools.reduce(lambda x, y: x and y,\n'
                                               '...                  [all([type(item) is tuple for item in back.iloc[i, j].values()])\n'
                                               '...                   for i, j in [(i0, j0) for i0 in range(5) for j0 in range(i0+1, 5)]]) \n'
                                               'False',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
