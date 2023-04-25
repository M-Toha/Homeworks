## Practice

# 1. Create a program that will ask user to search a word. Search this word in Giphy (use their API). 
# Return links to these GIFs as a result
import requests
def status_code(link: str) -> int:
    result = requests.get(link)
    return result.status_code

def giphy(keyword: str) -> str:
    res_giphy = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key=jPItATQv0KTft1Th0SUME1WMZtD2Ou34&q={keyword}&limit=25&offset=0&rating=g&lang=en')
# print(res_giphy.status_code)
    if status_code(f'https://api.giphy.com/v1/gifs/search?api_key=jPItATQv0KTft1Th0SUME1WMZtD2Ou34&q={keyword}&limit=25&offset=0&rating=g&lang=en') == 200:
        print(res_giphy.json()['data'][0]['url'])
    else: 
        print('Couldn\'t connect to the server')

giphy('apple')

# 2. Взяти API-weather, розпарсити і вивезти погоду від користувача(вводить локацію, по цій локації повернеться погода, вологість і тд)
# https://openweathermap.org *Потрібна реєстрація і створення свого api-ключа

def weather(longitude, latitude) -> str:
    res_weather = requests.get(f'https://proj_morderer:y6uA1Sv8R3@api.meteomatics.com/2023-04-24T18:45:00.000+03:00/t_2m:C,absolute_humidity_2m:gm3/{longitude},{latitude}/json?model=mix')
    if status_code(f'https://proj_morderer:y6uA1Sv8R3@api.meteomatics.com/2023-04-24T18:45:00.000+03:00/t_2m:C,absolute_humidity_2m:gm3/{longitude},{latitude}/json?model=mix') == 200:
        print(f'Temperature: {res_weather.json()["data"][0]["coordinates"][0]["dates"][0]["value"]}\n\
Absolute humidity: {res_weather.json()["data"][1]["coordinates"][0]["dates"][0]["value"]}') 
    else: 
        print('Couldn\'t connect to the server')    

weather(50.4500336, 30.5241361)

# 3. Вивезти всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json
def astronauts() -> str:
    res_astronauts = requests.get('http://api.open-notify.org/astros.json')
# print(res_astronauts.status_code)
    if status_code('http://api.open-notify.org/astros.json') == 200:
        print('Astronauts names:')
        for people in res_astronauts.json()['people']:
            print(people['name'])
    else: 
        print('Couldn\'t connect to the server')

astronauts()