from datetime import datetime, timedelta
import requests
import xmltodict
import json


def api():
    secret_key = '1EoCXIYMTPGPGVCZUbr6ca55nv8OGYwG2we7r7ABSvxit5vqKnqYiw9WD3PuD2IdteK8ieAAtgLEmmWU6yQvwA%3D%3D'

    today = datetime.today().strftime("%Y%m%d")
    yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")

    # today = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
    # yesterday = (datetime.today() - timedelta(2)).strftime("%Y%m%d")

    URL = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={secret_key}&pageNo=1&numOfRows=10&startCreateDt={yesterday}&endCreateDt={today}'
    response = requests.get(URL)
    dict_data = xmltodict.parse(response.text)
    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)

    return dict_data



if __name__ == "__main__":
    print(api())