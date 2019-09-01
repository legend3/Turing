#!/usr/bin/python
# -*-coding:utf8-*-



import paramiko
# import commands

# ssh对接
host='192.168.0.64'
user = 'root'
password = 'root'

try:
    ssh = paramiko.SSHClient()                                 # 绑定实例
    ssh.load_system_host_keys()                                # 加载本地HOST主机文件
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
    ssh.connect(host,22,user,password,timeout=5)               # 连接远程主机
    print("对接服务器成功！")
except RuntimeError as r:
    print("服务对接失败: ",r)

stdin, stdout, stderr = ssh.exec_command("touch /home/command.txt&&echo 'touch success'")
result = stdout.read(),stderr.read()# tuple
for i in result:
    print(i)


ssh.close()
# connect('192.168.0.64')


'''
2.7
commands是python2版本里的，在python3.0以上已经没有commands模块了，使用subprocess代替commands
commands模块只使用与linux的shell模式下;paramiko则可ssh连接服务器执行命令
'''
# # a = commands.getstatusoutput("echo 'hello commands'")
# print commands.getstatusoutput(ur"dir")
