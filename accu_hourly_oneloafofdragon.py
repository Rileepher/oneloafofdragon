from class_weather import WeatherHandle
#(宜蘭縣) 3369296,(桃園市) 3369297, (新竹縣) 3369298, (苗栗縣) 3369299, (彰化縣) 3369300, (南投縣) 3369301, (雲林縣) 3369302, (嘉義縣) 3369303, (屏東縣) 3369304, (臺東縣) 3369305, (花蓮縣) 3369306, (澎湖縣) 3369307, (基隆市) 312605, (新竹市) 313567, (嘉義市) 312591, (臺北市) 315078, (高雄市) 313812, (新北市) 2515397, (臺中市) 315040, (臺南市) 314999, (連江縣) 3369309, (金門縣) 2332525
fetchList = [["宜蘭縣", 3369296],["桃園市", 3369297], ["新竹縣", 3369298], ["苗栗縣", 3369299], ["彰化縣", 3369300], ["南投縣", 3369301], ["雲林縣", 3369302], ["嘉義縣", 3369303], ["屏東縣", 3369304], ["臺東縣", 3369305], ["花蓮縣", 3369306], ["澎湖縣", 3369307], ["基隆市", 312605], ["新竹市", 313567], ["嘉義市", 312591], ["臺北市", 315078], ["高雄市", 313812], ["新北市", 2515397], ["臺中市", 315040], ["臺南市", 314999], ["連江縣", 3369309], ["金門縣", 2332525]]
apikeyPath = 'accuweatherkey'
datacredPath = "crawler-practice-firebase-adminsdk-credential.json"
timeZone = 'Asia/Taipei'
OpAu = False

openWeather = WeatherHandle(apikeyPath=apikeyPath, datacredPath=datacredPath, timeZone=timeZone, OpAu=OpAu)
openWeather.getWeatherData(fetchList=fetchList)
openWeather.setFirebase()
# print(openWeather.getDatabase())