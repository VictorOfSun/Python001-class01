from MyDjango.celery import app
import subprocess
import os
# redis-server.exe redis.windows.conf


@app.task()
def get_task():
    return 'test'


@app.task()
def get_task2():
    print(os.getcwd())
    return os.getcwd()


@app.task()
def get_scrapy_task():
    res = subprocess.call('cd ../1_scrapy/spiders && scrapy crawl phone',shell=True)
    if res == 0:
        return 'scrapy ok'
    else:
        return 'no ok'

