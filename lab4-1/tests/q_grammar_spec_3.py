test = {   'name': 'q_grammar_spec_3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> _g, _a = xform.parse_augmented_grammar(grammar_spec_3, globals=globals());\n'
                                               ">>> isinstance(_a[list(_g.productions())[8]](Evening)('LY12'), bool)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
