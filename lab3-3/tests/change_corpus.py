test = {   'name': 'change_corpus',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> sopnum_prod = nltk.grammar.Production(nltk.grammar.Nonterminal('S'),\n"
                                               "...                                       [nltk.grammar.Nonterminal('S'),\n"
                                               "...                                        nltk.grammar.Nonterminal('OP'),\n"
                                               "...                                        nltk.grammar.Nonterminal('NUM')]);\n"
                                               ">>> numops_prod = nltk.grammar.Production(nltk.grammar.Nonterminal('S'),\n"
                                               "...                                       [nltk.grammar.Nonterminal('NUM'),\n"
                                               "...                                        nltk.grammar.Nonterminal('OP'),\n"
                                               "...                                        nltk.grammar.Nonterminal('S')]);\n"
                                               '>>> sopnum_prob = rule_probs(corpus_new)[sopnum_prod];\n'
                                               '>>> numops_prob = rule_probs(corpus_new)[numops_prod];\n'
                                               '>>> (0 <= numops_prob <= 1) and (0 <= sopnum_prob <= 1)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
