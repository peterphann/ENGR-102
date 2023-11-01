import time
import sympy as sp
import random as rand

x = sp.symbols('x')
y = sp.symbols('y')

function = sp.sympify('sin(cos(tan(x+y)))')
trials = 10
num = 20

times = []
for trial in range(trials):
  current_time = time.time()
  

  values1 = []
  for X in range(num):
    for Y in range(num):
      values1.append(function.subs({x:X, y:Y}))
  time1 = time.time() - current_time

  current_time = time.time()
  values2 = []
  for X in range(num):
    for Y in range(num):
      values2.append(function.evalf(subs={x:X, y:Y}))
  time2 = time.time() - current_time

  times.append(time1 - time2)

print(f'For {num ** 2} points in function {function}:')
print(f'subs() took {sum(times) / len(times)} secs longer')





