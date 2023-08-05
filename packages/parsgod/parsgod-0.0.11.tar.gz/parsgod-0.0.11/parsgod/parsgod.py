from collections import defaultdict
from difflib import SequenceMatcher
import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup


def find_link_class(url):
    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    def flatten(lst):
        for item in lst:
            if isinstance(item, (list, tuple)):
                yield from flatten(item)
            else:
                yield item

    def most_common(lst, n):
        counter = defaultdict(int)
        for item in flatten(lst):
            counter[item] += 1
        return sorted(counter.items(), key=lambda x: -x[1])[:n]

    sp_l = ['product__link',
            'element-cover-link js-element-name',
            'j6z tile-hover-target',
            'element-cover-link js-element-name',
            'cl-item-link js-cl-item-link js-cl-item-root-link',
            'product-card__link j-card-link j-open-full-product-card',
            'product-card-photo__link reset-link',
            'digi-product__label',
            'seredina']

    data = {}
    data2 = {}
    d = webdriver.Edge()
    d.get(url)
    time.sleep(3)
    d.execute_script("window.scrollTo(0, 10000)")
    response = d.page_source
    soup = BeautifulSoup(response, "lxml")
    sp = soup.find_all('a')
    sp2 = []
    sp3 = []
    for s in sp:
        sp2.append(s.get('class'))

    for i in most_common(sp2, 10):
        if i[0] != None:
            sp3.append(str(i[0]))

    for el in sp3:
        i = 0
        for h in sp_l:
            i += similar(el, h)
            data[el] = i
            data2[i] = el

    sp4 = []
    for keys in data:
        sp4.append(data[keys])

    sp4.sort()
    sp4.reverse()
    return data2[sp4[0]]

def find_price_class(url, class_link):
    d = webdriver.Edge()
    d.get(url)
    time.sleep(3)
    soup = BeautifulSoup(d.page_source, 'lxml')
    link = soup.find('a', class_=class_link).get('href')
    sp = url.split('/')
    base_url = sp[0] + '//' + sp[1] + sp[2]
    if base_url not in link:
        link = base_url + link
    dr = webdriver.Edge()
    dr.get(link)
    time.sleep(3)
    soup2 = BeautifulSoup(dr.page_source, 'lxml')
    sp2 = soup2.find_all()
    for s in sp2:
        if '₽' in s.text and len(s.text) < 25:
            print(s.text)
            if '[' in str(s.get('class')):
                return str(' '.join(s.get('class'))) + ';' + str(s.name)
            else:
                return str(s.get('class')) + ';' + str(s.name)

    return '""'



def requests_code(url, headers, cookies, link_class, price_class, price_tag):
    with open('request_parser.py', 'w', encoding='utf-8') as file:
        file.write('import requests\n'
                   'from bs4 import BeautifulSoup\n'
                   'import lxml\n'
                   'import csv\n'
                   'from itertools import zip_longest\n'
                   '\n'
                   f'def main(url, headers, cookies):\n'
                   f'   response = requests.get(url=url, headers=headers, cookies=cookies)\n'
                   f'   soup = BeautifulSoup(response.text, "lxml")\n'
                   f'\n'
                   f'   links = soup.find_all("a", class_="{link_class}") #If necessary, replace the class\n'
                   f'   sp = url.split("/")\n'
                   f'   base_url = sp[0] + "//" + sp[1] + sp[2]\n'
                   f'   for link in links:\n'
                   f'       card_link = link.get("href")\n'
                   f'       if base_url not in card_link:\n'
                   f'           card_link = base_url + card_link\n'
                   f'       card_response = requests.get(url=card_link, headers=headers, cookies=cookies)\n'
                   f'       card_soup = BeautifulSoup(card_response.text, "lxml")\n'
                   f'       tag = card_soup.find("h1").text\n'
                   f'       price = card_soup.find("{price_tag}", class_="{price_class}").text\n'
                   f'       \n'
                   f'       tags = [tag]\n'
                   f'       prices = [price]\n'
                   f'       d = [tags, prices]\n'
                   f'       export_data = zip_longest(*d, fillvalue="")\n'
                   f'       with open("data.csv", "a", encoding="utf-8", newline="") as file:\n'
                   f'           wr = csv.writer(file, delimiter=";")\n'
                   f'           wr.writerows(export_data)\n'
                   f'\n'
                   f'\n'
                   f'if __name__ == "__main__":\n'
                   f'   url = "{url}"\n'
                   f'   headers = "{headers}"\n'
                   f'   cookies = "{cookies}"\n'
                   f'   main(url, headers, cookies)')

