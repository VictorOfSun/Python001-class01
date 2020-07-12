****1. ping的实现 - subprocess 模块****    
运行python的时候，我们都是在创建并运行一个进程。像Linux进程那样，一个进程可以fork一个子进程，并让这个子进程exec另外一个程序。在``Python中，我们通过标准库中的subprocess包来fork一个子进程，并运行一个外部的程序。
subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。
subprocess 模块首先推荐使用的是它的 run 方法，更高级的用法可以直接使用 Popen 接口。

run 方法语法格式如下：    
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
args：表示要执行的命令。必须是一个字符串，字符串参数列表。            
stdin、stdout 和 stderr：子进程的标准输入、输出和错误。其值可以是 subprocess.PIPE、subprocess.DEVNULL、一个已经存在的文件描述符、已经打开的文件对象或者 None。subprocess.PIPE 表示为子进程创建新的管道。subprocess.DEVNULL 表示使用 os.devnull。默认使用的是 None，表示什么都不做。另外，stderr 可以合并到 stdout 里一起输出。
timeout：设置命令超时时间。如果命令执行时间超时，子进程将被杀死，并弹出 TimeoutExpired 异常。            
check：如果该参数设置为 True，并且进程退出状态码不是 0，则弹 出 CalledProcessError 异常。             
encoding: 如果指定了该参数，则 stdin、stdout 和 stderr 可以接收字符串数据，并以该编码方式编码。否则只接收 bytes 类型的数据。              
shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。           
run 方法调用方式返回 CompletedProcess 实例，和直接 Popen 差不多，实现是一样的，实际也是调用 Popen，与 Popen 构造函数大致相同，例如:              
实例： 执行ls -l /dev/null 命令
>>> subprocess.run(["ls", "-l", "/dev/null"])
crw-rw-rw-  1 root  wheel    3,   2  5  4 13:34 /dev/null
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0)
returncode: 执行完子进程状态，通常返回状态为0则表明它已经运行完毕，若值为负值 "-N",表明子进程被终。


**2.Python获取代码运行时间的四种方法**    
程序执行时间 = cpu时间 + io时间 + 休眠或者等待时间    
https://blog.csdn.net/zdx1996/article/details/86583676?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight     


**3.获取命令行参数--argparse模块简介**    
https://www.cnblogs.com/yimiaoyikan/p/10375859.html    

**4.第二题的数据去重**
1) 在写入数据库之前，先根据 data 去数据库查一下，看看有没有这条数据
2) 使用 Python 的 set 类型来存储每次的抓取结果，爬虫抓取完成最后在将 set 里的数据写入数据库   


**5.set()增加数据的方法**   
````
s = set()      
s.add(x)            # 添加一项          
s.update(x)         # 在s中添加多项  
````


**6.进程池，线程池创建**  
```` 
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
with ThreadPoolExecutor(n) as executor:
with ProcessPoolExecutor(n) as executor:
````


**7.把数据保存成json格式**   
````
with open(file_name, 'w') as f:
    json.dump(data, f)
````

**8.tcp**   
操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 Python 自带的 socket 套接字。   
socket: https://www.runoob.com/python/python-socket.html      
socket.connect()	主动初始化TCP服务器连接。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
````
import socket
# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',6999)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn,addr)
    while True:
        try:
            data = conn.recv(1024)  #接收数据
            print('recive:',data.decode()) #打印接收到的数据
            conn.send(data.upper()) #然后再发送数据
        except ConnectionResetError as e:
            print('关闭了正在占线的链接！')
            break
    conn.close()
````


**9.xpath教程**  
https://www.w3school.com.cn/xpath/index.asp
https://blog.csdn.net/mockingbirds/article/details/71022785
https://blog.csdn.net/myli_binbin/article/details/93890406