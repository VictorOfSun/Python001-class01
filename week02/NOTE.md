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

3.随机代理IP

middlewares.py文件中写下方的类，继承HttpProxyMiddleware

```
class RandomHttpProxyMiddleware(HttpProxyMiddleware):
```