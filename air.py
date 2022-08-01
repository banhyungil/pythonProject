import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

for row in rows:
    guName = row['MSRSTE_NM']
    guMise = row['IDEX_MVL']
    if guMise < 60:
        print(guName, guMise)

print(rows)