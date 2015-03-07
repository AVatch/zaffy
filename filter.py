import sys

import numpy as np
from skimage.future import graph
from skimage import io, segmentation, color
from scipy import misc


def _weight_mean_color(graph, src, dst, n):
    diff = graph.node[dst]['mean color'] - graph.node[n]['mean color']
    diff = np.linalg.norm(diff)
    return diff


def merge_mean_color(graph, src, dst):
    graph.node[dst]['total color'] += graph.node[src]['total color']
    graph.node[dst]['pixel count'] += graph.node[src]['pixel count']
    graph.node[dst]['mean color'] = (graph.node[dst]['total color'] /
                                     graph.node[dst]['pixel count'])

fname = 'test.png'
if len(sys.argv) > 1:
    fname = sys.argv[1]

img = misc.imread('pics/' + fname)
scale = int(img.size)**0.5 / 150

labels = segmentation.slic(img, compactness=30, n_segments=400)
g = graph.rag_mean_color(img, labels)
labels2 = graph.merge_hierarchical(labels, g, thresh=40, rag_copy=False,
                                   in_place_merge=True,
                                   merge_func=merge_mean_color,
                                   weight_func=_weight_mean_color)
g2 = graph.rag_mean_color(img, labels2)

out = color.label2rgb(labels, img, kind='avg')
out = segmentation.mark_boundaries(out, labels2, (0, 0, 0))

io.imshow(out)
io.show()
