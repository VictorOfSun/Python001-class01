# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class SpidersPipeline:
    def process_item(self, item, spider):

        #把dict转换成dataframe，要先转成list
        movie=[item]

        print(1)
        print(movie)

        movie1 = pd.DataFrame(data=[item])
        #mode='a'是代表追加数据，不覆盖
        movie1.to_csv('./movie1.csv', encoding='utf8', index=False, mode='a', header=False)

        return item
