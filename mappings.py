feature_types = {
    'YES_NO': {
        'YES': 1,
        'NO': 0
    },

    'POS_NEG': {
        'POS': 1,
        'NEG': 0,
        'ND': -1,
    },
}


feature_mappings = {
    'SEX': {
        'F': 1,
        'M': 0
    },

    'PRIOR.MAL': feature_types['YES_NO'],

    'PRIOR.CHEMO': feature_types['YES_NO'],

    'PRIOR.XRT': feature_types['YES_NO'],

    'Infection': feature_types['YES_NO'],

    'ITD': feature_types['POS_NEG'],

    'D835': feature_types['POS_NEG'],

    'Ras.Stat': feature_types['POS_NEG'],

    'Chemo.Simplest': {
        'Anthra-Plus': 0,
        'Anthra-HDAC': 1,
        'HDAC-Plus': 2,
        'Flu-HDAC': 3,
        'StdAraC-Plus': 4,
    }
}


def convert(type, label):
    """
    :param label:
    :return:
    """
    return feature_mappings['type']['label']
