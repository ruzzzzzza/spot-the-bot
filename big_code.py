from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import math

def ceil_by_eps(x, eps):
  d = x / eps
  d = math.floor(d)
  x = d * eps
  return x

svd = np.load('russian_files/russian_nofraglit_SVD_dict.npy', allow_pickle=True)[()]

valid_texts = [[10030, 816], [10034, 800], [10085, 2340], [10110, 690], [10118, 2203], [10137, 2254], [10142, 2199], [10146, 740], [10174, 2333], [10198, 2638], [10200, 2415], [10215, 1218], [10224, 1295], [10237, 2457], [10255, 2180], [10300, 1493], [10344, 2272], [10364, 965], [10421, 837], [10427, 1137], [10466, 2492], [10479, 230], [10518, 2300], [10556, 1135], [10584, 153], [10596, 1423], [10620, 1651], [10631, 332], [10650, 2143], [10726, 491], [10752, 2248], [10767, 1676], [10846, 162], [10858, 6], [10859, 1965], [10896, 2629], [10906, 1688], [10923, 391], [10938, 398], [10951, 1611], [10980, 1251], [10989, 1233], [11002, 2168], [11004, 2350], [11026, 2173], [11027, 1701], [11040, 20], [11055, 580], [11058, 911], [11058, 1678], [11062, 76], [11064, 1920], [11114, 1414], [11134, 1981], [11179, 2429], [11213, 945], [11251, 2069], [11270, 300], [11277, 435], [11283, 650], [11325, 1369], [11352, 213], [11354, 2335], [11378, 1026], [11427, 179], [11485, 1572], [11509, 611], [11516, 887], [11526, 1837], [11552, 2115], [11563, 1812], [11571, 191], [11608, 2235], [11644, 1666], [11645, 1962], [11713, 1946], [11716, 501], [11754, 1595], [11775, 2386], [11782, 1508], [11802, 1039], [11844, 529], [11850, 1529], [11862, 1307], [11864, 430], [11878, 1804], [11921, 24], [11942, 1547], [11951, 1546], [11973, 318], [12012, 2299], [12021, 1238], [12034, 1294], [12036, 1518], [12059, 531], [12066, 216], [12073, 1820], [12088, 2533], [12100, 659], [12120, 1594], [12207, 499], [12258, 1022], [12305, 2635], [12342, 287], [12511, 233], [12620, 2575], [12676, 2545], [12715, 1155], [12732, 1747], [12756, 1699], [12756, 2058], [12830, 167], [12833, 2250], [12844, 484], [12852, 2151], [12882, 1352], [12896, 2318], [12913, 2618], [12915, 317], [12940, 186], [12968, 1938], [12997, 833], [12997, 1367], [13003, 1008], [13028, 1362], [13137, 2123], [13143, 1796], [13147, 2051], [13193, 2511], [13208, 962], [13223, 1304], [13235, 2448], [13273, 1280], [13280, 94], [13335, 2093], [13342, 1744], [13382, 2232], [13405, 1525], [13411, 2129], [13427, 1816], [13498, 26], [13505, 892], [13637, 93], [13661, 1712], [13699, 2439], [13720, 1520], [13730, 2056], [13742, 1980], [13757, 2329], [13818, 868], [13867, 558], [13890, 616], [13921, 901], [13932, 2449], [13939, 242], [13953, 193], [13955, 1720], [13966, 1429], [13992, 2037], [13997, 2645], [14002, 1271], [14054, 849], [14078, 553], [14082, 2032], [14099, 1164], [14104, 2146], [14123, 1067], [14135, 2330], [14149, 392], [14158, 2027], [14161, 2065], [14214, 2348], [14256, 728], [14272, 908], [14274, 2475], [14342, 106], [14371, 2230], [14418, 64], [14445, 1540], [14445, 1970], [14508, 146], [14521, 1073], [14527, 1219], [14532, 1644], [14538, 2293], [14545, 1049], [14545, 1437], [14561, 707], [14576, 885], [14597, 2038], [14613, 840], [14616, 2446], [14622, 1807], [14648, 218], [14660, 1521], [14716, 2322], [14722, 1031], [14725, 252], [14729, 205], [14729, 706], [14733, 159], [14759, 361], [14795, 645], [14843, 1066], [14911, 1785], [14916, 365], [15036, 2264], [15043, 1640], [15047, 2534], [15075, 1742], [15091, 171], [15151, 2527], [15161, 1966], [15172, 861], [15195, 412], [15213, 934], [15290, 1222], [15300, 2277], [15313, 1201], [15363, 651], [15402, 2228], [15454, 1344], [15458, 1059], [15471, 296], [15504, 674], [15524, 2515], [15579, 305], [15616, 1561], [15681, 1463], [15692, 476], [15697, 575], [15700, 1252], [15705, 1632], [15721, 1625], [15822, 1461], [15827, 559], [15871, 1214], [15928, 2513], [15947, 1533], [15957, 692], [16006, 458], [16074, 1737], [16081, 1420], [16107, 958], [16135, 1671], [16157, 2461], [16211, 1042], [16238, 63], [16240, 2187], [16287, 326], [16394, 1613], [16396, 349], [16535, 2452], [16549, 177], [16573, 1880], [16576, 73], [16644, 1449], [16676, 1940], [16694, 1317], [16717, 1731], [16765, 181], [16815, 374], [16847, 35], [16847, 1719], [16901, 37], [16913, 2103], [16930, 1170], [16997, 688], [17025, 1136], [17071, 1451], [17098, 2138], [17103, 727], [17133, 138], [17159, 1379], [17180, 2098], [17207, 92], [17252, 2541], [17325, 1778], [17643, 1952], [17724, 371], [17761, 2566], [17812, 67], [17848, 415], [17870, 2490], [17965, 107], [17995, 893], [18002, 209], [18002, 2400], [18065, 2508], [18074, 1682], [18084, 2537], [18089, 2126], [18126, 937], [18139, 1610], [18170, 1125], [18253, 1721], [18260, 1191], [18275, 1863], [18290, 1445], [18294, 1819], [18307, 763], [18501, 822], [18584, 124], [18586, 1336], [18595, 18], [18600, 1554], [18605, 1992], [18619, 797], [18621, 1628], [18641, 331], [18650, 1906], [18671, 1196], [18677, 140], [18679, 909], [18764, 826], [18771, 1499], [18775, 2407], [18779, 1580], [18782, 1692], [18804, 600], [18868, 33], [18945, 1173], [18995, 1618], [18998, 39], [19052, 1681], [19080, 1553], [19108, 250], [19178, 2620], [19194, 1148], [19208, 114], [19216, 442], [19266, 2542], [19327, 1158], [19329, 713], [19375, 710], [19448, 428], [19459, 2654], [19474, 846], [19511, 1870], [19523, 1442], [19534, 1961], [19543, 2485], [19572, 927], [19585, 175], [19597, 421], [19624, 1212], [19633, 1469], [19675, 291], [19691, 2586], [19726, 1889], [19739, 1010], [19805, 388], [19847, 2095], [19916, 1433], [19974, 227], [20010, 46], [20074, 1885], [20075, 785], [20090, 1387], [20120, 666], [20152, 974], [20185, 1009], [20234, 502], [20244, 1862], [20296, 1181], [20310, 603], [20366, 2483], [20407, 2494], [20421, 299], [20460, 2096], [20496, 238], [20594, 1263], [20623, 506], [20662, 1225], [20687, 279], [20782, 372], [20803, 795], [20804, 769], [20868, 943], [20903, 523], [21010, 1342], [21030, 1171], [21048, 1017], [21064, 1316], [21145, 1760], [21154, 2384], [21180, 1531], [21306, 825], [21322, 1314], [21388, 573], [21427, 1544], [21459, 152], [21491, 1877], [21536, 629], [21539, 210], [21552, 482], [21673, 1979], [21708, 847], [21736, 357], [21751, 1855], [21777, 1206], [21960, 1994], [21989, 633], [22015, 1054], [22021, 615], [22110, 1665], [22140, 804], [22348, 1566], [22406, 346], [22437, 1389], [22448, 811], [22460, 586], [22474, 922], [22531, 1291], [22561, 634], [22673, 378], [22892, 1724], [22906, 638], [22919, 775], [23048, 1416], [23075, 224], [23142, 1277], [23142, 1732], [23237, 1424], [23274, 749], [23324, 1121], [23346, 1593], [23383, 426], [23392, 1399], [23409, 1736], [23497, 1462], [23513, 2641], [23537, 306], [23609, 1726], [23675, 475], [23759, 678], [23812, 292], [23828, 1122], [23831, 2000], [23942, 567], [24014, 1298], [24062, 1476], [24063, 1802], [24068, 996], [24122, 1011], [24159, 644], [24179, 1071], [24198, 245], [24256, 669], [24276, 509], [24281, 259], [24283, 1334], [24375, 204], [24458, 565], [24505, 286], [24641, 1312], [24699, 771], [24794, 422], [24830, 260], [24906, 2002], [25004, 197], [25031, 38], [25056, 1725], [25166, 2596], [25195, 981], [25353, 571], [25386, 2615], [25538, 871], [25609, 1444], [25658, 566], [25681, 308], [25769, 527], [25791, 1455], [25852, 1517], [25938, 1797], [25943, 1815], [25978, 1513], [25996, 1069], [26001, 1971], [26031, 539], [26084, 2634], [26104, 1913], [26113, 1814], [26138, 1881], [26282, 1408], [26294, 1188], [26489, 670], [26590, 1695], [26966, 973], [26967, 1956], [27107, 971], [27357, 1062], [27484, 1661], [27486, 1565], [27492, 1988], [27735, 72], [27779, 1702], [27790, 1378], [27796, 1968], [27799, 394], [27858, 1471], [28027, 488], [28128, 1382], [28191, 1184], [28229, 2585], [28284, 533], [28297, 2642], [28389, 1598], [28454, 199], [28459, 1376], [28481, 1357], [28496, 1036], [28669, 1982], [28748, 1636], [28761, 779], [29010, 1503], [29120, 1629], [29130, 2657], [29169, 1398], [29184, 721], [29209, 1297], [29237, 1643], [29302, 1384], [30277, 1998], [30277, 2476], [30379, 1983], [30412, 17], [30604, 265], [31365, 1798], [31907, 1758], [32997, 1198], [38143, 2646], [39410, 2481], [39906, 15], [46222, 16], [54076, 12], [55816, 3], [93950, 22], [128498, 11]]

