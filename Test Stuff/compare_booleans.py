print('A B C | 1 2')
print('-----------')

differences = 0

for i in [True, False]:
  a = i
  for j in [True, False]:
    b = j
    for k in [True, False]:
      c = k
      boolean_expression_1 = b and a
      boolean_expression_2 = (c or b) and (b and a)
      if not boolean_expression_1 == boolean_expression_2: differences += 1
      print(f'{int(a)} {int(b)} {int(c)}   {int(boolean_expression_1)} {int(boolean_expression_2)}')
print(f'There {"was" if differences == 1 else "were"} {differences} {"difference" if differences == 1 else "differences"}!')