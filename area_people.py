from api import api
from article import article_check





def area_today():
    if article_check()[0] == 'True':
        return article_check()[3]
    else:
        api_data = api()
        today_area_people = {}
        item = api_data['response']['body']['items']['item']
        for i in range(18):
            today_area_people[item[i]['gubun']] = item[i]['incDec']

        return today_area_people


def area_yesterday():
    if article_check()[0] == 'True':
        api_data = api()
        yesterday_area_people = {}
        item = api_data['response']['body']['items']['item']
        for i in range(18):
            yesterday_area_people[item[i]['gubun']] = item[i]['incDec']

        return yesterday_area_people
    else:
        api_data = api()
        yesterday_area_people = {}
        item = api_data['response']['body']['items']['item']
        for i in range(19, 37):
            yesterday_area_people[item[i]['gubun']] = item[i]['incDec']

        return yesterday_area_people


if __name__ == "__main__":
    pass