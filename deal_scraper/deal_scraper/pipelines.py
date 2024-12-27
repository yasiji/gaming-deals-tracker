# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class DealScraperPipeline:
    def open_spider(self, spider):
        self.conn = psycopg2.connect(
            dbname="gaming_deals",
            user="postgres",
            password="admin",
            host="localhost"
        )
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute(
            """
            INSERT INTO deals (product_name, price, link, retailer)
            VALUES (%s, %s, %s, %s)
            """,
            (item['product_name'], item['price'], item['link'], 'Amazon')
        )
        self.conn.commit()
        return item

