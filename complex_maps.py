"""Grant Arras."""
# MTH 402 complex mapping using matplotlib pyplot
from matplotlib import pyplot
# matplotlib.org

csquare = [(0 + 0j), (0 + 5j), (5 + 0j), (5 + 5j)]
# Order points in list to the shape of a N


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

# Graphing the unaltered 5x5 square
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

# Function to translate points by (2 + 2i)


def translate(num):
    """Translate point + (2 + 2j)."""
    return num + (2 + 2j)

# Graphing the translated square
pyplot.figure(figsize=(16, 16), dpi=100)
newcset = list(map(translate, cset))
newcu = list(map(lambda z: z.real, newcset))
newcv = list(map(lambda z: z.imag, newcset))
pyplot.scatter(newcu, newcv)
pyplot.xlabel('reals')
pyplot.ylabel('imags')
pyplot.title('5x5 square under f(z) = z + (2 + 2j)')
pyplot.savefig('../csquare_trans.png')
pyplot.close()

# Function to magnify points by 2


def magnify(num):
    """Magnify point by 2."""
    return num * 2

# Graphing the magnified square
pyplot.figure(figsize=(16, 16), dpi=100)
magcset = list(map(magnify, cset))
magcu = list(map(lambda z: z.real, magcset))
magcv = list(map(lambda z: z.imag, magcset))
pyplot.scatter(magcu, magcv)
pyplot.xlabel('reals')
pyplot.ylabel('imags')
pyplot.title('5x5 square under f(z) = 2z')
pyplot.savefig('../csquare_mag.png')
pyplot.close()

# Funtion to rotate points by e^i(pi/4)


def rotate(num):
    """Rotate point by 45 degrees."""
    return num * complex(((2 ** .5) / 2), ((2 ** .5) / 2))

# Graphing the rotated square
pyplot.figure(figsize=(16, 16), dpi=100)
rotcset = list(map(rotate, cset))
rotcu = list(map(lambda z: z.real, rotcset))
rotcv = list(map(lambda z: z.imag, rotcset))
pyplot.scatter(rotcu, rotcv)
pyplot.xlabel('reals')
pyplot.ylabel('imags')
pyplot.title('5x5 square under f(z) = ((2 ** .5) / 2 + j((2 ** .5) / 2))z')
pyplot.savefig('../csquare_rot.png')
pyplot.close()

# Function to map f(z) = az +b


def clm(num):
    """Complex Linear mapping of num."""
    return complex((2 ** .5), (2 ** .5)) * num + (2 + 2j)

# Graphing the 5x5 square that has been translated, magnified, and rotated

pyplot.figure(figsize=(16, 16), dpi=100)
clmset = list(map(clm, cset))
clmu = list(map(lambda z: z.real, clmset))
clmv = list(map(lambda z: z.imag, clmset))
pyplot.scatter(clmu, clmv)
pyplot.xlabel('reals')
pyplot.ylabel('imags')
pyplot.title(
    '5x5 Square under f(z) = ((2 ** .5)+ j(2 ** .5))z + (2 + 2j)')
pyplot.savefig('../csquare_clm.png')
pyplot.close()

print('Done!')  # Notify user that code ran successfully

# Following code was used for testing pyplot in real numbers before altering to
# complex numbers above
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
# pyplot.xlabel('reals')
# pyplot.ylabel('imags')
# pyplot.title('my title')
# pyplot.savefig('square.png')
# pyplot.close()


# def t(numtup):
#     return (numtup[0], numtup[1] + 2)


# pyplot.figure(figsize=(16, 16), dpi=100)
# pyplot.scatter(*zip(*list(map(t, gen_square(square)))))
# pyplot.xlabel('reals')
# pyplot.ylabel('imags')
# pyplot.title('my title')
# pyplot.savefig('square2.png')
# pyplot.close()


# def m(numtup):
#     return (2 * numtup[0], 2 * numtup[1])


# pyplot.figure(figsize=(16, 16), dpi=100)
# pyplot.scatter(*zip(*list(map(m, gen_square(square)))))
# pyplot.xlabel('reals')
# pyplot.ylabel('imags')
# pyplot.title('my title')
# pyplot.savefig('square3.png')
# pyplot.close()


# def f(num):
#     """Complex function."""
#     return num ** 2


# def trans(cnum):
#     """Translation."""
#     return cnum + complex(0, 3)

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
