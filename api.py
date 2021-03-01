import os
import requests
import xmltodict
import json
from datetime import datetime, timedelta


api_key = os.environ['API_KEY']

def api():
    # 오늘 날짜 불러오기
    today = datetime.today().strftime("%Y%m%d")
    yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")

    # 어제 날짜 불러오기
    # today = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
    # yesterday = (datetime.today() - timedelta(2)).strftime("%Y%m%d")

    URL = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={api_key}&pageNo=1&numOfRows=10&startCreateDt={yesterday}&endCreateDt={today}'
    response = requests.get(URL)
    dict_data = xmltodict.parse(response.text)
    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)

    return dict_data



if __name__ == "__main__":
    print(api())