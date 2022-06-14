import json, urllib.request, time, firebase_admin, zlib, os
from firebase_admin import credentials, firestore

os.environ['TZ'] = 'Asia/Taipei'
time.tzset()
nowTime = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

with open('accuweatherkey', 'r') as f:
    apikey = f.read()[:-1]

#(宜蘭縣) 3369296,(桃園市) 3369297, (新竹縣) 3369298, (苗栗縣) 3369299, (彰化縣) 3369300, (南投縣) 3369301, (雲林縣) 3369302, (嘉義縣) 3369303, (屏東縣) 3369304, (臺東縣) 3369305, (花蓮縣) 3369306, (澎湖縣) 3369307, (基隆市) 312605, (新竹市) 313567, (嘉義市) 312591, (臺北市) 315078, (高雄市) 313812, (新北市) 2515397, (臺中市) 315040, (臺南市) 314999, (連江縣) 3369309, (金門縣) 2332525
fetchList = [["宜蘭縣", 3369296],["桃園市", 3369297], ["新竹縣", 3369298], ["苗栗縣", 3369299], ["彰化縣", 3369300], ["南投縣", 3369301], ["雲林縣", 3369302], ["嘉義縣", 3369303], ["屏東縣", 3369304], ["臺東縣", 3369305], ["花蓮縣", 3369306], ["澎湖縣", 3369307], ["基隆市", 312605], ["新竹市", 313567], ["嘉義市", 312591], ["臺北市", 315078], ["高雄市", 313812], ["新北市", 2515397], ["臺中市", 315040], ["臺南市", 314999], ["連江縣", 3369309], ["金門縣", 2332525]]
allData = [{fetches[0]:json.loads(urllib.request.urlopen(f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{str(fetches[1])}?apikey={apikey}&language=zh-tw&details=true").read().decode('utf-8'))} for fetches in fetchList]
compressAllData = zlib.compress(str(allData).encode('utf-8'))
resultData = {nowTime:compressAllData}

cred = credentials.Certificate("crawler-practice-firebase-adminsdk-credential.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection('crawler-practice-project-3').document('One-Loaf-of-Dragon').collection('Project-02')
doc_ref.document("weather-"+nowTime).set(resultData)

fromDataBase = doc_ref.document("weather-"+nowTime).get().to_dict()
assert str(allData) == zlib.decompress(fromDataBase[nowTime]).decode('utf-8')