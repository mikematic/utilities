#!/bin/bash
for arg;do
file=$(echo "$arg" | sed 's/\.\w*$/''/')
mencoder "$arg" -ovc lavc -oac lavc -ffourcc DX50 -o "${file}.avi"
ffmpeg -vcodec xvid -b 300 -qmin 3 -qmax 5 -bufsize 4096 -g 300 -i "${file}.avi" -s 320x240 -aspect 4:3 -acodec aac -ab 128 -ar 48000 -ac 2 -benchmark "${file}.mp4"
rm "${file}.avi"
done
