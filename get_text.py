from datetime import datetime, timedelta
from total_people import total_today, total_yesterday
from area_people import area_today, area_yesterday
from diff_calc import diff_calc

def get_text():
    # 어제 날짜
    yesterday = (datetime.today() - timedelta(1)).strftime("%Y %m %d").split((' '))
    yesterday_year = yesterday[0][2:]
    yesterday_month = yesterday[1]
    yesterday_day = yesterday[2]

    total_today_data = total_today()
    total_yesterday_Data = total_yesterday()

    area_today_data = area_today()
    area_yesterday_data = area_yesterday()


    text = f"""[{yesterday_year}.{yesterday_month}.{yesterday_day} 코로나 현황]
종합 → {total_today_data[0]}
국내 → {total_today_data[1]}({diff_calc(total_today_data[1],total_yesterday_Data[1])})
해외 → {total_today_data[2]}({diff_calc(total_today_data[2],total_yesterday_Data[2])})

[지역별]
서울 → {area_today_data['서울']}({diff_calc(int(area_today_data['서울']), int(area_yesterday_data['서울']))})
경기 → {area_today_data['경기']}({diff_calc(int(area_today_data['경기']), int(area_yesterday_data['경기']))})
인천 → {area_today_data['인천']}({diff_calc(int(area_today_data['인천']), int(area_yesterday_data['인천']))})
부산 → {area_today_data['부산']}({diff_calc(int(area_today_data['부산']), int(area_yesterday_data['부산']))})
대구 → {area_today_data['대구']}({diff_calc(int(area_today_data['대구']), int(area_yesterday_data['대구']))})
광주 → {area_today_data['광주']}({diff_calc(int(area_today_data['광주']), int(area_yesterday_data['광주']))})
울산 → {area_today_data['울산']}({diff_calc(int(area_today_data['울산']), int(area_yesterday_data['울산']))})
대전 → {area_today_data['대전']}({diff_calc(int(area_today_data['대전']), int(area_yesterday_data['대전']))})
세종 → {area_today_data['세종']}({diff_calc(int(area_today_data['세종']), int(area_yesterday_data['세종']))})
강원 → {area_today_data['강원']}({diff_calc(int(area_today_data['강원']), int(area_yesterday_data['강원']))})
충남 → {area_today_data['충남']}({diff_calc(int(area_today_data['충남']), int(area_yesterday_data['충남']))})
충북 → {area_today_data['충북']}({diff_calc(int(area_today_data['충북']), int(area_yesterday_data['충북']))})
경남 → {area_today_data['경남']}({diff_calc(int(area_today_data['경남']), int(area_yesterday_data['경남']))})
경북 → {area_today_data['경북']}({diff_calc(int(area_today_data['경북']), int(area_yesterday_data['경북']))})
전남 → {area_today_data['전남']}({diff_calc(int(area_today_data['전남']), int(area_yesterday_data['전남']))})
전북 → {area_today_data['전북']}({diff_calc(int(area_today_data['전북']), int(area_yesterday_data['전북']))})
제주 → {area_today_data['제주']}({diff_calc(int(area_today_data['제주']), int(area_yesterday_data['제주']))})
검역 → {area_today()['검역']}({diff_calc(int(area_today()['검역']), int(area_yesterday()['검역']))})

* (+/-): 전날 대비 확진자 증감 표시
** 주말(토,일)은 발송되지 않습니다
"""

    return text





if __name__ == "__main__":
    print(get_text())