def async_requests_code(url, headers, cookies, link_class, price_class, price_tag):
    with open('async_request_parser.py', 'w', encoding='utf-8') as file:
        file.write('import aiohttp\n'
                   'from bs4 import BeautifulSoup\n'
                   'import asyncio\n'
                   'import csv\n'
                   'from itertools import zip_longest\n'
                   '\n'
                   'async def fetch(session, url, headers, cookies):\n'
                   '    async with session.get(url, headers=headers, cookies=cookies) as response:\n'
                   '        return await response.text()\n'
                   '\n'
                   f'async def main(url, headers, cookies):\n'
                   '    async with aiohttp.ClientSession() as session:\n'
                   '        response = await fetch(session, url, headers, cookies)\n'
                   '        soup = BeautifulSoup(response, "lxml")\n'
                   '\n'
                   f'       links = soup.find_all("a", class_="{link_class}") #If necessary, replace the class\n'
                   f'       sp = url.split("/")\n'
                   f'       base_url = sp[0] + "//" + sp[1] + sp[2]\n'
                   f'       for link in links:\n'
                   f'           card_link = link.get("href")\n'
                   f'           if base_url not in card_link:\n'
                   f'               card_link = base_url + card_link\n'
                   '            card_response = await fetch(session, card_link, headers, cookies)\n'
                   '            card_soup = BeautifulSoup(card_response, "lxml")\n'
                   '\n'
                   '            tag = card_soup.find("h1").text\n'
                   f'            price = card_soup.find("{price_tag}", class_="{price_class}").text\n'
                   '\n'
                   '            tags = [tag]\n'
                   '            prices = [price]\n'
                   '            d = [tags, prices]\n'
                   '            export_data = zip_longest(*d, fillvalue="")\n'
                   '            with open("data.csv", "a", encoding="utf-8", newline="") as file:\n'
                   '                wr = csv.writer(file, delimiter=";")\n'
                   '                wr.writerows(export_data)\n'
                   '\n'
                   '\n'
                   'if __name__ == "__main__":\n'
                   f'    url = "{url}"\n'
                   f'    headers = "{headers}"\n'
                   f'    cookies = "{cookies}"\n'
                   '    asyncio.run(main(url, headers, cookies))\n')

def selenium_code_edge(url, pause_time, link_class, price_class, price_tag):
    with open('selenium_parser.py', 'w', encoding='utf-8') as file:
        file.write(f"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import lxml
from itertools import zip_longest

def main(url, pause_time):
    driver = webdriver.Edge()
    driver.get(url)
    time.sleep(pause_time)
    soup = BeautifulSoup(driver.page_source, "lxml")
    links = soup.find_all("a", class_="{link_class}") #If necessary, replace the class
    sp = url.split("/")
    base_url = sp[0] + "//" + sp[1] + sp[2]
    for link in links:
        card_link = link.get("href")
        if base_url not in card_link:
            card_link = base_url + card_link
        driver1 = webdriver.Edge()
        driver1.get(card_link)
        time.sleep(pause_time)
        card_soup = BeautifulSoup(driver1.page_source, "html.parser")

        tag = card_soup.find("h1").text
        price = card_soup.find("{price_tag}", class_="{price_class}").text

        tags = [tag]
        prices = [price]
        d = [tags, prices]
        export_data = zip_longest(*d, fillvalue="")
        with open("data.csv", "a", encoding="utf-8", newline="") as file:
            wr = csv.writer(file, delimiter=";")
            wr.writerows(export_data)

    driver.quit()

if __name__ == "__main__":
    url = "{url}"
    pause_time = {pause_time}
    main(url, pause_time)
""")

def response(url, headers, cookies):
    response_code = requests.get(url, headers=headers, cookies=cookies)
    if response_code.status_code == 200:
        return True
    else:
        return False



def pgmode(url='https://example.ru', headers='', cookies='', mode='standart', pause_time=1):
    link_class = find_link_class(url=url)
    price_class = find_price_class(url=url, class_link=link_class).split(';')
    price_tag = price_class[-1]
    price_class = price_class[0]
    if response(url=url, headers=headers, cookies=cookies) and mode == 'standart':
        requests_code(url=url, headers=headers, cookies=cookies, link_class=link_class, price_class=price_class, price_tag=price_tag)
    elif response(url=url, headers=headers, cookies=cookies) and mode == 'asyncio':
        async_requests_code(url=url, headers=headers, cookies=cookies, link_class=link_class, price_class=price_class, price_tag=price_tag)
    else:
        selenium_code_edge(url=url, pause_time=pause_time, link_class=link_class, price_class=price_class, price_tag=price_tag)


