from __future__ import absolute_import, division, print_function, unicode_literals
from modelaverage import average

modellist = ['models/mnist1.h5', 'models/mnist2.h5', 'models/mnist3.h5', 'models/mnist4.h5', 'models/mnist5.h5',
             'models/mnist6.h5', 'models/mnist7.h5', 'models/mnist8.h5', 'models/mnist9.h5']

averaged_model = average(modellist)

for w in averaged_model.get_weights():
    print(w.shape)