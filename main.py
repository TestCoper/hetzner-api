from utils import *


text = \
"""
1) show all serevrs name
2) show all ip's of this token
3) delete ip addres
4) generate new address
5) assigin addresz
6) TurnServer-ON
7) creat fl ip
8) unass fl ip
"""


while True:
    clear()
    print(text)
    selec = int(input('> '))
    if selec == 0:
        break
    elif selec == 1:
        show_serversL()
    elif selec == 2:
        show_ips()
        input('Press [Enter]')
    elif selec == 3:
        delte_ip()
    elif selec == 4:
        creat_ip()
    elif selec == 5:
        AssIpToServ()
    elif selec == 6:
        TuOn()
    elif selec == 7:
        creat_ip_fl()
    elif selec == 8:
        un_ass_fl_ip()
    elif selec == 9:
        Assipfuck()


