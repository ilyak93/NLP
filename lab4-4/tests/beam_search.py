test = {   'name': 'beam_search',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> K = 5;\n'
                                               '>>> \n'
                                               '>>> correct = 0;\n'
                                               '>>> total = 0;\n'
                                               '>>> \n'
                                               '>>> # create beam searcher;\n'
                                               '>>> beam_searcher = BeamSearcher(model);\n'
                                               '>>> \n'
                                               '>>> for batch in test_iter:\n'
                                               '...   # Input and output\n'
                                               '...   src, src_lengths = batch.src\n'
                                               '...   # Predict\n'
                                               '...   prediction, _ = beam_searcher.beam_search(src, src_lengths, K)\n'
                                               '...   # Convert to string\n'
                                               "...   prediction = ' '.join([TGT.vocab.itos[token] for token in prediction])\n"
                                               "...   prediction = prediction.lstrip('<bos>').rstrip('<eos>').strip()\n"
                                               "...   ground_truth = ' '.join([TGT.vocab.itos[token] for token in batch.tgt.view(-1)])\n"
                                               "...   ground_truth = ground_truth.lstrip('<bos>').rstrip('<eos>').strip()\n"
                                               '...   if ground_truth == prediction:\n'
                                               '...     correct += 1\n'
                                               '...     break\n'
                                               '...   total += 1\n'
                                               '...   \n'
                                               '>>> correct > 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
