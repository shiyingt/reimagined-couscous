### Objective
Generate temperature, CPU, fanspeed of an rpi to be used as inputs for a contour map.
### Methodology
Information about the core temperature and CPU of an rpi can be derived straight from the rpi.
Varied fanspeed by changing duty cycle of pwm pin.
Varied fps of an rpi camera to get varied cpu.
1. Ran a script in the background to measure time, temperature, cpu, fanspeed of an rpi and output data to a csv file.
to run a script in the background, add append(&) to the file name,
```
sudo python monitor-svc-log.py&
```
2. Recorded various videos at different fps.
to start recording a video on an rpi camera, 
```
raspivid -t 305000 -w 640 -h 480 -fps 30 -b 1200000 -p 0,0,640,480 -o pivideo.h264
```
