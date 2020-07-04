1. 系统代理IP

   ```
   # export http_proxy='http://52.179.231.206:80'
   # setting 增加 scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
   # 通过 Request.meta['proxy'] 读取 http_proxy 环境变量加载代理
   ```

2. 防止CSRF检测

   ```
   'x-requested-with': 'XmlHttpRequest'
   ```

浏览器在请求网页的时候，会携带很多请求头，你得爬虫只写了 ua 和 referer，所以被对方识别到了，要尽量模拟浏览器的请求头，来进行伪装

「请求头中有很多信息，需要一个个加进去试吗？」
- - - - - - - - - - - - - - -
要模拟浏览器，就是说请求头越接近浏览器越好，所以你最好和浏览器都保持一样，都复制过来，明白了吗～

3. 随机代理IP

middlewares.py文件中写下方的类，继承HttpProxyMiddleware

```
class RandomHttpProxyMiddleware(HttpProxyMiddleware):
```

