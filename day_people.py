from datetime import datetime, timedelta
import requests
import xmltodict
import json


def get_day_people():
    secret_key = '1EoCXIYMTPGPGVCZUbr6ca55nv8OGYwG2we7r7ABSvxit5vqKnqYiw9WD3PuD2IdteK8ieAAtgLEmmWU6yQvwA%3D%3D'

    today = datetime.today().strftime("%Y%m%d")
    yesterday = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
    before_yesterday = (datetime.today() - timedelta(2)).strftime("%Y%m%d")

    URL = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={secret_key}&pageNo=1&numOfRows=10&startCreateDt={yesterday}&endCreateDt={today}'
    response = requests.get(URL)
    dict_data = xmltodict.parse(response.text)
    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)



    yesterday_si_do_people = {}
    ago_yesterday_si_do_people = {}
    for i in range(18):
        yesterday_si_do_people[dict_data['response']['body']['items']['item'][i]['gubun']] = dict_data['response']['body']['items']['item'][i]['incDec']

    for i in range(19,37):
        ago_yesterday_si_do_people[dict_data['response']['body']['items']['item'][i]['gubun']] = dict_data['response']['body']['items']['item'][i]['incDec']

    return