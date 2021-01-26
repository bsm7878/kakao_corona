from api import api





def total_today():
    api_data = api()
    today_total_data = api_data['response']['body']['items']['item'][18]
    today_total = int(today_total_data['incDec'])
    today_in_total = int(today_total_data['localOccCnt'])
    today_out_total = int(today_total_data['overFlowCnt'])

    return (today_total, today_in_total, today_out_total)


def total_yesterday():
    api_data = api()
    yesterday_total_data = api_data['response']['body']['items']['item'][37]
    yesterday_total = int(yesterday_total_data['incDec'])
    yesterday_in_total = int(yesterday_total_data['localOccCnt'])
    yesterday_out_total = int(yesterday_total_data['overFlowCnt'])

    return (yesterday_total, yesterday_in_total, yesterday_out_total)



if __name__ == "__main__":
    print(total_today())