# q = 2

qs = []

file = open('russian_files/russian_biggpt2_corpus.txt', 'r')
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
    q = 2 # entropy

    values = []
    epses = []

    for i in range(iterations - 1):


        if i != iterations - 2 and i != 14:
            
            values.append(0)
            epses.append(0)

            eps += mx_eps / iterations / step

            continue
        
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

    
    index = 0
    for i in range(len(values) - 1, -1, -1):
        if (epses[i] > 7):
            index = i
            break

    qs.append(values[index] - values[len(values) - 1])

np.savetxt('russian_generated_texts_2.txt', qs)
qs = []

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
    q = 3 # entropy

    values = []
    epses = []

    for i in range(iterations - 1):


        if i != iterations - 2 and i != 14:
            
            values.append(0)
            epses.append(0)

            eps += mx_eps / iterations / step

            continue
        
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

    
    index = 0
    for i in range(len(values) - 1, -1, -1):
        if (epses[i] > 7):
            index = i
            break

    qs.append(values[index] - values[len(values) - 1])

np.savetxt('russian_generated_texts_3.txt', qs)
qs = []

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


        if i != iterations - 2 and i != 14:
            
            values.append(0)
            epses.append(0)

            eps += mx_eps / iterations / step

            continue
        
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

    index = 0
    for i in range(len(values) - 1, -1, -1):
        if (epses[i] > 7):
            index = i
            break

    qs.append(values[index] - values[len(values) - 1])

np.savetxt('russian_generated_texts_4.txt', qs)