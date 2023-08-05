# defgw
Get default gateway interface / IP (for Linux)

Parses/decodes /proc/net/route and prints def gw information

## Install
~~~
pip3 install getdefgw
~~~

## Usage
~~~
$ getdefgw 
192.168.100.245

$ getdefgw --dev
wlp8s0
~~~