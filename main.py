from auto import auto
import time
from api import api
from article import article_check


def send_text():
    while True:
        try:
            # 질병관리청 Text Check
            if article_check()[0] == 'True':
                print(1)
                break

            # 공공데이터포털 Api
            else:
                api_data = api()
                api_data['response']['body']['items']['item'][37]
                print(2)
                break
        except IndexError:
            print(3)
            time.sleep(60)

    auto()


if __name__ == "__main__":

    # 실행!
    send_text()

