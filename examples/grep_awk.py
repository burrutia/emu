#!/usr/bin/python
# example usage for unix_util module

import os, sys, string
sys.path.append("/home/emu/modules")
import unix_util
from unix_util import shell_utils

a = shell_utils()

object = "my_secgroup  10.220.10.123 dev t1.large"
pattern = 'dev'
awkval = int('1')
a.awk(object=object,smatch=pattern,ph=awkval)
