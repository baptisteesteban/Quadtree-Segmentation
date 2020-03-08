from quad_seg import QuadTreeArt
from imageio import imread

if __name__ == "__main__":
    img = imread("dog.jpg")
    art = QuadTreeArt(img)
    art.makeArt()
