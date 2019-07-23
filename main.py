import check
import sys
import time
import os
#主机列表
hosts=['127.0.0.1']
#端口号
port = 22
#用户名
username = 'likang'
#密码
password = '123456'
#需要检查的分区
part = '/'
#oracle_sid
sid = "MSPROD"

#文件路径
path = "/home/likang/python/test,/home/likang/python/test1" 

#磁盘阀值
thresholdValue = 85
#将print输出保存到文件中
output=sys.stdout
outputfile=open("log.txt","a")
sys.stdout=outputfile
type = sys.getfilesystemencoding()

#记录执行时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#逐个主机检查运行情况
for hostname in hosts:
   # if hostname == '127.0.0.1':
        #两个数据库的sid不同所以在这里做了个判断
   #     sid="WHMTST"
    check.check_mem(hostname,port,username,password)
    mumSize = check.check_disk(hostname,port,username,password,part)
    print('mumSize : %s' % mumSize)
    number = check.getout_number(mumSize)
    print('number : %d' % number)
    pathList = path.split(',')
    if (number > thresholdValue):
    	for listname in pathList:
    		check.delete(listname)
    		if (number < thresholdValue):
    			break
    			pass
    		pass
   	

   #if number > 7:
    #	check.delete(path)
    #check.check_tablespace(hostname,port,username,password,sid)
    print("\n\n")