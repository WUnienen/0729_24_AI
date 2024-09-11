# %%
# 請下載日射量json資料,存檔名稱為'台灣日射量.json'
import requests
from requests.exceptions import HTTPError,ConnectionError,Timeout

try:
    url = "https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/O-A0091-001?Authorization=rdec-key-123-45678-011121314&format=JSON"
    response = requests.get(url)
    response.raise_for_status()
    content = response.text
    #print(content)
except ConnectionError:
    print("連線伺服器發生錯誤")
except Timeout:
    print("伺服器忙碌,沒有回應")
except HTTPError:
    print("伺服器回應連線錯誤")
except Exception:
    print("不知名的錯誤")

# %%
import io
import json
from pprint import pprint
file=io.StringIO(content)
#print(type(file))
content=json.load(file)

# %%
date:str=contents['cwaopendata']['sent']

# %%
Station=contents['cwaopendata']['dataset']['Station']
pprint(station)

# %%
for station in stations:
    name:str=station['StationName']
    weather:str=station['WeatherElement']['SolarRadiation']
    print(name,weather)
    print("================")

# %%
class Station():
    def __init__(self,name:str,weather:float):
        self.name=name
        self.weather=weather

stations1:list=[]
for station in stations:
    name:str=station['StationName']
    weather:str=station['WeatherElement']['SolarRadiation']
    station:Station=Station(name,float(weather))
    stations1.append(station)

stations1


