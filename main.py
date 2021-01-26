from auto import auto
import schedule
import time
from datetime import datetime
from api import api

if __name__ == "__main__":

    def send_text():

        while True:
            try:
                api_data = api()
                api_data['response']['body']['items']['item'][37]
                break
            except IndexError:
                time.sleep(60)

        auto()



    # schedule.every().day.at("10:01").do(send_text)
    send_text()

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)