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

valid_texts = [[100931, 869]]

# newlit biggpt2
file = open('english_files/english_biggpt2_corpus.txt', 'r')
position = file.tell()

for number in range(len(valid_texts)):

    index_of_text = valid_texts[number][1] + 1
    for i in range(index_of_text):
        english_text = file.readline()
    file.seek(position)

    array_of_words = english_text.split()
    last_array = []

    dimension = 5

    for i in range(len(array_of_words)):
        if array_of_words[i] not in svd:
            continue
        last_array.append(svd[array_of_words[i]][:dimension])

    array_of_words = last_array

    print(len(array_of_words))

    iterations = 100
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


    plt.title('Generated english text fractal dimension 10^5 words')
    # original generated
    plt.savefig('fractal dimensions a lot of words/' + "English text generated fractal dimension " + ".png")