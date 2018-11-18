# measures the time, temperature, cpu, fanspeed of an rpi and outputs to a csv file.
# by changing fps of an rpi camera, varied cpu of the rpi to get several excel sheets to be used as inputs for a contour map.
# to start recording a video on an rpi camera, 
```
raspivid -t 305000 -w 640 -h 480 -fps 30 -b 1200000 -p 0,0,640,480 -o pivideo.h264
```
