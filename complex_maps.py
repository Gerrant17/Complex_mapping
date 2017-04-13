"""Grant Arras."""
# MTH 402 complex mapping using matplotlib pyplot
from matplotlib import pyplot
# matplotlib.org

csquare = [(0 + 0j), (0 + 5j), (5 + 0j), (5 + 5j)]
# Shape of a N for point order in list


def chorizontal(left, right):
    """Connect two points to form a horizontal line."""
    newl = [left]
    while left != right:
        left += 1
        newl.append(left)
    return newl


def cvertical(bot, top):
    """Connect two points to form a vertical line."""
    newl = [bot]
    while bot != top:
        bot += 1j
        newl.append(bot)
    return newl


def cgen_square(square):
    """Make a list of complex numbers that form a square when plotted."""
    plotted = chorizontal(square[0], square[2])
    plotted.extend(chorizontal(square[1], square[3]))
    plotted.extend(cvertical(square[0], square[1]))
    plotted.extend(cvertical(square[2], square[3]))
    return list(set(plotted))

print(cgen_square(csquare))

pyplot.figure(figsize=(16, 16), dpi=100)
cset = cgen_square(csquare)
cu = list(map(lambda z: z.real, cset))
cv = list(map(lambda z: z.imag, cset))
pyplot.scatter(cu, cv)
pyplot.xlabel('reals')
pyplot.ylabel('imags')
pyplot.title('Basic 5x5 Square')
pyplot.savefig('../csquare.png')
pyplot.close()


def translate(num):
    """Translate point + (2 + 2j)."""
    return num + (2 + 2j)

pyplot.figure(figsize=(16, 16), dpi=100)
newcset = list(map(translate, cset))
newcu = list(map(lambda z: z.real, newcset))
newcv = list(map(lambda z: z.imag, newcset))
pyplot.scatter(newcu, newcv)
pyplot.xlabel('reals')
pyplot.ylabel('imags')
pyplot.title('Translated + (2 + 2j)')
pyplot.savefig('../csquare_trans.png')
pyplot.close()


def magnify(num):
    """Magnify point by 2."""
    return num * 2

pyplot.figure(figsize=(16, 16), dpi=100)
magcset = list(map(magnify, cset))
magcu = list(map(lambda z: z.real, magcset))
magcv = list(map(lambda z: z.imag, magcset))
pyplot.scatter(magcu, magcv)
pyplot.xlabel('reals')
pyplot.ylabel('imags')
pyplot.title('Magnified by 2')
pyplot.savefig('../csquare_mag.png')
pyplot.close()


def rotate(num):
    """Rotate by 45 degrees."""
    return num * complex(((2 ** .5) / 2), ((2 ** .5) / 2))

pyplot.figure(figsize=(16, 16), dpi=100)
rotcset = list(map(rotate, cset))
rotcu = list(map(lambda z: z.real, rotcset))
rotcv = list(map(lambda z: z.imag, rotcset))
pyplot.scatter(rotcu, rotcv)
pyplot.xlabel('reals')
pyplot.ylabel('imags')
pyplot.title('Rotated 45 degrees')
pyplot.savefig('../csquare_rot.png')
pyplot.close()


pyplot.figure(figsize=(16, 16), dpi=100)
magtranset = list(map(magnify, newcset))
comset = list(map(rotate, magtranset))
comu = list(map(lambda z: z.real, comset))
comv = list(map(lambda z: z.imag, comset))
pyplot.scatter(comu, comv)
pyplot.xlabel('reals')
pyplot.ylabel('imags')
pyplot.title('5x5 Square, Trans + (2 + 2j), Mag by 2, Rotated 45 degrees')
pyplot.savefig('../csquare_tmr.png')
pyplot.close()

# square = [(0, 0), (0, 5), (5, 0), (5, 5)]


# def horizontal_line(left, right):
#     newl = []
#     for i in range(right[0] - left[0] + 1):
#         newl.append((left[0] + i, left[1]))
#     return newl


# def vertical_line(bot, top):
#     newl = []
#     for i in range(top[1] - bot[1] + 1):
#         newl.append((bot[0], bot[1] + i))
#     return newl


# def gen_square(square):
#     plotted = horizontal_line(square[0], square[2])
#     plotted.extend(horizontal_line(square[1], square[3]))
#     plotted.extend(vertical_line(square[0], square[1]))
#     plotted.extend(vertical_line(square[2], square[3]))
#     return plotted
# print(gen_square(square))

# pyplot.figure(figsize=(16, 16), dpi=100)
# pyplot.scatter(*zip(*gen_square(square)))
# pyplot.savefig('square.png')
# pyplot.close()


# def t(numtup):
#     return (numtup[0], numtup[1] + 2)


# pyplot.figure(figsize=(16, 16), dpi=100)
# pyplot.scatter(*zip(*list(map(t, gen_square(square)))))
# pyplot.savefig('square2.png')
# pyplot.close()


# def m(numtup):
#     return (2 * numtup[0], 2 * numtup[1])


# pyplot.figure(figsize=(16, 16), dpi=100)
# pyplot.scatter(*zip(*list(map(m, gen_square(square)))))
# pyplot.savefig('square3.png')
# pyplot.close()


# def f(num):
#     """Complex function."""
#     return num ** 2


# def trans(cnum):
#     """Translation."""
#     return cnum + complex(0, 3)


# real = [0, 1, 0, 1]
# imag = [0, 0, complex(0, 1), complex(0, 1)]
# mset = []
# for i in range(10):
#     mset.append(complex(i, i))
# newmset = list(map(f, mset))
# u = list(map(lambda z: z.real, newmset))
# v = list(map(lambda z: z.imag, newmset))
# pyplot.figure(figsize=(16, 16), dpi=100)
# pyplot.scatter(u, v)
# pyplot.xlabel('reals')
# pyplot.ylabel('imags')
# pyplot.title('my title')
# pyplot.grid = True
# pyplot.savefig('../image.png')
# pyplot.close()
# tnewmset = list(map(trans, newmset))
# newu = list(map(lambda z: z.real, tnewmset))
# newv = list(map(lambda z: z.imag, tnewmset))
# pyplot.figure(figsize=(16, 16), dpi=100)
# pyplot.scatter(newu, newv)
# pyplot.xlabel('reals')
# pyplot.ylabel('imags')
# pyplot.title('my title')
# pyplot.grid = True
# pyplot.savefig('../trans_image.png')
# pyplot.close()
