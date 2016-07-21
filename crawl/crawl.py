#-*- coding:UTF-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup

url = "http://xxx.yyy.com/zzzz?"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
host = "search.daum.net"
cookie = ""
q = ""

headers = {'User-Agent': user_agent, 'Host' : host, 'Cookie' : cookie}

for page in range(1,100):
    data = urllib.urlencode({'key':'value'})
    req = urllib2.Request(url + data)
    req.add_header( 'User-Agent', user_agent)
    req.add_header( 'Host', host)
    req.add_header( 'Cookie', cookie)

    response = urllib2.urlopen(req)
    the_page = response.read()

    soup = BeautifulSoup(the_page,"html.parser")
    links = soup.find_all('a')
