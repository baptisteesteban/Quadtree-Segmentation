import matplotlib.pyplot as plt
from matplotlib import patches

from skimage.color import rgb2yuv

from queue import SimpleQueue


class Quad(object):
    """
    Quad representation with shape and a top-left position
    """
    def __init__(self, l, c, nrows, ncols):
        self.l = l
        self.c = c
        self.nrows = nrows
        self.ncols = ncols


class QuadTreeNode(object):
    """
    Node of the QuadTree with a value (rect) and the four partitions
    """
    def __init__(self, rect, NW=None, NE=None, SW=None, SE=None):
        self.rect = rect
        self.NW = NW
        self.NE = NE
        self.SW = SW
        self.SE = SE


class QuadTree(object):
    """
    QuadTree structure
    """
    def __init__(self, img, criterion):
        self.img = img
        self.criterion = criterion
        self.root = None
        self.ychan = rgb2yuv(img)[:, :, 0]
        self.ychan = (self.ychan - self.ychan.min()) / (self.ychan.max() - self.ychan.min())

    def _constructRec(self, node):
        rect = node.rect
        rect_img = self.ychan[rect.l:rect.l+rect.nrows, rect.c:rect.c+rect.ncols]
        if rect_img.max() - rect_img.min() > 0.25 and rect.nrows > 4 and rect.ncols > 4:
            node.NW = QuadTreeNode(Quad(rect.l, rect.c, rect.nrows // 2, rect.ncols // 2))
            node.NE = QuadTreeNode(Quad(rect.l + rect.nrows // 2, rect.c, rect.nrows - rect.nrows // 2, rect.ncols // 2))
            node.SW = QuadTreeNode(Quad(rect.l, rect.c + rect.ncols // 2, rect.nrows // 2, rect.ncols - rect.ncols // 2))
            node.SE = QuadTreeNode(Quad(rect.l + rect.nrows // 2, rect.c + rect.ncols // 2, rect.nrows - rect.nrows // 2, rect.ncols - rect.ncols // 2))

            self._constructRec(node.NW)
            self._constructRec(node.NE)
            self._constructRec(node.SW)
            self._constructRec(node.SE)

    def construct(self):
        self.root = QuadTreeNode(Quad(0, 0, self.img.shape[0], self.img.shape[1]))
        self._constructRec(self.root)

    def visualize(self):
        if self.root is None:
            raise Exception("The quadtree is not constructed")

        fig, ax = plt.subplots(1)
        ax.imshow(self.img)

        q = SimpleQueue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            rect = patches.Rectangle((node.rect.c, node.rect.l), node.rect.ncols, node.rect.nrows, linewidth=1, edgecolor='r', facecolor=None, fill=False)
            ax.add_patch(rect)

            if node.NW:
                q.put(node.NW)
            if node.NE:
                q.put(node.NE)
            if node.SW:
                q.put(node.SW)
            if node.SE:
                q.put(node.SE)

        plt.show()
