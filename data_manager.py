import numpy as np
import csv
import mappings


def as_arrays(ids, features):
    """
    :param csv_data:
    :return: tuple (feature matrix) * class * class * regression
    """
    data = np.array(features, dtype=np.float64)
    features = data[:,:-3]
    remission_type = np.array(data[:,-3], dtype=np.int32)
    remission_time = data[:,-2]
    days_lived  = data[:,-1]
    return np.array(ids), features, remission_type, remission_time, days_lived


def _transpose(matrix):
    return map(list, zip(*matrix))


def as_cleaned(raw_data):
    """
    :param raw_data: 2d list feature list
    :return: 2d list with all non float values converted to int/float
    """
    transposed = _transpose(raw_data) #transpose for easy iteration, only feasible with small datasets
    for feature in transposed:
        label = feature[0]
        if label in mappings.feature_mappings:
            for index in range(1, len(feature)):
                cls = feature[index]
                feature[index] = mappings.convert(label, cls)

    ids = transposed[0][1:]
    features = transposed[1:]
    features = _transpose(features)
    features = features[1:]
    for i, row in enumerate(features):
        for j, col in enumerate(row):
            if features[i][j] == 'NA':
                features[i][j] = 0
    return ids, features


def load_raw_data(csv_file):
    """
    :param csv_file:
    :return: 2d python list of raw data
    """
    datafile = csv.reader(open(csv_file, 'rb'), delimiter=',')
    return list(datafile)


def load_as_preprocessed(csv_file):
    """
    Convenience function loads raw data, cleans, and returns as tuple of features*cls*cls*reg
    :param csv_file:
    :return:
    """
    raw_data = load_raw_data(csv_file)
    ids, features = as_cleaned(raw_data)
    return as_arrays(ids, features)
