from config import get_cookies
from urllib.parse import urlencode
from collections import defaultdict
import datetime
import requests
import json
import random

headers = {
    'Host': 'index.baidu.com',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}


class BaiduIndex:
    """
        百度搜索指数
    """

    def __init__(self, keywords, start_date, end_date):
        self._keywords = keywords if isinstance(keywords, list) else keywords.split(',')
        self._time_range_list = self.get_time_range_list(start_date, end_date)
        self.result = []
        self.cookies_list = get_cookies()
        while True:
            i = random.randint(0, len(self.cookies_list) - 1)
            try:
                self.get_result(self.cookies_list[i])
                break
            except:
                with open("error_account.txt", "w") as f:
                    f.write(str(i) + " " + self.cookies_list[i] + "\n")
                self.cookies_list.pop(i)

    def get_result(self,cookies):
        """
        """
        for start_date, end_date in self._time_range_list:
            encrypt_datas, uniqid = self.get_encrypt_datas(start_date, end_date, cookies)
            # print(encrypt_datas)
            key = self.get_key(uniqid,cookies)
            # print(key)
            for encrypt_data in encrypt_datas:
                # print(encrypt_data)
                encrypt_data['data'] = int(self.decrypt_func(key, encrypt_data['data'])[0])
                # print(encrypt_data)
                self.format_data(encrypt_data)

    def get_encrypt_datas(self, start_date, end_date, cookies):
        """
        :start_date; str, 2018-10-01
        :end_date; str, 2018-10-01
        """
        request_args = {
            'word': ','.join(self._keywords),
            'startDate': start_date,
            'endDate': end_date,
            'area': 0,
        }
        url = 'http://index.baidu.com/api/FeedSearchApi/getFeedIndex?' + urlencode(request_args)
        html = self.http_get(url, cookies)

        datas = json.loads(html)
        uniqid = datas['data']['uniqid']
        encrypt_datas = []
        for single_data in datas['data']['index']:
            encrypt_datas.append(single_data)
        return (encrypt_datas, uniqid)

    def get_key(self, uniqid, cookies):
        """
        """
        url = 'http://index.baidu.com/Interface/api/ptbk?uniqid=%s' % uniqid
        # print(url)
        html = self.http_get(url,cookies)
        datas = json.loads(html)
        key = datas['data']
        # print(key)
        return key

    def format_data(self, data):
        keyword = str(data['key'])
        index = int(data['data'])
        start_date = data['startDate']
        # print(start_date[:-9])
        cur_date = datetime.datetime.strptime(start_date[:-9], '%Y-%m-%d')
        formated_data = {
            'word':keyword,
                'date': cur_date.strftime('%Y-%m-%d')
            }
        formated_data['index'] = index
        self.result.append(formated_data)

    @staticmethod
    def http_get(url, cookies):
        headers['Cookie'] = cookies
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None

    @staticmethod
    def get_time_range_list(startdate, enddate):
        """
        max 6 months
        """
        date_range_list = []
        startdate = datetime.datetime.strptime(startdate, '%Y-%m-%d')
        enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d')
        while 1:
            tempdate = startdate + datetime.timedelta(days=300)
            if tempdate > enddate:
                all_days = (enddate-startdate).days
                date_range_list.append((startdate, enddate))
                return date_range_list
            date_range_list.append((startdate, tempdate))
            startdate = tempdate + datetime.timedelta(days=1)

    @staticmethod
    def decrypt_func(key, data):
        """
        decrypt data
        """
        a = key
        i = data
        n = {}
        s = []
        for o in range(len(a)//2):
            n[a[o]] = a[len(a)//2 + o]
        for r in range(len(data)):
            s.append(n[i[r]])
        return ''.join(s).split(',')