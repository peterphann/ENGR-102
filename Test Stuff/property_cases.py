import random as rand

names = ['Water', 'Oil', 'Honey', 'Gasoline', 'Motor Oil', 'Cellulose', 'Milk']
properties = ['Boiling Point', 'Melting Point', 'Random Point', 'Critical Point']



def create_cases(num : int):
  cases = []
  for i in range(num):
    name = rand.choice(names)
    temp = rand.randint(100, 999)
    property = rand.choice(properties)
    property_val = rand.randint(0, 9999)

    first = f'{name} {temp}K'
    second = f'{property} {property_val}'
    cases.append(f'{first:<20}{second}')

  print(cases)

create_cases(100)