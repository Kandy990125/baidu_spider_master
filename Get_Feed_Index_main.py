from get_feed_index import BaiduIndex
from SQL_main import insert_sql2
def Feed_main(time):
    name_list1 = ['蔡徐坤','陈立农','范丞丞', '黄明昊','林彦俊']
    baidu_index = BaiduIndex(name_list1, time, time)
    for item in baidu_index.result:
        word = item["word"]
        date = item["date"]
        index = item["index"]
        insert_sql2("BaiduFeedIndex", word, date, index)

    name_list2 = ['朱正廷', '王子异', '小鬼', '尤长靖']
    baidu_index2 = BaiduIndex(name_list2, time, time)
    for item in baidu_index2.result:
        word = item["word"]
        date = item["date"]
        index = item["index"]
        insert_sql2("BaiduFeedIndex", word, date, index)
