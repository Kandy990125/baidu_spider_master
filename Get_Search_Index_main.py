from get_index import BaiduIndex
from SQL_main import insert_sql
def Search_main(time):
    name_list1 = ['蔡徐坤','陈立农','范丞丞', '黄明昊','林彦俊']
    baidu_index = BaiduIndex(name_list1, time, time)
    for name in name_list1:
        all = baidu_index(name,"all")
        pc = baidu_index(name,"pc")
        wise = baidu_index(name,"wise")
        date = all[0]["date"]
        all_index = int(all[0]["index"])
        pc_index = int(pc[0]["index"])
        wise_index = int(wise[0]["index"])
        insert_sql('BaiduSearchIndex', name, date,all_index ,pc_index,wise_index)
    name_list2 = ['朱正廷','王子异','小鬼','尤长靖']
    baidu_index2 = BaiduIndex(name_list2, time, time)
    for name in name_list2:
        all = baidu_index2(name, "all")
        pc = baidu_index2(name, "pc")
        wise = baidu_index2(name, "wise")
        date = all[0]["date"]
        all_index = int(all[0]["index"])
        pc_index = int(pc[0]["index"])
        wise_index = int(wise[0]["index"])
        insert_sql('BaiduSearchIndex', name, date, all_index, pc_index, wise_index)