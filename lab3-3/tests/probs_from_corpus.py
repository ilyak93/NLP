test = {   'name': 'probs_from_corpus',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> (sum(lhs_counter(corpus).values()) == sum(rule_counter(corpus).values())) \\\n'
                                               '... and (all([isinstance(k, nltk.grammar.Production) for k in rule_probs(corpus)])) \\\n'
                                               '... and (all([0 <= v <= 1 for v in rule_probs(corpus).values()])) \\\n'
                                               "... and (nltk.grammar.Production(nltk.grammar.Nonterminal('NUM'), ('one',)) in rule_probs(corpus))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
