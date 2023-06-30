from hcloud import Client
import os
import time
client = Client(token="")
clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')
verselc = lambda x: 'ipv4' if x == 4 else 'ipv6'
meth_chekone = lambda x: cho_sing_or_range(1) if x == '1' else cho_sing_or_range(2)
meth_fahm = lambda x: delte_ip_single() if x == '1' else delte_ip_range()
meth_fahm_2 = lambda x: del_ip_fl_sing() if x == '1' else del_ip_fl_range()
meth_sho_ip = lambda x: show_ips_pri() if x == '1' else show_ips_fl()

chose_personale_deletone = 0


dic_allservers = {  
}

dic_allips = {
}

dic_allips_fl = {
}

# --------------- SERVER DIT SECTION ------------------#
def get_serevrs():
    servers = client.servers.get_all()
    global idip 
    idip = 0
    dic_allservers.clear()
    for i in servers:
            serv = {
            }
            serv['status'] = i.status
            serv['name'] = i.name
            serv['datacenter'] = i.datacenter
            serv['datacenter-country'] = i.datacenter.location.country
            serv['server-primary-ip4'] = i.public_net.primary_ipv4.ip
            serv['server-primary-ip6'] = i.public_net.primary_ipv6.ip
            serv['floating-ips'] = []
            for iplof in i.public_net.floating_ips:
                  serv['floating-ips'].append(iplof.ip) 
            serv['mains'] = i
            dic_allservers[idip] = serv
            idip += 1
            


def show_serversL():
      get_serevrs()
      print(dic_allservers)
      input()

def show_serversS():
      for iii in range(0, len(dic_allservers)):
            print(str(iii) + ')' + dic_allservers[iii]['name']+ ' - ' + dic_allservers[iii]['server-primary-ip4'])
            print('\n')


#--------------- IP DIT SECTION -------------------#

text_show_ip = \
"""
1) Show primary ip

2) show flo ip
"""

def show_ips():
      print(text_show_ip)
      sele_meth_show = input('select your show method > ')
      meth_sho_ip(sele_meth_show)


def get_ip_pri():
      ips = client.primary_ips.get_all()
      global idip 
      idip = 0
      dic_allips.clear()
      for ip in ips:
            detail = {}
            detail['name'] = ip.name 
            detail['ip'] = ip.ip
            detail['main'] = ip
            dic_allips[idip] = detail
            idip += 1

def show_ips_pri():
      get_ip_pri()
      clear()
      for iii in range(0, len(dic_allips)):
            print(str(iii) + ')' + dic_allips[iii]['ip'])
            print('\n')



def get_ip_fl():
      ips = client.floating_ips.get_all()
      global idip 
      idip = 0
      dic_allips_fl.clear()
      for ip in ips:
            detail = {}
            detail['name'] = ip.name 
            detail['ip'] = ip.ip
            detail['main'] = ip
            dic_allips_fl[idip] = detail
            idip += 1

def show_ips_fl():
      get_ip_fl()
      clear()
      for iii in range(0, len(dic_allips_fl)):
            print(str(iii) + ')' + dic_allips_fl[iii]['ip'])
            print('\n')


#------------ DELETE IP SECTION ----------#

text_del_ip_selo = \
"""
1) primary

2) flout ip
"""


text_del_ip = \
"""
1) delte singel ip

2) delte range ip
"""

def delte_ip():
      print(text_del_ip_selo)
      sele_meth_del = input('select your type > ')
      meth_chekone(sele_meth_del)


def cho_sing_or_range(val):
      print(text_del_ip)
      sele_meth_del = input('select your method > ')
      if (val == 1):
            meth_fahm(sele_meth_del)
      elif (val == 2):
            meth_fahm_2(sele_meth_del)

def delte_ip_single():
      show_ips_pri()
      SelDelServ = int(input("select witch server's ip you want delete > "))
      clear()
      print(dic_allips[SelDelServ]['ip'] + ' Deleted suc!!')
      dic_allips[SelDelServ]['main'].delete()
      input('Press [Enter]')


def delte_ip_range():
      get_ip_pri()
      clear()
      delnum = int(input('how many ip you want delete > '))
      SelDelServ = int(input('start from witch ip > '))
      for i in range(0, delnum):
            dic_allips[SelDelServ]['main'].delete()
            print(dic_allips[SelDelServ]['ip'] + ' Deleted suc!!')
            SelDelServ += 1
      input('Press [Enter]')

def del_ip_fl_sing():
      clear()
      show_ips_fl()
      SelDelServ = int(input("select witch server's ip you want delete > "))
      clear()
      print(dic_allips_fl[SelDelServ]['ip'] + ' Deleted suc!!')
      dic_allips_fl[SelDelServ]['main'].delete()
      input('Press [Enter]')

