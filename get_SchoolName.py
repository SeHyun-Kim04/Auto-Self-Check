import requests
import get_CrtfcNoEncpt


def main(URL, sc_name, st_name, st_brith):
    send_data = {
        "schulNm": sc_name
    }

    res = requests.post(URL + '/stv_cvd_co00_003.do', data=send_data)
    t = res.text.find('firstSchulCode')

    S_code = ""
    for i in range(10):
        S_code += res.text[t + 45 + i];

    if res.status_code == 200:
        return get_CrtfcNoEncpt.main(URL, sc_name, st_name, st_brith, S_code)

    else:
        return -1
