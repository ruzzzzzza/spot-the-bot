from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import math

def ceil_by_eps(x, eps):
  d = x / eps
  d = math.floor(d)
  x = d * eps
  return x

svd = np.load('english_files/english_newlit_SVD_dict.npy', allow_pickle=True)[()]

valid_texts = [[100931, 869]]

file = open('english_files/english_biggpt2_corpus.txt', 'r')
position = file.tell()

for number in range(len(valid_texts)):

    index_of_text = valid_texts[number][1] + 1
    # newlit biggpt2
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

    iterations = 100
    mx_eps = 1
    step = 20
    eps = 0 + mx_eps / iterations / step
    q = 4 # entropy

    values = []
    epses = []

    for i in range(iterations - 1):

        points = {}
        for i in range(len(array_of_words)):
            point = []
            for j in range(dimension):
                point.append(ceil_by_eps(array_of_words[i][j], eps))
            points[tuple(point)] = points.get(tuple(point), 0) + 1

        sum = 0
        for obj in points:
            sum += points[obj]**q

        values.append(((1 - q)**(-1))*math.log2(sum))
        epses.append(math.log2(mx_eps/eps))

        eps += mx_eps / iterations / step

    
    plt.plot(epses, values, lw = 0.5)
    plt.xlabel("log2(1/e)")
    plt.ylabel("log2(M(e))")


    plt.title('Generated english text probable dimension q=4')
    # original generated
    plt.savefig('probably dimensions/' + "English generated text fractal dimension 4" + str(number) + ".png")
    plt.clf()