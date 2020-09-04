1. scrapy项目修改名称

   ![image-20200901161622428](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200901161622428.png)

2. 实现自动翻页

   就是爬虫中 parse 解析的时候，可以提取分页相关的数据，代码写逻辑判断，有没有解析出来下一页，有的话 yield scrapy.Request 抓取下，就实现自动翻页了

3. 用pymysql去插入情感分析这个字段

   1）写个for循环，然后一条一条数据去update情感分析

   2）要么就单独用另一张表，直接把分析后的数据写入新表也行

4. 前十的商品是会变的，那我每次都要动态读出前一天前十的数据吗

   每次都爬排名靠前的10条数据，然后展示的时候只展示数据库里最后10条就行

5. 抓10个的方法

   用切片soda[:10]，不用计数

6. 商品和评论分别建立两个item类，逻辑清晰

7. 判断是商品item类还是评论item类

    isinstance(obj, cls)

   - object -- 实例对象。
   - classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
   
8. 根据不同的name去生成不同的路由

    https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial03/#removing-hardcoded-urls-in-templates

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

这个标签的工作方式是在 `polls.urls` 模块的 URL 定义中寻具有指定名字的条目。你可以回忆一下，具有名字 'detail' 的 URL 是在如下语句中定义的：

```python
...
# the 'name' value as called by the {% url %} template tag
path('<int:question_id>/', views.detail, name='detail'),
...
```

如果你想改变投票详情视图的 URL，比如想改成 `polls/specifics/12/` ，你不用在模板里修改任何东西（包括其它模板），只要在 `polls/urls.py` 里稍微修改一下就行：

```python
...
# added the word 'specifics'
path('specifics/<int:question_id>/', views.detail, name='detail'),
...
```

9. 写定时任务去每天抓取前十的话，就前十如果有些是相同产品，那评论内容要判重一下

   每插入一条都要去查找一下有没有

   要么就不管重复直接写表，用 pandas 清洗的时候去重也会慢，还有就是 scrapy 去重，但是要做持久化，比较麻烦

10. 判断pymysql的查询结果是否为空

    判断 cursor.fetchone() 是否有结果,有结果返回元组，没结果返回 None

11. 换了kombu这个文件夹来替换 async 关键字

    需要修改这些文件才能启动成功的，只替换尹老师给的目录是不够的

    ![image-20200901175811339](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200901175811339.png)

    把 /site-packages/celery/worker/ 目录下的这几个文件中的 async 关键字修改后就能成功运行了

12. celery启动生产者加上 -l info 参数就会打印日志

13. 重启celery需要删除以下文件后再重启才可以

    ![image-20200901180022479](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200901180022479.png)

14. 如何同时执行两个命令

    ```python
    # coding: UTF-8
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    import subprocess
    import os
    import commands
    
    #os.system('cmd1 && cmd2')
    cmd1 = "cd ../"
    cmd2 = "ls"
    cmd = cmd1 + " && " + cmd2
    
    #如下两种都可以运行
    subprocess.Popen(cmd, shell=True)
    subprocess.call(cmd,shell=True)
    ```

    也可以将多条shell写入.sh 文件.然后运行.sh文件

15. cd应该要从哪里开始呀，是从tasks.py还是Django开始呀

    1） 运行 task 的时候处在 django 项目根目录，然后根据相对路径 cd 到 scrapy 根目录

    2） 如果不能执行 scrapy cralw xxx 命令，还有一个办法，就是在 scrapy 项目根目录下创建一个 run.py 文件，里面写上 
    from scrapy import cmdline
    cmdline.execute(['scrapy', 'crawl', 'xxx'])
    这两行代码，这样就可以 cd 到 scrapy 目录然后 python run.py 就行了

    3） 要么用 os.path 拼接成绝对路径试试，先获取当前路径文件夹名称，然后拼接下再 cd

    ​	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

16. python获取当前文件所在目录和当前工作目录

    当前工作目录

    ```python
    import  os
    print(os.getcwd()) # 获取当前工作目录路径
    print(os.path.abspath('.')) # 获取当前工作目录路径
    ```

    当前文件路径

    ```python
    import os
    current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录
    weight_path = os.path.join(current_work_dir, weight_path)  # 再加上它的相对路径，这样可以动态生成绝对路径
    ```

17. get传多个参数

    ?page=xxx&res=yyy

    第一个是问号，后面是 &

