test = {   'name': 'pcfg_to_dict',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(pcfg_to_dict(probabilistic_arithmetic_grammar), dict) \\\n'
                                               '... and all([(isinstance(k, nltk.grammar.Production)) and (0 <= v <= 1) for k,v in pcfg_to_dict(probabilistic_arithmetic_grammar).items()])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
