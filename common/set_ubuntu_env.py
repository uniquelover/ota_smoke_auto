#!/usr/bin/env python2

"""
USAGE: Set temp environment for ubuntu os before execute ota auto test
DATE: 12/25/2020
"""

from time import sleep
import os


try:  # py3
    from shlex import quote
except ImportError:  # py2
    from pipes import quote

# -------------SET ESYNC HOME DIR-----------------------

esync_path = '/home/excelfore/Documents/excelfore/esync'
print('export ESYNC_HOME_DIR={}'.format(quote(esync_path)))

if os.environ['ESYNC_HOME_DIR'] == '/home/excelfore/Documents/excelfore/esync':
    print('set ESYNC_HOME successfully')

else:
    print('failed to set ESYNC_HOME')


# sleep(5)


# ------------SET LD LIBRARY PATH--------------------- 


ld_path='/home/excelfore/Documents/excelfore/esync/lib'

print('export LD_LIBRARY_PATH={}'.format(quote(ld_path)))


# if os.environ['LD_LIBRARY_PATH'] == '/home/excelfore/Documents/excelfore/esync/lib':
#     print('set LD_LIBRARY_PATH successfully')

# else:
#     print('failed to set LD_LIBRARY_PATH')





