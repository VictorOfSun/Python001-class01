1. 查找元素

   ```python
   >>> x = [1,2,3]
   >>> 1 in x
   True
   
   >>> y = set()
   >>> y.add(1)
   >>> 1 in y
   True
   
   >>> z = {'a':1}
   >>> 1 in z
   False
   
   >>> 'a' in z
   True
   ```

2. setattr()

   **setattr()** 函数对应函数 [getattr()](https://www.runoob.com/python/python-func-getattr.html)，用于设置属性值，该属性不一定是存在的。

   ```python
   setattr(object, name, value)
   ```

- object -- 对象。

- name -- 字符串，对象属性。

- value -- 属性值。

  返回值：无。

  对已存在的属性进行赋值：

  ```python
  >>>class A(object):
  ...     bar = 1
  ... 
  >>> a = A()
  >>> getattr(a, 'bar')          # 获取属性 bar 值
  1
  >>> setattr(a, 'bar', 5)       # 设置属性 bar 值
  >>> a.bar
  5
  ```

  如果属性不存在会创建一个新的对象属性，并对属性赋值：

  ```python
  >>>class A():
  ...     name = "runoob"
  ... 
  >>> a = A()
  >>> setattr(a, "age", 28)
  >>> print(a.age)
  28
  >>>
  ```

3. hasattr

   **hasattr()** 函数用于判断对象是否包含对应的属性。

   ```python
   hasattr(object, name)
   ```

- object -- 对象。

- name -- 字符串，属性名。

  返回值：如果对象有该属性返回 True，否则返回 False。

   ```python
   # !/usr/bin/python
   # -*- coding: UTF-8 -*-
   
   class Coordinate:
       x = 10
       y = -5
       z = 0
   
   point1 = Coordinate()
   print(hasattr(point1, 'x'))
   print(hasattr(point1, 'y'))
   print(hasattr(point1, 'z'))
   print(hasattr(point1, 'no'))  # 没有该属性
   ```

4. getattr()

   **getattr()** 函数用于返回一个对象属性值。

   ```python
   getattr(object, name[, default])
   ```

- object -- 对象。

- name -- 字符串，对象属性。

- default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。

   返回值：返回对象属性值。

   ```python
   >>>class A(object):
   ...     bar = 1
   ... 
   >>> a = A()
   >>> getattr(a, 'bar')        # 获取属性 bar 值
   1
   >>> getattr(a, 'bar2')       # 属性 bar2 不存在，触发异常
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: 'A' object has no attribute 'bar2'
   >>> getattr(a, 'bar2', 3)    # 属性 bar2 不存在，但设置了默认值
   3
   >>>
   ```

   获取对象属性后返回值可直接使用：

   ```python
   >>> class A(object):        
   ...     def set(self, a, b):
   ...         x = a        
   ...         a = b        
   ...         b = x        
   ...         print a, b   
   ... 
   >>> a = A()                 
   >>> c = getattr(a, 'set')
   >>> c(a='1', b='2')
   2 1
   >>> 
   ```



上周事情比较多，笔记先空着，之后找时间补