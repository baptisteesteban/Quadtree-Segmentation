# QuadTree Segmentation

This application is made to create some art with quadtree.

The idea of this project came to me looking at [this repository](https://github.com/fogleman/Quads).

It needs some improvements but it is a beginning.

With the `-s` option, you can generate a *res_img/* directory, containing the images of each level of the quadtree.

These images can be converted to a video using `ffmpeg`. The `make_video.sh` automatically create this video, in `mp4` file format.

##### Quadtree criterion

The criterion to split the image can be changed. It is a function which takes an image and returns a boolean. I use a simple criterion based
on the difference of the minimum value and the maximum value of the normalized Y channel of the image in YUV colorspace.

It is a simple criterion, so I am looking for a new criterion.
