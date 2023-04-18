import requests
res_monobank = requests.get('https://api.monobank.ua/bank/currency')
res_monobank.status_code
print(res_monobank.status_code, type(res_monobank.status_code))