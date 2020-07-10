#-*- coding: utf-8 -*-
import sys
import socket
import subprocess
import argparse
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import json
import time

# ping
def ping(ip):
    result = []
    for i in ip:
        try:
            command = "ping %s" % (i)
            res = subprocess.run(command)
            if res.returncode == 0:
                result.append(i)
        except Exception as e:
            print(e)
    return result

# tcp
def tcp(ip):
    result = {}
    cot = 0
    for i in ip:
        result[i] = []
        li=[5000,3306]
        # for port in range(0, 1024):
        for j in range(2):
            try:
                sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sk.settimeout(2)
                res = sk.connect_ex((i, li[j]))
                print(res)
                if res == 0:
                    result[i].append(li[j])
                sk.close()
            except Exception as e:
                print(e)
    return result


# 多进程
def proc():
    with ProcessPoolExecutor(args.n) as executor:
        start_time = time.clock()
        if args.f == 'ping':
            future = executor.submit(ping, ip)
        else:
            future = executor.submit(tcp, ip)
        end_time = time.clock()
    print(future.result())
    save(future)


# 多线程
def thread():
    with ThreadPoolExecutor(args.n) as executor:
        if args.f == 'ping':
            future = executor.submit(ping, ip)
        else:
            future = executor.submit(tcp, ip)
    print(future.result())
    save(future)

# 将扫描结果保存成json文件
def save(future):
    if args.w != 0:
        with open(args.w, 'w') as  f:
            json.dump(future.result(), f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=4, help='并发数量')
    parser.add_argument('-f', choices=['ping', 'tcp'], default='tcp', help='测试类型')
    parser.add_argument('-ip', type=str, required=True, help='ip')
    parser.add_argument('-w', type=str, default=None, help='扫描结果进行保存')
    parser.add_argument('-m', choices=['proc', 'thread'], default='proc', help='选择多线程或者多进程', required=False)
    parser.add_argument('-v', action='count', default=0, help='打印扫描器运行耗时')
    args = parser.parse_args()
    ip = args.ip.split('-')

    # 选择多进程还是多线程
    start_time = time.clock()
    if args.m == 'proc':
        proc()
    else:
        thread()
    end_time = time.clock()

    # 打印耗时
    if args.v != 0:
        time_cost = end_time - start_time
        print (str(end_time)+" seconds")


