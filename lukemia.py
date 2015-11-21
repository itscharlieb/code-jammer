import numpy as np
import sklearn
import csv
import mappings


def as_array(csv_data):
    """
    :param csv_data:
    :return: tuple (feature matrix) * class * class * regression
    """
    data = np.genfromtxt(csv_data)
    features = data[:,:-3]
    clss1 = data[:,-3]
    clss2 = data[:,-2]
    rgrs  = data[:,-1]
    return features, clss1, clss2, rgrs


def _transpose(matrix):
    return map(list, zip(*matrix))


def as_cleaned(raw_data):
    """
    :param raw_data: 2d list feature list
    :return: 2d list with all non float values converted to int/float
    """
    transposed = _transpose(raw_data) #transpose for easy iteration, only useful for small datasets
    for feature_index, feature in enumerate(transposed):
        label = feature[0]
        if label in mappings.feature_mappings:
            for index in range(1, len(feature)):
                cls = feature[index]
                feature[index] = mappings.convert(label, cls)
    features = _transpose(transposed)
    return features[1:]


def load_raw_data(csv_file):
    """
    :param csv_file:
    :return: 2d python list of raw data
    """
    datafile = csv.reader(open(csv_file, 'rb'), delimiter=',')
    return list(datafile)


