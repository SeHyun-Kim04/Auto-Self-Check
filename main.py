"""
    * 자동 자가진단 프로그램
    * https://github.com/SeHuyun-Kim04/Auto-Self-Check
    * Made By K.S.H(김세현)
"""


import check_Server
import get_SchoolName
import post_ASC

if __name__ == '__main__':
    # 1. 기본 변수 설정
    sc_name = "" # 학교입력
    st_name = ""  # 이름입력
    st_brith = ""  # 생일입력
    Area = ""  # 지역입력

    # 2. 지역별 주소 설정 & 확인
    print("===== 자동화 자가진단.")
    link = check_Server.main(Area)
    if link == -1:
        print("Error - 서버확인(Area)")
        exit()
    elif link == -2:
        print("Error - 지역확인")
        exit()

    # 3.  CNE(qstnCrtfcNoEncpt)가져오기
    CNE = get_SchoolName.main(link, sc_name, st_name, st_brith)
    if CNE == -1:
        print("Error - CNE Get 실패")
        exit()

    # 4. 검사완료 POST하기.
    check = post_ASC.main(link, sc_name, st_name, CNE)
    if check == -1:
        print("Error - 서버확인(post_ASC)")
        exit()
    elif check == -2:
        print("Error - post 확인")
        exit()

    print("자가진단 완료")
