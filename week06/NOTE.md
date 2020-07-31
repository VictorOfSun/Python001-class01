1. CSRF verification failed. Request aborted.）

   方法1：找到项目中的在settings配置文件中，把#'django.middleware.csrf.CsrfViewMiddleware’注释掉

   方法2：在html的代码中，凡是遇到post提交表单，都在表单的标签下加上{% csrf_token %}

2. bootstrap div 右对齐

    ```html
    <div class="col-lg-5  pull-right"></div>
    ```

3. bootstrap 表单

   ```html
   <form class="navbar-form navbar-left" role="search">
     <div class="form-group">
       <input type="text" class="form-control" placeholder="Search">
     </div>
     <button type="submit" class="btn btn-default">Submit</button>
   </form>
   ```

4. Django if 用法

   % if %}标签**不允许**在同一个标签中**同时使用 and 和 or**，因为逻辑上可能模糊的，例如，如下示例是错误的：

   ```html
   {% if athlete_list and coach_list or cheerleader_list %}1
   ```

   　　系统不支持用圆括号来组合比较操作。如果确实需要用到圆括号来组合表达逻辑式，考虑将它移到模板之外处理，然后以模板变量的形式传入结果，或者仅仅用嵌套的{% if %}标签替换，就像这样：

   ```html
   {% if athlete_list %}
       {% if coach_list or cheerleader_list %}
           We have athletes, and either coaches or cheerleaders!
       {% endif %}
   {% endif %}12345
   ```

   {% if %}标签**多次使用同一个逻辑操作符是没有问题的，但是不能把不同的操作符组合起来**。例如，这是合法的：

   ```html
   {% if athlete_list or coach_list or parent_list or teacher_list %}1
   ```

   在执行循环之前先检测列表的大小是一个通常的做法，当列表为空时输出一些特别的提示。

   ```html
   {% if athlete_list %}
       {% for athlete in athlete_list %}
           <p>{{ athlete.name }}</p>
       {% endfor %}
   {% else %}
       <p>There are no athletes. Only computer programmers.</p>
   {% endif %}1234567
   ```

   　　因为这种做法十分常见，所以“for”标签支持一个可选的“{% empty %}”分句，通过它可以定义当列表为空时的输出内容，下面的示例与前面的示例等价：

   ```html
   {% for athlete in athlete_list %}
       <p>{{ athlete.name }}</p>
   {% empty %}
       <p>There are no athletes. Only computer programmers.</p>
   {% endfor %}
   ```

5.  Django ORM操作

   #### queryset中支持链式操作

   book=Book.objects.all().order_by('-nid').first()

   **只要返回的是queryset对象就可以调用其他的方法,直到返回的是对象本身**

   #### 模糊查询常用的操作

   大于、大于等于:

   __gt 大于>
   __gte 大于等于>=

   Student.objects.filter(age__gt=10) // 查询年龄大于10岁的学生
   Student.objects.filter(age__gte=10) // 查询年龄大于等于10岁的学生

   特别注意：这里的下划线是双下划线，下面将介绍的也都是双下划线。
   小于、小于等于：

   __lt 小于<
   __lte 小于等于<=

   Student.objects.filter(age__lt=10) // 查询年龄小于10岁的学生
   Student.objects.filter(age__lte=10) // 查询年龄小于等于10岁的学生
   like:

   __exact 精确等于 like 'aaa'
   __iexact 精确等于 忽略大小写 ilike 'aaa'
   __contains 包含 like '%aaa%'
   __icontains 包含,忽略大小写 ilike '%aaa%'，但是对于sqlite来说，contains的作用效果等同于icontains。
   in:

   __in

   查询年龄在某一范围的学生
   Student.objects.filter(age__in=[10, 20, 30])
   is null / is not null：

   __isnull 判空

   Student.objects.filter(name__isnull=True) // 查询用户名为空的学生
   Student.objects.filter(name__isnull=False) // 查询用户名不为空的学生
   不等于/不包含于：

   Student.objects.filter().excute(age=10) // 查询年龄不为10的学生
   Student.objects.filter().excute(age__in=[10, 20]) // 查询年龄不在 [10, 20] 的学生
   其他常用模糊查询：

   __startswith 以…开头
   __istartswith 以…开头 忽略大小写
   __endswith 以…结尾
   __iendswith 以…结尾，忽略大小写
   __range 在…范围内
   __year 日期字段的年份
   __month 日期字段的月份
   __day 日期字段的日

   Book.objects.filter(create_time__year=2019, create_time__month=4).all()

   如果是mysql数据库settings里面修改  **USE_TZ = False**

   *多表连接查询：*

    class A(models.Model):
     name = models.CharField(u'名称')
    class B(models.Model):
     aa = models.ForeignKey(A)

   B.objects.filter(aa__name__contains='searchtitle')#查询B表中外键aa所对应的表中字段name包含searchtitle的B表对象。
   
   #### 查询API
   
   ```python
   all():         查询所有结果
       
   filter(``*``*``kwargs):    它包含了与所给筛选条件相匹配的对象
       
   get(``*``*``kwargs):     返回与所给筛选条件相匹配的对象，返回结果有且只有一个，
                 ``如果符合筛选条件的对象超过一个或者没有都会抛出错误。
           
   exclude(``*``*``kwargs):   它包含了与所给筛选条件不匹配的对象
       
   order_by(``*``field):    对查询结果排序 用法:order_by('**-**price')    DESC 降序
           
   reverse():       对查询结果反向排序
       
   count():        返回数据库中匹配查询(QuerySet)的对象数量。
       
   first():        返回第一条记录
       
   last():        返回最后一条记录
       
   exists():       如果QuerySet包含数据，就返回``True``，否则返回``False     **相当于limit 1(用途查询这个表中是否有值)**
       
   values(``*``field):    `用法:Book.objects.all.values('title','price') 返回值是<queryset[{'title':'aa','pirce':12},{}]
           
    values_list(``*``field):  用法:Book.objects.all.values_list('title','price') 返回值是<queryset[('aa',12),('bb',33)]
           
   distinct():      从返回结果中剔除重复纪录 用法:Book.objects.all.values('title','price').distinct()  
                 错误用法 Book.objects.all.distinct() 因为id不相同,其他相同,无法去重 
   ```
   
   6. django 
   
   ```html
      <form method="post" action="{% url 'check' %}">  
          {% csrf_token %}
          <input type="text" name="name" placeholder="your username"><br>
          <input type="password" name="pwd" placeholder="your password"><br>
          <input type="submit" value="提交"><br>
      </form>
   ```
   
   ```python
   def reg(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
    print(name,pwd)
    return render(request,'login.html')
   ```