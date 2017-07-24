#!/bin/bash
echo "Shutdown started web server..."
ps -ef | grep run.py | awk '{print $2}' | xargs kill -9

echo "Kill all fio processes..."
pkill -9 fio

echo "Kill iostat process..."
pkill -9 iostat

echo "Start fio..."
nohup fio --filename=/dev/nvme0n1 -rw=read -numjobs=4 -iodepth=32 -ioengine=libaio -offset=100G -bs=128k -direct=1 -name=starblaze_demo --group_reporting  -random_generator=tausworthe64 -loop=100 &

echo "Start iostat..."
nohup iostat -x 1 >> /root/starblaze_demo/app/stat_file/iostat.log &

echo "Copy correct web template..."
cp /root/starblaze_demo/app/templates/128K_SEQUENTIAL_READ.html /root/starblaze_demo/app/templates/index.html

echo "Start web server..."
nohup python ../run.py &
