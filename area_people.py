from api import api





def area_today():
    api_data = api()
    today_area_people = {}
    item = api_data['response']['body']['items']['item']
    for i in range(18):
        today_area_people[item[i]['gubun']] = item[i]['incDec']

    return today_area_people


def area_yesterday():
    api_data = api()
    yesterday_area_people = {}
    item = api_data['response']['body']['items']['item']
    for i in range(19, 37):
        yesterday_area_people[item[i]['gubun']] = item[i]['incDec']

    return yesterday_area_people


if __name__ == "__main__":
    pass