import os
import sha
import urllib

from skimage import segmentation, color
from skimage.future import graph
from scipy import misc


def filt(url):
    urllib.urlretrieve(url, os.path.join(os.getcwd(), 'tmp.png'))
    img = misc.imread('tmp.png')
    os.remove('tmp.png')

    labels1 = segmentation.slic(img, compactness=10, n_segments=400)
    out1 = color.label2rgb(labels1, img, kind='avg')

    g = graph.rag_mean_color(img, labels1, mode='similarity')
    labels2 = graph.cut_normalized(labels1, g)
    out2 = color.label2rgb(labels2, img, kind='avg')

    g1 = graph.rag_mean_color(img, labels2, mode='similarity')
    labels3 = graph.cut_normalized(labels2, g1)
    out3 = color.label2rgb(labels3, img, kind='avg')

    s = sha.new(url)
    name = s.digest().encode('hex')
    misc.imsave(os.getcwd() + '/media/{}.png'.format(name), out1)
    return name+'.png'
