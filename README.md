# Python DAB ~ DoS Tool ~ By Wįłłý Fœx : @BlackVikingPro [Python]
**DoS Tool supporting 3 attack methods, soon to be more!**

-- Python D.A.B. (Deny All Bitches [ |)3|\|`/ 411 |31T(|-|3z ]) -- By: BlackVikingPro

-- Current Version: v2.0

## About
DoS (Denial of Service) tool written in Python (Python 2.7) to overflow a server with data. 

## Setup Script
> ```bash
root@ubuntu:~# dos2unix dab.py
root@ubuntu:~# chmod +x dab.py
```
> Launch!
### Initialize the Attack
```bash
root@ubuntu:~# ./dab.py --server <target> --port <port> --type http|udp|tcp --post|get --message "henlo world"
```
> Watch your target fall!

## Disclaimer
All responsibilities are at your own risk. Please use it only for research purposes

## Update(s)
Updates will hopefully be frequent. Apollogies if they come a bit late.

## Notes
* Multi-threading for more power WILL be coming soon.
* More efficient HTTP request(s) will be coming soon.
* Has been tested on Linux's Python 2.7.12

## Update notes
#### Finally v2.0 is here!
This update now consists of a new feature that allows you to port scan the target while starting
a new thread to flood that open port! Only available via TCP! 
> [ Syntax: ./dab.py --server localhost --type tcp --port-threading ]

## Update History
> #### v2.0
> * Added port scanning/threading
> * Fixed bug that broke TCP pipes

> #### v1.0
> * Initial Release
>	* **v1.1** ~ Fixed some bugs
