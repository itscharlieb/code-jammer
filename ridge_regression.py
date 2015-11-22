import data_manager
import invert

csv_data_file = 'data.csv'
ids, ftrs, tps, tms, dl = data_manager.load_as_preprocessed(csv_data_file)

def sub(matr_a, matr_b):
    return map(lambda i: map(lambda x, y: x - y, matr_a[i], matr_b[i]), xrange(len(matr_a)))


def mult(a, b):
    zip_b = zip(*b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


def trans(matrix):
    return map(list, zip(*matrix))


def inv(matrix):
    return invert.invert(matrix)


def id(size, diag=1):
    return lambda size: [[diag * int(i == j) for i in range(size)] for j in range(size)]


def optimal_weights(samples, values, r):
    x_trans = trans(samples)
    r_id = id(len(samples[0]), r)
    inner = sub(mult(x_trans, samples), r_id)
    return mult(inner, mult(x_trans, values))

