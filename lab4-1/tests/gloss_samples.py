test = {   'name': 'gloss_samples',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> def _check(string, tests):\n'
                                               '...   """Verify that all the tests are satisfied in that some string \n'
                                               '...   in each test exists in the answer"""  \n'
                                               '...   return all(map(lambda subtest: any(map(lambda substr: substr in string, \n'
                                               '...                                          subtest)),\n'
                                               '...                  tests));\n'
                                               '>>> _tests1 =[["exists", "is", "some"]];\n'
                                               '>>> _tests2 = [["all", "every", "each"]];\n'
                                               '>>> _check(gloss1.lower(), _tests1) and _check(gloss2.lower(), _tests2)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
