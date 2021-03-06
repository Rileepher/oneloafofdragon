from class_weather import WeatherHandle
#F-D0047-001(宜蘭縣), F-D0047-005(桃園市), F-D0047-009(新竹縣), F-D0047-013(苗栗縣), F-D0047-017(彰化縣), F-D0047-021(南投縣), F-D0047-025(雲林縣), F-D0047-029(嘉義縣), F-D0047-033(屏東縣), F-D0047-037(臺東縣), F-D0047-041(花蓮縣), F-D0047-045(澎湖縣), F-D0047-049(基隆市), F-D0047-053(新竹市), F-D0047-057(嘉義市), F-D0047-061(臺北市), F-D0047-065(高雄市), F-D0047-069(新北市), F-D0047-073(臺中市), F-D0047-077(臺南市), F-D0047-081(連江縣), F-D0047-085(金門縣)
fetchList = ['001', '005', '009', '013', '017', '021', '025', '029', '033', '037', '041', '045', '049', '053', '057', '061', '065', '069', '073', '077', '081', '085']
apikeyPath = 'openweatherkey'
datacredPath = "crawler-practice-firebase-adminsdk-credential.json"
timeZone = 'Asia/Taipei'
OpAu = True

openWeather = WeatherHandle(apikeyPath=apikeyPath, datacredPath=datacredPath, timeZone=timeZone, OpAu=OpAu)
openWeather.getWeatherData(fetchList=fetchList)
openWeather.setFirebase()
# print(openWeather.getDatabase())
