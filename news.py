import requests
from bs4 import BeautifulSoup


def business_news(text):
    fixed_url = 'https://economictimes.indiatimes.com/news/international/business'
    headlines_1 = ""
    news_headlines_list = []
    r = requests.get(fixed_url)
    data = r.text
    count = 0
    soup = BeautifulSoup(data, "html.parser")
    for news_headlines in soup.findAll('div', class_='eachStory'):
        news_headlines_list.append(news_headlines.find('h3').get_text())
    for key in news_headlines_list:
        count +=1
        if count<5:
            headlines_1 = headlines_1 + 'Headline : ' + key + '. Next '
        else:
            break
    return headlines_1[:-5]

def agriculture_news(text):
    fixed_url = 'https://economictimes.indiatimes.com/news/economy/agriculture'
    headlines_1 = ""
    news_headlines_list = []
    r = requests.get(fixed_url)
    data = r.text
    count = 0
    soup = BeautifulSoup(data, "html.parser")
    for news_headlines in soup.findAll('div', class_='eachStory'):
        news_headlines_list.append(news_headlines.find('h3').get_text())
    for key in news_headlines_list:
        count +=1
        if count<5:
            headlines_1 = headlines_1 + 'Headline : ' + key + '. Next '
        else:
            break
    return headlines_1[:-5]


def finance_news(text):
    fixed_url = 'https://economictimes.indiatimes.com/news/economy/finance'
    headlines_1 = ""
    news_headlines_list = []
    r = requests.get(fixed_url)
    data = r.text
    count = 0
    soup = BeautifulSoup(data, "html.parser")
    for news_headlines in soup.findAll('div', class_='eachStory'):
        news_headlines_list.append(news_headlines.find('h3').get_text())
    for key in news_headlines_list:
        count +=1
        if count<5:
            headlines_1 = headlines_1 + 'Headline : ' + key + '. Next '
        else:
            break
    return headlines_1[:-5]


def political_news(text):
    fixed_url = 'https://economictimes.indiatimes.com/news/politics-nation'
    headlines_1 = ""
    news_headlines_list = []
    r = requests.get(fixed_url)
    data = r.text
    count = 0
    soup = BeautifulSoup(data, "html.parser")
    for news_headlines in soup.findAll('div', class_='botplData flt'):
        news_headlines_list.append(news_headlines.h3.get_text())
    for key in news_headlines_list:
        count +=1
        if count<5:
            headlines_1 = headlines_1 + 'Headline : ' + key + '. Next '
        else:
            break
    return headlines_1[:-5]

def world_news(text):
    fixed_url = 'https://economictimes.indiatimes.com/news/international/world-news'
    headlines_1 = ""
    news_headlines_list = []
    r = requests.get(fixed_url)
    data = r.text
    count = 0
    soup = BeautifulSoup(data, "html.parser")
    for news_headlines in soup.findAll('div', class_='eachStory'):
        news_headlines_list.append(news_headlines.find('h3').get_text())
    for key in news_headlines_list:
        count +=1
        if count<5:
            headlines_1 = headlines_1 + 'Headline : ' + key + '. Next '
        else:
            break
    return headlines_1[:-5]
