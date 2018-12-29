from Get_Feed_Index_main import Feed_main
from Get_Search_Index_main import Search_main
from datetime import datetime, date, timedelta
import time
if __name__ =="__main__":
    while True:
        t = date.today()
        dt = datetime.strptime(str(t), '%Y-%m-%d')
        yesterday = dt + timedelta(days=-1)
        yesterday = str(yesterday).split(' ')[0]
        print(yesterday)
        hour = int(datetime.now().strftime('%H'))
        minute = int(datetime.now().strftime('%M'))
        if minute == 0 and hour == 23 :
            Search_main(yesterday)
            Feed_main(yesterday)
        time.sleep(60)