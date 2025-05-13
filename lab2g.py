#!/usr/bin/env python3
# Author: Md. Shahriar Zaman
# Author ID: mzaman30
# Date Created: 2025/05/13

import sys

if len(sys.argv) != 2:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
