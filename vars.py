from socket import *
import netifaces as ni

hostname = gethostname()
try:
    host = gethostbyname(hostname)
except gaierror:
    host = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']

global SYSTEM_IP
SYSTEM_IP = host

global SYSTEM_PORT
SYSTEM_PORT = 15600

global has_ended
has_ended = False


global chat_log
chat_log = ''