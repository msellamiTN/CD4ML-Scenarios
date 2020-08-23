from cd4ml.model_utils import get_model_class


def train_model(train_data, target, model_name, params, seed=None):
    model_class = get_model_class(model_name)

    print("Training %s model" % model_name)
    clf = model_class(random_state=seed, **params)

    n_rows = len(train_data)
    n_cols = len(train_data[0])
    print('n_rows: %s, n_cols: %s' % (n_rows, n_cols))
    trained_model = clf.fit(train_data, target)
    return trained_model, params
