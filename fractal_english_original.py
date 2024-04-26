from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import math

''' # выбор валидных текстов
valid_texts = []
index_of_text = 50000
with open('english_files/english_newlit_corpus.txt', 'r') as file:
    for i in range(index_of_text):
        english_text = file.readline()

        array_of_words = english_text.split()

        flag = True

        for j in range(len(array_of_words)):
            if array_of_words[j] not in svd:
                flag = False
                break

        if flag:
            valid_texts.append([len(array_of_words), i])

valid_texts = sorted(valid_texts)
print(valid_texts)
'''


def ceil_by_eps(x, eps):
  d = x / eps
  d = math.floor(d)
  x = d * eps
  return x

svd = np.load('english_files/english_newlit_SVD_dict.npy', allow_pickle=True)[()]

# original
valid_texts = [[438, 1569], [440, 7150], [440, 7358], [441, 3381], [441, 4855], [443, 7599], [444, 2271], [444, 5911], [445, 1148], [445, 1174], 
               [445, 3380], [445, 3895], [445, 5852], [445, 7281], [446, 761], [446, 4799], [446, 9830], [448, 2393], [448, 4859], [449, 389]]

for number in range(len(valid_texts)):

    index_of_text = valid_texts[number][1] + 1
    # newlit biggpt2
    with open('english_files/english_newlit_corpus.txt', 'r') as file:
        for i in range(index_of_text):
            english_text = file.readline()

    array_of_words = english_text.split()

    dimension = 8

    for i in range(len(array_of_words)):
        array_of_words[i] = svd[array_of_words[i]][:dimension]

    iterations = 80
    mx_eps = 1
    step = 20
    eps = 0 + mx_eps / iterations / step

    values = []
    epses = []

    for i in range(iterations - 1):

        points = []
        for i in range(len(array_of_words)):
            point = []
            for j in range(dimension):
                point.append(ceil_by_eps(array_of_words[i][j], eps))
            points.append(tuple(point))

        unique_points = set(points)
        count_unique_points = len(unique_points)

        values.append(math.log2(count_unique_points))
        epses.append(math.log2(mx_eps/eps))

        eps += mx_eps / iterations / step

    plt.plot(epses, values, lw = 0.5)
    plt.xlabel("log2(1/e)")
    plt.ylabel("log2(M(e))")


    plt.title('Original english text fractal dimension 400 words')
    # original generated
    plt.savefig('original fractal dimensions 400 words/' + "English text fractal dimension " + str(number) + ".png")
    plt.clf()