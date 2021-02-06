test = {   'name': 'q_grammar_spec_4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> _g, _a = xform.parse_augmented_grammar(grammar_spec_4, globals=globals());\n'
                                               ">>> isinstance(_a[list(_g.productions())[4]]('from')(Boston), bool) \\\n"
                                               "... and isinstance(_a[list(_g.productions())[4]]('from')(NewYork), bool) \\\n"
                                               "... and isinstance(_a[list(_g.productions())[8]]('arriving')(Morning), bool) \\\n"
                                               "... and isinstance(_a[list(_g.productions())[9]]('departing')(Evening), bool)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
