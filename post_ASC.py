import requests
import json


def main(URL, sc_name, st_name, CNE):
    URL += '/stv_cvd_co01_000.do';

    send_data = {
        "qstnCrtfcNoEncpt": CNE,
        "schulNm": sc_name,
        "stdntName": st_name,
        "rspns01": 1,
        "rspns02": 1,
        "rspns07": 0,
        "rspns08": 0,
        "rspns09": 0
    }
    res = requests.post(URL, data=send_data)
    data_set = json.loads(res.text)

    if res.status_code == 200:
        if data_set['resultSVO']['data']['rtnRsltCode'] == 'SUCCESS':
            return 1
        else:
            return -1
    else:
        return -2
