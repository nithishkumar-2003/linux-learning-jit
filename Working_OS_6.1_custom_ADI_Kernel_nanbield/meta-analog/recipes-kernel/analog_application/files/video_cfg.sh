#!/bin/bash

if true
then
v4l2-ctl -v width=1920,height=1080,pixelformat=RGGB
#Configure serializer subdev
media-ctl -d "platform:fe801000.csi" --set-v4l2 '"max96717:0 23-0040":0[fmt:SRGGB8_1X8/1920x1080 field:none]'

#Configure deser subdev
media-ctl -d "platform:fe801000.csi" --set-v4l2 '"max96724:0 10-0027":0[fmt:SRGGB8_1X8/1920x1080 field:none]'

#Configure camera subdev
media-ctl -d "platform:fe801000.csi" --set-v4l2 '"imx219 24-0010":0[fmt:SRGGB8_1X8/1920x1080 field:none]'
else
v4l2-ctl -v width=1920,height=1080,pixelformat=pRAA

 #Configure serializer subdev
media-ctl -d "platform:fe801000.csi" --set-v4l2 '"max96717:0 23-0040":0[fmt:SRGGB10_1X10/1920x1080 field:none]'

#Configure deser subdev
media-ctl -d "platform:fe801000.csi" --set-v4l2 '"max96724:0 10-0027":0[fmt:SRGGB10_1X10/1920x1080 field:none]'

#Configure camera subdev
media-ctl -d "platform:fe801000.csi" --set-v4l2 '"imx219 24-0010":0[fmt:SRGGB10_1X10/1920x1080 field:none]'
fi
