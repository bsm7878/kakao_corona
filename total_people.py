from api import api
from article import article_check




def total_today():

    if article_check()[0] == 'True':
        today_data = article_check()
        return (today_data[1]+today_data[2], today_data[1], today_data[2])
    else:
        api_data = api()
        today_total_data = api_data['response']['body']['items']['item'][18]
        today_total = int(today_total_data['incDec'])
        today_in_total = int(today_total_data['localOccCnt'])
        today_out_total = int(today_total_data['overFlowCnt'])

        return (today_total, today_in_total, today_out_total)


def total_yesterday():
    if article_check()[0] == 'True':
        api_data = api()
        yesterday_total_data = api_data['response']['body']['items']['item'][18]
        yesterday_total = int(yesterday_total_data['incDec'])
        yesterday_in_total = int(yesterday_total_data['localOccCnt'])
        yesterday_out_total = int(yesterday_total_data['overFlowCnt'])

        return (yesterday_total, yesterday_in_total, yesterday_out_total)
    else:
        api_data = api()
        yesterday_total_data = api_data['response']['body']['items']['item'][37]
        yesterday_total = int(yesterday_total_data['incDec'])
        yesterday_in_total = int(yesterday_total_data['localOccCnt'])
        yesterday_out_total = int(yesterday_total_data['overFlowCnt'])

        return (yesterday_total, yesterday_in_total, yesterday_out_total)



if __name__ == "__main__":
    print(total_today())