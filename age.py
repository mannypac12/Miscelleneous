## 크리스마스 특별코드

## 날짜 사이 기간을 Y 년 M 월 D 일로 변경

"""
연말정산에 왠지 유용할 것 같은 코드...
"""

import datetime
from dateutil.relativedelta import relativedelta 

## Convert date

print("날짜입력방식: yyyymmdd")

st_date = input("시작 일을 입력하세요: ")
ed_date = input("마지막 일을 입력하세요: ")

def convert_ymd(st_date, ed_date):

    cov_st_dt = datetime.datetime.strptime(st_date, '%Y%m%d')
    cov_ed_dt = datetime.datetime.strptime(ed_date, '%Y%m%d')
    rel_dt = relativedelta(cov_ed_dt, cov_st_dt)

    return f"""{rel_dt.years} 년 {rel_dt.months} 월 {rel_dt.days} 일"""

print(convert_ymd(st_date, ed_date))
