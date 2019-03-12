"""
      code by Tae Hwan Jung(Jeff Jung) @graykode
      code reference : https://stackoverflow.com/questions/48212110/average-weights-in-keras-models
"""
import os
import tensorflow as tf
import numpy as np

def average(modelfiles):
    """
    :param modelfiles: list of model file names.
    :return: averaged weight model
    """
    if len(modelfiles) == 0:
        raise Exception('model file is not found')

    modelfiles = [os.path.abspath(path) for path in modelfiles]
    models = []
    for idx, file in enumerate(modelfiles):
        models.append(tf.keras.models.load_model(file, compile=False))
        print('%d/%d files loaded' % (idx + 1, len(modelfiles)))

    weights = [model.get_weights() for model in models]
    new_weights = list()
    for weights_list_tuple in zip(*weights):
        new_weights.append([np.array(weights_).mean(axis=0) \
             for weights_ in zip(*weights_list_tuple)])

    model = tf.keras.models.load_model(modelfiles[0], compile=False)
    model.set_weights(new_weights)
    return model