def del_ip_fl_range():
      clear()
      show_ips_fl()
      delnum = int(input('how many ip you want delete > '))
      SelDelServ = int(input('start from witch ip > '))
      for i in range(0, delnum):
            dic_allips_fl[SelDelServ]['main'].delete()
            print(dic_allips_fl[SelDelServ]['ip'] + ' Deleted suc!!')
            SelDelServ += 1
      input('Press [Enter]')

#------------- Creat IP SECTION ----------------#
def creat_ip():
    clear()
    NameCreatIP = input('select your ip name > ')
    get_serevrs()
    get_ip_pri()
    print('\n')
    show_serversS()
    SelServFoCreat = int(input("select witch server's ip you want craet ip > "))
    datac = dic_allservers[SelServFoCreat]['datacenter']
    while True:
        IpVerSel = int(input("select version of ip (4 or 6) > "))
        if (IpVerSel == 4 or IpVerSel == 6):
              IpUserVer = verselc(IpVerSel)
              break
        else:
              continue
    for i in range(0, 40):
          NameCreatIP = NameCreatIP + str(i)
          print(client.primary_ips.create(type=IpUserVer, datacenter=datac, name=NameCreatIP))
    input('Press [Enter]')

#-------------- ASSIGN IP SECTION--------------# 
TextSelePrOrFlT1 = \
'''
SELECT ONE OF THIS :
1) primery ip ass
2) Fl ip ass

'''

def AssIpToServ():
      seleForPrOrFl = int(input(TextSelePrOrFlT1))
      if (seleForPrOrFl == 1):
            show_ips_pri()
            SelDelServ = int(input("select witch ip you want assign > "))
            SeleIpForAss = dic_allips[SelDelServ]['main']
            clear()
      elif (seleForPrOrFl == 2):
            show_ips_fl()
            SelDelServ = int(input("select witch ip you want assign > "))
            SeleIpForAss = dic_allips_fl[SelDelServ]['main']
            clear()
      get_serevrs()
      print('\n')
      show_serversS()
      SelServFoCreat = int(input("select witch server you want assign ip > "))
      servselec = dic_allservers[SelServFoCreat]['mains'].id
      clear()
      
      if (seleForPrOrFl == 1):
            print('Turn-OFF Server....')
            dic_allservers[SelServFoCreat]['mains'].power_off()
            time.sleep(4)
            print('Un-ASSIGN Last IP...')
            dic_allservers[SelServFoCreat]['mains'].public_net.primary_ipv4.unassign()
            time.sleep(3)
            print('ASSIGN New IP...')
            seestat = SeleIpForAss.assign(assignee_id= servselec,assignee_type='server')
            time.sleep(3)
            print('Turn-ON Server....')
            dic_allservers[SelServFoCreat]['mains'].power_on()
            print(seestat.status)
      elif (seleForPrOrFl == 2):
            print('ASSIGN New IP...')
            seestat = SeleIpForAss.assign(server=dic_allservers[SelServFoCreat]['mains'])
            print(seestat.status)
      
# --------------- TurnOn server section -------------#
def TuOn():
      get_serevrs()
      print('\n')
      show_serversS()
      SelServFoCreat = int(input("select witch server you want TurnON > "))
      dic_allservers[SelServFoCreat]['mains'].power_on()
      print('Server TurndOn suc !!')
      input('Press [Enter]')


#--------- Floating ip section -------------#

def creat_ip_fl():
    clear()
    get_serevrs()
    print('\n')
    show_serversS()
    SelServFoCreat = int(input("select witch server's ip you want craet ip > "))
    serarg = dic_allservers[SelServFoCreat]['mains']
    tedad = 0
    while True:
        IpVerSel = int(input("select version of ip (4 or 6) > "))
        if (IpVerSel == 4 or IpVerSel == 6):
              IpUserVer = verselc(IpVerSel)
              break
        else:
              continue
    for i in range(0, 30):
          print(client.floating_ips.create(type=IpUserVer, server=serarg))
          tedad += 1
    input( str(tedad) + ' ip created - Press [Enter]')



def un_ass_fl_ip():
      clear()
      show_ips_fl()
      SelDelServ = int(input("select witch ip you want assign > "))
      SeleIpForAss = dic_allips_fl[SelDelServ]['main'].id
      clear()
      get_serevrs()
      print('\n')
      show_serversS()
      SelServFoCreat = int(input("select witch server you want assign ip > "))
      servselec = dic_allservers[SelServFoCreat]['mains'].id
      client.floating_ips.unassign_from_server(SeleIpForAss, servselec)
      clear()