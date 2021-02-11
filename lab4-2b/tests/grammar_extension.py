test = {   'name': 'grammar_extension',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> sentence = "every flight goes to a capital";\n'
                                               '>>> parse = list(parser.parse(sentence.split()))[0];\n'
                                               '>>> isinstance(interpret(parse, augmentations), bool)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sentence = "a flight leaves from Paris";\n'
                                               '>>> parse = list(parser.parse(sentence.split()))[0];\n'
                                               '>>> isinstance(interpret(parse, augmentations), bool)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sentence = "a flight leaves from London";\n'
                                               '>>> parse = list(parser.parse(sentence.split()))[0];\n'
                                               '>>> isinstance(interpret(parse, augmentations), bool)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sentence = "every flight that goes to Tel Aviv goes to a capital";\n'
                                               '>>> parse = list(parser.parse(sentence.split()))[0];\n'
                                               '>>> isinstance(interpret(parse, augmentations), bool)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sentence = "every flight that leaves from a capital goes to a capital";\n'
                                               '>>> parse = list(parser.parse(sentence.split()))[0];\n'
                                               '>>> isinstance(interpret(parse, augmentations), bool)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sentence = "every flight that goes to a capital leaves from a capital";\n'
                                               '>>> parse = list(parser.parse(sentence.split()))[0];\n'
                                               '>>> isinstance(interpret(parse, augmentations), bool)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sentence = "every flight that goes to a city leaves from a capital";\n'
                                               '>>> parse = list(parser.parse(sentence.split()))[0];\n'
                                               '>>> isinstance(interpret(parse, augmentations), bool)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
