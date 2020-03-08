from quad_seg import QuadTreeArt
from imageio import imread

from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input", help="Input image to make the art")
    parser.add_argument("-s", "--saveimages", help="Save the output images", action="store_true")
    parser.add_argument("--min_nrows", type=int, default=4, help="Minimum number of rows of a node rectangle")
    parser.add_argument("--min_ncols", type=int, default=4, help="Minimum number of columns of a node rectangle")
    args = parser.parse_args()
    
    img = imread(args.input)
    art = QuadTreeArt(img, args.min_nrows, args.min_ncols)
    art.makeArt(args.saveimages)
