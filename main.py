import requests
from lxml import etree
from bs4 import BeautifulSoup


def get_html(url, headers):
    result = requests.get(url, headers=headers)
    result.encoding = result.apparent_encoding
    return result.text


def get_pages(result):
    soup = BeautifulSoup(result, 'html.parser')
    all_topics = soup.find_all('tr')[1:]
    for topic in all_topics:
        topic_times = topic.find('td', class_='last')
        topic_title = topic.find('td', class_='keyword')
        topic_ranke = topic.find('td', class_='first')
        if topic_times != None and topic_title != None and topic_ranke != None:
            topic_ranke = topic.find('td', class_='first').get_text().replace('', '').replace('\n', '')
            topic_times = topic.find('td', class_='last').get_text().replace('', '').replace('\n', '')
            topic_title = topic.find('td', class_='keyword').get_text().replace('', '').replace('\n', '').replace(
                'search', '')
            print(topic_ranke, topic_title, topic_times)


def main():
    url = "http://top.baidu.com/buzz?b=1&fr=topindex"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    html = get_html(url, headers)
    get_pages(html)


if __name__ == '__main__':
    main()
