import sys

from skimage import data, io, segmentation, color
from skimage.future import graph
from matplotlib import pyplot as plt
from scipy import misc



# img = data.coffee()

fname = 'test.png'
if len(sys.argv) > 1:
    fname = sys.argv[1]

img = misc.imread('pics/' + fname)
# scale = int(img.size)**0.5 / 150

labels1 = segmentation.slic(img, compactness=10, n_segments=400)
out1 = color.label2rgb(labels1, img, kind='avg')

g = graph.rag_mean_color(img, labels1, mode='similarity')
labels2 = graph.cut_normalized(labels1, g)
out2 = color.label2rgb(labels2, img, kind='avg')

g1 = graph.rag_mean_color(img, labels2, mode='similarity')
labels3 = graph.cut_normalized(labels2, g1)
out3 = color.label2rgb(labels3, img, kind='avg')

# plt.figure()
# io.imshow(out1)


# plt.figure()
# io.imshow(out3)
# plt.figure()
# io.imshow(out2)
# io.show()

misc.imsave('pics/filter_' + fname, out1)