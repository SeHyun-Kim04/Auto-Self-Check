import requests
import json


def main(URL, sc_name, st_name, st_brith, Scode):
    send_data = {
        "schulCode": Scode,
        "schulNm": sc_name,
        "pName": st_name,
        "frnoRidno": st_brith
    }

    res = requests.post(URL + '/stv_cvd_co00_012.do', data=send_data)
    data_set = json.loads(res.text)

    if res.status_code == 200:
        return data_set['resultSVO']['data']['qstnCrtfcNoEncpt']

    else:
        return -1
