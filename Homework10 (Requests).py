## Practice

# 1. Create a program that will ask user to search a word. Search this word in Giphy (use their API). 
# Return links to these GIFs as a result
import requests
keyword = input('Enter the keyword: ')
res_giphy = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key=jPItATQv0KTft1Th0SUME1WMZtD2Ou34&q={keyword}&limit=25&offset=0&rating=g&lang=en')
# print(res_giphy.status_code)
if res_giphy.status_code == 200:
    print(res_giphy.json()['data'][0]['url'])
else: 
    print('Couldn\'t connect to the server')


# 2. Взяти API-weather, розпарсити і вивезти погоду від користувача(вводить локацію, по цій локації повернеться погода, вологість і тд)
# https://openweathermap.org *Потрібна реєстрація і створення свого api-ключа

longitude = float(input('Enter longitude: '))
latitude = float(input('Enter latitude: ')) #координати?
res_weather = requests.get('https://proj_morderer:y6uA1Sv8R3@api.meteomatics.com/2023-04-22T19:35:00.000+03:00/t_2m:C,absolute_humidity_2m:gm3/50.4500336,30.5241361/json?model=mix')
print(res_weather.status_code)
print(f'Temperature: {res_weather.json()["data"][0]["coordinates"][0]["dates"][0]["value"]}\n\
Absolute humidity: {res_weather.json()["data"][1]["coordinates"][0]["dates"][0]["value"]}') 

# 3. Вивезти всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json

res_astronauts = requests.get('http://api.open-notify.org/astros.json')
# print(res_astronauts.status_code)
if res_astronauts.status_code == 200:
    print('Astronauts names:')
    for people in res_astronauts.json()['people']:
        print(people['name'])
else: 
    print('Couldn\'t connect to the server')
