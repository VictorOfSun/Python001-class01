1. 如果被反爬的话，可以加入cookie即可解决，cookie有时候用久了就不起效果了，就换一下就好了
2. 字符串strip()方法，用于移除字符串头尾指定的字符(默认为空格或换行符)或字符序列
3. pandas的to_csv的encoding，windows需要使用gbk字符集
4. scrapy中要使用pipeline的话，需要将setting.py文件当中的ITEM_PIPELINES打开
5. 当想查询的div下有多个相同的标签时，想找指定的某i个时，xpath可以写成[i]，如li[3]
6. xpath中：//代表前面可以放任意长的路径的，/的话一般出现在浏览器自动识别某个特定元素时候，代表最上层的某个元素，加上.以后变成./ .//是从当前的匹配位置继续往下找，两个.代表从你当前的上一级的位置继续往下找，就是找和当前平级的
7. xpath：@取属性，text()取内容
8. 刚开始checkout的时候，git不会允许你直接切换，因为你修改了暂存区的内容， 它会提醒你提交后再切换，这时候，你可以使用-f 强行切换
9. 使用cookie的方法https://blog.csdn.net/weixin_38706928/article/details/80376572
10. scrapy设置cookie https://blog.csdn.net/fuck487/article/details/84617194
11. 将dict转化为dataframehttps://blog.csdn.net/zx1245773445/article/details/89355562
12. pandas read_csv和to_csv参数详解https://blog.csdn.net/u010801439/article/details/80033341/
13. extract()方法https://blog.csdn.net/nzjdsds/article/details/77278400?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase
