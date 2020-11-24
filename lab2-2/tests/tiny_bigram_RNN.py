test = {   'name': 'tiny_bigram_RNN',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> (torch.isclose(T[0,:], W @ sigma(U @ Vocab[0] + V @ h0)).all() \n'
                                               '...  and torch.isclose(T[1,:], W @ sigma(U @ Vocab[1] + V @ h0)).all())\n'
                                               'tensor(True)',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
