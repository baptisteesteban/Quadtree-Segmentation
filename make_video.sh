#!/bin/bash

ffmpeg -r 1 -i res_img/img%d.png -vcodec mpeg4 art.mp4
