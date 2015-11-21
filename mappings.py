feature_types = {
    'yes_no': {
        'yes': 1,
        'no': 0,
    },

    'pos_neg': {
        'pos': 1,
        'neg': 0,
        'nd': -1,
        'notdone': -1
    },
}


feature_mappings = {
    'SEX': {
        'f': 1,
        'm': 0
    },

    'PRIOR.MAL': feature_types['yes_no'],

    'PRIOR.CHEMO': feature_types['yes_no'],

    'PRIOR.XRT': feature_types['yes_no'],

    'Infection': feature_types['yes_no'],

    'ITD': feature_types['pos_neg'],

    'D835': feature_types['pos_neg'],

    'Ras.Stat': feature_types['pos_neg'],

    'Chemo.Simplest': {
        'anthra-plus': 0,
        'anthra-hdac': 1,
        'hdac-plus': 2,
        'flu-hdac': 3,
        'stdarac-plus': 4,
    },

    'resp.simple': {
        'complete_remission': 0,
        'resistant': 1,
        'na': 2
    }
}


def convert(label, cls):
    """
    :param label:
    :return:
    """
    return feature_mappings[label][cls.lower()]
