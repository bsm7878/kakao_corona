from datetime import datetime, timedelta
from total_people import total_today, total_yesterday
from area_people import area_today, area_yesterday
from diff_calc import diff_calc
import time

def get_text():
    # 어제 날짜
    yesterday = (datetime.today() - timedelta(1)).strftime("%Y %m %d").split((' '))
    yesterday_year = yesterday[0][2:]
    yesterday_month = yesterday[1]
    yesterday_day = yesterday[2]



    text = f"""[{yesterday_year}.{yesterday_month}.{yesterday_day} 코로나 현황]
종합 → {total_today()[0]}
국내 → {total_today()[1]}({diff_calc(total_today()[1],total_yesterday()[1])})
해외 → {total_today()[2]}({diff_calc(total_today()[2],total_yesterday()[2])})

[지역별]
서울 → {area_today()['서울']}({diff_calc(int(area_today()['서울']), int(area_yesterday()['서울']))})
경기 → {area_today()['경기']}({diff_calc(int(area_today()['경기']), int(area_yesterday()['경기']))})
인천 → {area_today()['인천']}({diff_calc(int(area_today()['인천']), int(area_yesterday()['인천']))})
부산 → {area_today()['부산']}({diff_calc(int(area_today()['부산']), int(area_yesterday()['부산']))})
대구 → {area_today()['대구']}({diff_calc(int(area_today()['대구']), int(area_yesterday()['대구']))})
광주 → {area_today()['광주']}({diff_calc(int(area_today()['광주']), int(area_yesterday()['광주']))})
울산 → {area_today()['울산']}({diff_calc(int(area_today()['울산']), int(area_yesterday()['울산']))})
대전 → {area_today()['대전']}({diff_calc(int(area_today()['대전']), int(area_yesterday()['대전']))})
세종 → {area_today()['세종']}({diff_calc(int(area_today()['세종']), int(area_yesterday()['세종']))})
강원 → {area_today()['강원']}({diff_calc(int(area_today()['강원']), int(area_yesterday()['강원']))})
충남 → {area_today()['충남']}({diff_calc(int(area_today()['충남']), int(area_yesterday()['충남']))})
충북 → {area_today()['충북']}({diff_calc(int(area_today()['충북']), int(area_yesterday()['충북']))})
경남 → {area_today()['경남']}({diff_calc(int(area_today()['경남']), int(area_yesterday()['경남']))})
경북 → {area_today()['경북']}({diff_calc(int(area_today()['경북']), int(area_yesterday()['경북']))})
전남 → {area_today()['전남']}({diff_calc(int(area_today()['전남']), int(area_yesterday()['전남']))})
전북 → {area_today()['전북']}({diff_calc(int(area_today()['전북']), int(area_yesterday()['전북']))})
제주 → {area_today()['제주']}({diff_calc(int(area_today()['제주']), int(area_yesterday()['제주']))})
검역 → {area_today()['검역']}({diff_calc(int(area_today()['검역']), int(area_yesterday()['검역']))})
"""

    return text





if __name__ == "__main__":
    print(get_text())