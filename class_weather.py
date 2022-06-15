import json, urllib.request, time, firebase_admin, zlib, os
from firebase_admin import credentials, firestore

class WeatherHandle:
    def __init__(self, apikeyPath, datacredPath, timeZone, OpAu):
        with open(apikeyPath, 'r') as f:
            self.apiKey = f.read()
        self.OpAu = OpAu
        cred = credentials.Certificate(datacredPath)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client().collection('crawler-practice-project-3').document('One-Loaf-of-Dragon')

        os.environ['TZ'] = timeZone
        time.tzset()
        self.nowTime = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

        self.resultData = ""
    def getWeatherData(self, fetchList):
        if self.OpAu:
            allData = [json.loads(urllib.request.urlopen(f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-{fetches}?Authorization={self.apiKey}&format=JSON&elementName=&sort=time").read().decode('utf-8')) for fetches in fetchList]
        else:
            allData = [{fetches[0]:json.loads(urllib.request.urlopen(f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{str(fetches[1])}?apikey={self.apiKey}&language=zh-tw&details=true").read().decode('utf-8'))} for fetches in fetchList]
        compressAllData = zlib.compress(str(allData).encode('utf-8'))
        self.resultData = {self.nowTime:compressAllData}
        return True
    def setFirebase(self):
        if self.OpAu:
            doc_ref = self.db.collection('Project-01')
        else:
            doc_ref = self.db.collection('Project-02')
        doc_ref.document("weather-"+self.nowTime).set(self.resultData)
        return True
    def getDatabase(self):
        if self.OpAu:
            doc_ref = self.db.collection('Project-01')
        else:
            doc_ref = self.db.collection('Project-02')
        return {self.nowTime:zlib.decompress(doc_ref.document("weather-"+self.nowTime).get().to_dict()[self.nowTime]).decode('utf-8')}
    