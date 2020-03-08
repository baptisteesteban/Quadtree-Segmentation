import numpy as np
import matplotlib.pyplot as plt
from queue import SimpleQueue

from .quadtree import QuadTree


class QuadTreeArt(object):
    def __init__(self, img):
        self.img = img
        self.quadtree = QuadTree(self.img, None)
        self.quadtree.construct()

    def makeArt(self, save=False):
        to_show = np.zeros(self.img.shape, dtype=np.uint8)
        q = SimpleQueue()
        q.put(self.quadtree.root)
        q.put(None)
        while not q.empty():
            node = q.get()
            if node is None:
                plt.imshow(to_show)
                plt.pause(1)
                if q.empty():
                    return
                else:
                    q.put(None)
                    continue

            rect = node.rect
            img_rect = self.img[rect.l:rect.l+rect.nrows, rect.c:rect.c+rect.ncols]
            to_show[rect.l:rect.l+rect.nrows, rect.c:rect.c+rect.ncols] = np.mean(img_rect.reshape(-1, 3), axis=0)

            if node.NW:
                q.put(node.NW)
            if node.NE:
                q.put(node.NE)
            if node.SW:
                q.put(node.SW)
            if node.SE:
                q.put(node.SE)

        plt.show()
