from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0',
}
response = requests.get('https://www.reddit.com/', headers = headers).text
soup = BeautifulSoup(response,'html.parser')
tag_list = soup.select('div[class*=sitetable] a[class*=title]')
for idx, tag in enumerate(tag_list,1):
    print(idx, tag)