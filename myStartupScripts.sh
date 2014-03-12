#!/bin/sh


#Start desktop Terminal
sleep 20 && gnome-terminal --window-with-profile=trans777 --geometry 103x14+400+611 &

#Start Conky
sleep 45 && conky -d -c /home/blackmatrix/Apps/conky/configs/conky.conf &

#Start Wally
sleep 10 && /usr/bin/wally &
