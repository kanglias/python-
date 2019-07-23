import paramiko
import os
#获取ssh连接并执行shellcomand返回正确的结果
def doshell(hostname,port,username,password,shellcommand):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,port,username,password)
    stdin, stdout, stderr = ssh.exec_command(shellcommand)
    result=stdout.readlines()
    ssh.close()
    return  result
#查询内存情况
def check_mem(hostname,port,username,password):
    shellcommand = 'free -m'
    result=doshell(hostname,port,username,password,shellcommand)
    line_number=0
    for line in result:
        rs = line.split()
        if line_number == 0:
            print('[主机地址]%s' % hostname)
            print("[内存]")
        elif line_number == 2:
            print('程序使用：%s%s ' % (rs[2], 'M'))
            print('系统挪用：%s%s ' % (rs[3], 'M'))
            print("[swap]")
        else:
            print('总大小：%s%s ' % (rs[1], 'M'))
            print('空闲内存：%s%s ' % (rs[3], 'M'))
        line_number += 1
#检查硬盘情况
def check_disk(hostname,port,username,password,part):
    shellcommand = 'df -h '+part
    result = doshell(hostname, port, username, password, shellcommand)
    line_number = 0
    for line in result:
        rs = line.split()
        if line_number == 0:
            #print('[主机地址]%s' % hostname)
            print("[硬盘]")
        else :
            print('分区：%s ' % (rs[0]))
            print('总大小：%s ' % (rs[1]))
            print('空闲空间：%s ' % (rs[3]))
            print('已用空间: %s' % (rs[4]))
            mumSize = rs[4]
        line_number += 1
    return mumSize


#取出字符串中的数字
def getout_number(str):
    numbers = []
    s = str
    l = len(s)
    i = 0
    while i < l:
        num = ''
        symbol = s[i]
        while '0' <= symbol <= '9': # symbol.isdigit()
            num += symbol
            i += 1
            if i < l:
                symbol = s[i]
            else:
                break
        i += 1
        if num != '':
            numbers.append(int(num))
    number = numbers[0]

    return number

#删除该目录下的内容
def delete(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)