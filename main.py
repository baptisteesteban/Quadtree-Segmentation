from quad_seg import QuadTreeArt
from imageio import imread

if __name__ == "__main__":
    img = imread("lena.png")
    art = QuadTreeArt(img)
    art.makeArt()
