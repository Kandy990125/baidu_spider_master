def get_cookies():
    COOKIES = []
    with open("cookies1.txt", 'r', encoding='utf-8') as f:
        list = f.readlines()
        for item in list:
            item_list = item.split('----')
            COOKIES.append(item_list[2][:-1])
        return COOKIES