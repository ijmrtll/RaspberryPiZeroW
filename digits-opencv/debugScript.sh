#!/bin/bash

rm -r debug/*jpg
scp -r pi@192.168.1.69:~/digits-opencv/debug/ .
open debug/*.jpg

exit;