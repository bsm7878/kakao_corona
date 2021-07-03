import requests
from bs4 import BeautifulSoup
from datetime import datetime



def article_check():
    req = requests.get('https://www.kdca.go.kr/board/board.es?mid=a20501000000&bid=0015')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')


    article_title = soup.select_one(
        '#content_detail > .tstyle_list > #listView > ul:nth-of-type(1) > .title2 > a'
    )

    # title, href 가져오기
    href = 'https://www.cdc.go.kr/' + article_title['href']
    title = article_title['title']

    # title이 오늘 맞는지 확인
    today_month = str(datetime.today().month)
    today_day = str(datetime.today().day)
    check_text = '코로나바이러스감염증-19 국내 발생 현황(' + today_month + '.' + today_day + '., 0시 기준)'

    if check_text == title:
        req = requests.get(href)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        day_text = str(soup.select_one(
            '.tb_contents > p:nth-of-type(3)'
        ))

        # 국내 확진자
        today_in_total = int(day_text.split(',')[1].split(' ')[-1][:-1])
        # 해외 확진자
        today_out_total = int(day_text.split(',')[2].split(' ')[3][:-2])

        # 지역별 확진자
        today_area = []
        for j in range(3, 20):
            area_text = str(soup.select_one(
                f'.tb_contents > table:nth-of-type(1) > tbody > tr:nth-of-type(1) > td:nth-of-type({j})'
            ).text).strip()

            today_area.append(area_text)

        today_people = []
        for j in range(3, 20):
            area_text = str(soup.select_one(
                f'.tb_contents > table:nth-of-type(1) > tbody > tr:nth-of-type(2) > td:nth-of-type({j})'
            ).text).strip()

            today_people.append(area_text)

        today_area_people = {}
        for i in range(0, 17):
            today_area_people[today_area[i]] = today_people[i]

        return ('True', today_in_total, today_out_total, today_area_people)

    else:
        return ('False')


if __name__ == "__main__":
    print(article_check())