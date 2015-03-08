# import cv2
import numpy as np,sys

# import sys

# from skimage import data, io, segmentation, color
# from skimage.future import graph
# from matplotlib import pyplot as plt
# from scipy import misc

# import cv2
# import numpy as np

# # img = cv2.imread('messi5.jpg',0)
# # edges = cv2.Canny(img,100,200)

# # plt.subplot(121),plt.imshow(img,cmap = 'gray')
# # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# # plt.show()


# # img = data.coffee()

# fname = 'test.png'
# if len(sys.argv) > 1:
#     fname = sys.argv[1]

# img = misc.imread('pics/' + fname)
# # scale = int(img.size)**0.5 / 150

# labels1 = segmentation.slic(img, compactness=30, n_segments=400)
# out1 = color.label2rgb(labels1, img, kind='avg')

# # g = graph.rag_mean_color(img, labels1, mode='similarity')
# # labels2 = graph.cut_normalized(labels1, g)
# # out2 = color.label2rgb(labels2, img, kind='avg')

# # plt.figure()
# # io.imshow(out1)
# # plt.figure()
# # io.imshow(out2)
# # io.show()

# edges = cv2.Canny(out1,100,200)
# # plt.subplot(121),plt.imshow(img,cmap = 'gray')
# # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()