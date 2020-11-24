test = {   'name': 'backward',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> U = torch.Tensor([0.1]);\n'
                                               '>>> V = torch.Tensor([0.2]);\n'
                                               '>>> W = torch.Tensor([0.3]);\n'
                                               '>>> x1 = torch.Tensor([0.5]);\n'
                                               '>>> x2 = torch.Tensor([0.6]);\n'
                                               '>>> h0 = torch.Tensor([0]);\n'
                                               '>>> U.requires_grad = True;\n'
                                               '>>> h1 = torch.clamp(U * x1 + V * h0, min=0);\n'
                                               '>>> o1 = W * h1;\n'
                                               '>>> L = (o1 - x2) ** 2;\n'
                                               '>>> L.backward(retain_graph=True);\n'
                                               '>>> math.isclose(U.grad.item(), dL_dU(x1=x1, x2=x2, o1=o1, h0=h0, U=U, V=V, W=W))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
