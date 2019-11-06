from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36'}
url = 'http://127.0.0.1:8080/spider/website.html'
resp = requests.get(url, headers=headers)
resp.encoding = 'gb2312'
#print(resp.text)

'''soup = BeautifulSoup(resp.text, 'html.parser')
p = soup.find_all('p', id='cp')
for i in p:
    a = p.find('a')
    href = a.get('href')
    text = a.get_text()
    print(href + '----' + text)
'''

soup = BeautifulSoup(resp.text, 'html.parser')
elm_p = soup.find_all('p')
#-------------------------
print(elm_p[1].text)
#-------------------------
for e in elm_p:
    print(e.text)
#-------------------------
elm_div = soup.find_all(name='div', id='div_poem')
print(elm_div[0].find(name='p'))
#-------------------------
elm_img = soup.find_all(name='img')
print(elm_img[0]['src'])
#-------------------------
elm_a = soup.find_all(name='a')
print(elm_a[0].get('href'))
