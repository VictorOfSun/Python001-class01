import requests
from lxml import etree
import conn
from time import sleep
from concurrent.futures import ThreadPoolExecutor

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '',
    'db' : 'test'
}

sqls = "insert into company(name,salary,city) values (%s,%s,%s)"

# Python 使用def定义函数，myurl是函数的参数
def get_url(url,city,result):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

    cookie = 'user_trace_token=20200709114814-1314b974-88e1-4ee3-b030-3ed05284bbfc; _ga=GA1.2.115885258.1594266495; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594266495; LGUID=20200709114815-0578ec6a-9eb6-4c88-944f-78a2e20d141e; LGSID=20200709144840-b58ea673-dd38-4a74-bc30-c94cb5d02507; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.000000Krmlmkm2PiaUqEqMXWHqVyRTbFjGIN4sa5kDzi6Bd9NO53uy2MzxjGXOrLejyLEnwkJtCR%5F5qMsqSmmh7lGxKrAbd9bpgvSK-h%5FSY1hwZaO-f-kDTV9z6K5EtitD2t2-d8n-CJIXFN7t9xZaJAG9rdK6Xb-zcscBudENLCI%5FbZZHbhdPXKBaOagaby2Ym44rYOL-e%5FiUyUbCl5lKlklJOx.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4VnL30ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TaV8UHPS0KzmLmqnfKdThkxpyfqnHRkrjb1njm1PsKVINqGujYknWRYrj6kPfKVgv-b5HDsPWm3nHDz0AdYTAkxpyfqnHDdn1f0TZuxpyfqn0KWThnqnWDkPjm%26ck%3D4251.2.90.277.171.266.200.213%26dt%3D1594266490%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26tpl%3Dtpl%5F11534%5F22836%5F18980%26l%3D1518930637%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%25258B%252589%2525E5%25258B%2525BE%21%2526linkType%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; _gid=GA1.2.167287.1594277341; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221733255a7966cd-0d77076d35013f-4353760-1327104-1733255a797783%22%2C%22%24device_id%22%3A%221733255a7966cd-0d77076d35013f-4353760-1327104-1733255a797783%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pcbt%22%7D%7D; gate_login_token=7ef25c5f5667105cb29a1c50b04bd9c5915fa7fd6a1ed968538c8b9812a4d47e; LG_HAS_LOGIN=1; _putrc=1B32283FD7FB5BD8123F89F2B170EADC; JSESSIONID=ABAAABAABAGABFAE2246A3D75CFDE8214A5195DB8670404; login=true; hasDeliver=0; privacyPolicyPopup=false; WEBTJ-ID=20200709145008-1733256ad88646-0dcaed4d328d58-4353760-1327104-1733256ad8a525; unick=%E6%9D%8E%E6%AC%A3; RECOMMEND_TIP=true; index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=09b1e7e4d49c476fb89f0596585a248f; X_HTTP_TOKEN=0d4a28da6fc6f08e34577249519afcb137d186475c; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594277543; LGRID=20200709145223-f8c43d70-a145-4946-bf10-d5f056a514e3'

    header = {'user-agent': user_agent,
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5,en-GB;q=0.4',
              'Cache-Control': 'no-cache',
              'Connection': 'keep-alive',
              'cookie': cookie}
    try:
        # downloader 下载器
        response = requests.get(url, headers=header)
        info = response.text
        parse(info,city,result)
    except Exception as e:
        print('下载出现异常', e)


def parse(html,city,result):
    html =etree.HTML(html)
    obj=html.xpath('//li[@class="con_list_item default_list"]')
    res=[]
    for x in obj:
        company=[x.xpath('@data-positionname'), x.xpath('@data-salary')]
        res.append(company)
        db = conn.ConnDB(dbInfo, sqls)
        data = (x.xpath('@data-positionname'),x.xpath('@data-salary'),city)

        # 插入数据库-异常处理
        try:
            db.run(data)
        except Exception as e:
            print(e)


def page_turn():
    urls={
        '北京':'https://www.lagou.com/beijing-zhaopin/Python/',
        '上海':'https://www.lagou.com/shanghai-zhaopin/Python/',
        '广州':'https://www.lagou.com/guangzhou-zhaopin/Python/',
        '深圳':'https://www.lagou.com/shenzhen-zhaopin/Python/'
    }
    result=[]
    for city in urls.keys():
        ur = tuple(urls[city]+str(page) for page in range(1,7))
        for page in ur:
            print(page)
            get_url(page,city,result)
            sleep(5)


def multithread():
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(page_turn)
        print(future.result())


if __name__ == '__main__':
    multithread()
