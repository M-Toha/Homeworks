'''
### Practice

1. Modify the Country class to include a third instance attribute called capital as a string. 
Store your new class in a script and test it out by adding the following code at the bottom of the script:
```
japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.") 
```
The output of your script should be:

Japan population is 140000000 and capital is Tokyo.
'''
class Country:
    def __init__(self, name: str, population: int, capital: str):
        self.name = name
        self.population = population
        self.capital = capital
japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.") 

# 2. Add increase_population method to country class. 
# This method should take an argument and increase population of the country on this number. 
class Country:
    def __init__(self, name: str, population: int, capital: str):
        self.name = name
        self.population = population
        self.capital = capital
    def increase_population(self, increse_number: int):
        self.population += increse_number
        return self.population
japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
japan.increase_population(23000)
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")

'''
3. Create add method to add two countries together. 
This method should create another country object with the name of the two countries combined 
and population of the two countries added together.
```
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'
```
'''
class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
    def increase_population(self, increse_number: int):
        self.population += increse_number
        return self.population
    def add(self, second_country: Country):
        return Country(name = f'{self.name} {second_country.name}', population = self.population + second_country.population)
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
assert(bosnia_herzegovina.population) == 15000000
assert(bosnia_herzegovina.name) == 'Bosnia Herzegovina'

'''
4. (Optional) Implement previous method with magic method

```
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'
```'''
class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
    def increase_population(self, increse_number: int):
        self.population += increse_number
        return self.population
    def __add__(self, second_country: Country):
        return Country(name = f'{self.name} {second_country.name}', population = self.population + second_country.population)
    
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
assert(bosnia_herzegovina.population) == 15000000
assert(bosnia_herzegovina.name) == 'Bosnia Herzegovina'
print(bosnia_herzegovina.name, bosnia_herzegovina.population)