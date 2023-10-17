rounding = 2

sol = input('Enter the value you are trying to calculate (p/v/n/t): ')

if (sol != 'p'):
  pressure_raw = input('Enter pressure: ')
  pressure_split = pressure_raw.split(' ')
  pressure_atm = float(pressure_split[0])
  pressure_unit = pressure_split[1]  
  if pressure_unit == 'mmHg': pressure_atm /= 760.0
  elif pressure_unit == 'bar': pressure_atm /= 1.013
  elif pressure_unit == 'kPa': pressure_atm /= 101.3 

  print(pressure_atm)

if (sol != 'v'):
  volume_raw = input('Enter volume: ')
  volume_split = volume_raw.split(' ')
  volume_L = float(volume_split[0])
  volume_unit = volume_split[1]

  if volume_unit == 'mL': pressure_atm /= 1000

moles = None if sol == 'n' else float(input('Enter moles: '))

if (sol != 't'):
  temperature_raw = input('Enter temperature: ')
  temperature_split = temperature_raw.split()
  temperature_K = float(temperature_split[0])
  temperature_unit = temperature_split[1]

  if temperature_unit == 'C': temperature_K += 273.15
  elif temperature_unit == 'F': temperature_K = (temperature_K - 32) * (5/9) + 273.15

gas_constant = 0.08206

if sol == 'p':
  pressure = (moles * gas_constant * temperature_K) / volume_L
  print('The pressure is:')
  print(f'{pressure:.{rounding}f} atm.')
  print(f'{760 * pressure:.{rounding}f} mmHg.')
  print(f'{1.013 * pressure:.{rounding}f} bar.')
  print(f'{101.3 * pressure:.{rounding}f} bar.')
elif sol == 'v':
  print(moles, gas_constant, temperature_K, pressure_atm)
  volume = (moles * gas_constant * temperature_K) / pressure_atm
  print('The volume is:')
  print(f'{volume} L.')
  print(f'{1000 * volume} mL.')
elif sol == 'n':
  print(f'There are {(pressure_atm * volume_L) / (temperature_K * gas_constant)} moles.')
elif sol == 't':
  temperature = (pressure_atm * volume_L) / (moles * gas_constant)
  print('The temperature is:')
  print(f'{temperature} K')
  print(f'{temperature - 273.15} C')
  print(f'{(temperature - 273.15) * (9/5) + 32} F')
else:
  print('Invalid operation you dumbfuck')
