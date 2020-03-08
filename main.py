from quad_seg import QuadTree
from imageio import imread

if __name__ == "__main__":
    img = imread("lena.png")
    quadtree = QuadTree(img, None)
    quadtree.construct()
    quadtree.visualize()
