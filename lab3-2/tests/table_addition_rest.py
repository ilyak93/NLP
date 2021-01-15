test = {   'name': 'table_addition_rest',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # All table elements are empty or string;\n'
                                               '>>> functools.reduce(lambda x, y: x and y,\n'
                                               '...                  [all([type(item) is str for item in table.iloc[i, j]])\n'
                                               '...                   for i, j in [(i0, j0) for i0 in range(5) for j0 in range(i0+1, 5)]]) \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
