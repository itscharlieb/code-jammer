import data_manager
import numpy as np
from sklearn import svm, grid_search
from sklearn.feature_selection import SelectPercentile
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn import decomposition
from sklearn import tree
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import BaggingClassifier


def build_pipelines(ls, ss):
    pipelines = []
    for learner_tup, learner_params in ls.items():
        for selector_tup, selector_params in ss.items():
            learner_name = learner_tup[0]
            learner = learner_tup[1]
            selector_name = selector_tup[0]
            selector = selector_tup[1]
            pipe = Pipeline([
                (selector_name, selector),
                (learner_name, learner)
            ])
            params = dict(learner_params, **selector_params)
            pipelines.append((pipe, params))
    return pipelines

selectors = {
    ('percentile', SelectPercentile()): {
        'percentile__percentile': (1, 5)
    }

    # ('pca', decomposition.PCA()): {
    #     'pca__n_components': (2, 4, 8, 16, 32)
    # }
}

learners = {
    # ('bag', BaggingClassifier()): {
    #     'bag__base_estimator': (svm.SVC(C=1, kernel='linear'),),
    #     'bag__n_estimators': (10,)
    # }
    ('svc', svm.SVC()): {
        'svc__C': (0.1, 1.0, 10.0, 100.0, 1000.0),
        'svc__kernel': ('rbf', 'sigmoid', 'linear')
    }

    # ('lr', LogisticRegression()): {
    #     'lr__penalty': ('l1', 'l2'),
    #     'lr__C': (1.0, 2.0)
    # },
}

#load data
csv_data_file = 'data.csv'
ids, ftrs, tps, tms, dl = data_manager.load_as_preprocessed(csv_data_file)

ftrs = ftrs[:,34:-1]


pipeline = build_pipelines(learners, selectors)
for pipe, params in pipeline:
    grid = grid_search.GridSearchCV(pipe, params, cv=10)
    grid.fit(ftrs, tps)
    for score in grid.grid_scores_:
        print(score.parameters, \
              '[Mean]          = %5.4f%%' % score.mean_validation_score, \
              '[Std Deviation] = %5.4f%%' % np.std(score.cv_validation_scores))

