from random import randint

def calculate(sex, age, cholesterol, smoker, hdl, sbp, treated):
  points = 0
  final = 0

  if sex == 'M':
    if age <= 34: points -= 9
    elif age <= 39: points -=4
    elif age <= 44: points += 0
    elif age <= 49: points += 3
    elif age <= 54: points += 6
    elif age <= 59: points += 8
    elif age <= 64: points += 10
    elif age <= 69: points += 11
    elif age <= 74: points += 12
    else: points += 13

    if cholesterol < 160: points += 0
    elif cholesterol <= 199:
      if age <= 39: points += 4
      elif age <= 49: points += 3
      elif age <= 59: points += 2
      elif age <= 69: points += 1
      else: points += 0
    elif cholesterol <= 239:
      if age <= 39: points += 7
      elif age <= 49: points += 5
      elif age <= 59: points += 3
      elif age <= 69: points += 1
      else: points += 0
    elif cholesterol <= 279:
      if age <= 39: points += 9
      elif age <= 49: points += 6
      elif age <= 59: points += 4
      elif age <= 69: points += 2
      else: points += 1
    else:
      if age <= 39: points += 11
      elif age <= 49: points += 8
      elif age <= 59: points += 5
      elif age <= 69: points += 3
      else: points += 1

    if smoker:
      if age <= 39: points += 8
      elif age <= 49: points += 5
      elif age <= 59: points += 3
      else: points += 1

    if hdl < 40: points += 2
    elif hdl <= 49: points += 1
    elif hdl <= 59: points += 0
    else: points -= 1

    if treated:
      if sbp < 120: points += 0
      elif sbp <= 129: points += 1
      elif sbp <= 139: points += 2
      elif sbp <= 159: points += 2
      else: points += 3
    else:
      if sbp < 120: points += 0
      elif sbp <= 129: points += 0
      elif sbp <= 139: points += 1
      elif sbp <= 159: points += 1
      else: points += 2

    if points < 0: final = '<1'
    elif points <= 4: final = 1
    elif points <= 6: final = 2
    elif points == 7: final = 3
    elif points == 8: final = 4
    elif points == 9: final = 5
    elif points == 10: final = 6
    elif points == 11: final = 8
    elif points == 12: final = 10
    elif points == 13: final = 12
    elif points == 14: final = 16
    elif points == 15: final = 20
    elif points == 16: final = 25
    else: final = '>30'

  else:
    if age <= 34: points -= 7
    elif age <= 39: points -= 3
    elif age <= 44: points += 0
    elif age <= 49: points += 3
    elif age <= 54: points += 6
    elif age <= 59: points += 8
    elif age <= 64: points += 10
    elif age <= 69: points += 12
    elif age <= 74: points += 14
    else: points += 16

    if cholesterol < 160: points += 0
    elif cholesterol <= 199:
      if age <= 39: points += 4
      elif age <= 49: points += 3
      elif age <= 59: points += 2
      elif age <= 69: points += 1
      else: points += 1
    elif cholesterol <= 239:
      if age <= 39: points += 8
      elif age <= 49: points += 6
      elif age <= 59: points += 4
      elif age <= 69: points += 2
      else: points += 1
    elif cholesterol <= 279:
      if age <= 39: points += 11
      elif age <= 49: points += 8
      elif age <= 59: points += 5
      elif age <= 69: points += 3
      else: points += 2
    else:
      if age <= 39: points += 13
      elif age <= 49: points += 10
      elif age <= 59: points += 7
      elif age <= 69: points += 4
      else: points += 2
    if smoker:
      if age <= 39: points += 9
      elif age <= 49: points += 7
      elif age <= 59: points += 4
      elif age <= 69: points += 2
      else: points += 1
    if hdl < 40: points += 2
    elif hdl <= 49: points += 1
    elif hdl <= 59: points += 0
    else: points -= 1
    if treated:
      if sbp < 120: points += 0
      elif sbp <= 129: points += 3
      elif sbp <= 139: points += 4
      elif sbp <= 159: points += 5
      else: points += 6
    else:
      if sbp < 120: points += 0
      elif sbp <= 129: points += 1
      elif sbp <= 139: points += 2
      elif sbp <= 159: points += 3
      else: points += 4

    if points < 9: final = '<1'
    elif points <= 12: final = 1
    elif points <= 14: final = 2
    elif points == 15: final = 3
    elif points == 16: final = 4
    elif points == 17: final = 5
    elif points == 18: final = 6
    elif points == 19: final = 8
    elif points == 20: final = 11
    elif points == 21: final = 14
    elif points == 22: final = 17
    elif points == 23: final = 22
    elif points == 24: final = 27
    else: final = '>30'
    
  print(f'sex:{sex} age:{age} cho:{cholesterol} smo:{"Y" if smoker else "N"} hdl:{hdl} sbp:{sbp} med:{"Y" if treated else "N"} out:{final}')

# calculate('M', 20, 150, True, 30, 115, True)
# calculate('M', 20, 180, False, 45, 125, True)
# calculate('M', 20, 220, True, 55, 135, True)
# calculate('M', 20, 260, True, 65, 145, True)
# calculate('M', 20, 290, True, 40, 165, True)
# calculate('M', 40, 150, True, 40, 115, False)
# calculate('M', 40, 180, False, 40, 125, False)
# calculate('M', 40, 220, True, 40, 135, False)
# calculate('M', 40, 260, True, 40, 145, False)
# calculate('M', 40, 290, True, 40, 165, False)
# calculate('M', 50, 150, True, 40, 120, True)
# calculate('M', 50, 180, False, 40, 120, True)
# calculate('M', 50, 220, True, 40, 120, True)
# calculate('M', 50, 260, True, 40, 120, True)
# calculate('M', 50, 290, True, 40, 120, True)
# calculate('M', 60, 150, True, 40, 120, True)
# calculate('M', 60, 180, True, 40, 120, True)
# calculate('M', 60, 220, False, 40, 120, True)
# calculate('M', 60, 260, True, 40, 120, True)
# calculate('M', 60, 290, True, 40, 120, True)
# calculate('M', 70, 150, True, 40, 120, True)
# calculate('M', 70, 180, False, 40, 120, True)
# calculate('M', 70, 220, True, 40, 120, True)
# calculate('M', 70, 260, True, 40, 120, True)
# calculate('M', 70, 290, True, 40, 120, True)
# calculate('M', 35, 290, True, 40, 120, True)
# calculate('M', 45, 290, True, 40, 120, True)
# calculate('M', 55, 290, True, 40, 120, True)
# calculate('M', 65, 290, True, 40, 120, True)
# calculate('M', 70, 290, True, 40, 120, True)
# calculate('M', 75, 290, True, 40, 120, True)



# calculate('F', 20, 150, True, 30, 115, True)
# calculate('F', 20, 180, False, 45, 125, True)
# calculate('F', 20, 220, True, 55, 135, True)
# calculate('F', 20, 260, True, 65, 145, True)
# calculate('F', 20, 290, True, 40, 165, True)
# calculate('F', 40, 150, True, 40, 115, False)
# calculate('F', 40, 180, False, 40, 125, False)
# calculate('F', 40, 220, True, 40, 135, False)
# calculate('F', 40, 260, True, 40, 145, False)
# calculate('F', 40, 290, True, 40, 165, False)
# calculate('F', 50, 150, True, 40, 120, True)
# calculate('F', 50, 180, False, 40, 120, True)
# calculate('F', 50, 220, True, 40, 120, True)
# calculate('F', 50, 260, True, 40, 120, True)
# calculate('F', 50, 290, True, 40, 120, True)
# calculate('F', 60, 150, True, 40, 120, True)
# calculate('F', 60, 180, True, 40, 120, True)
# calculate('F', 60, 220, False, 40, 120, True)
# calculate('F', 60, 260, True, 40, 120, True)
# calculate('F', 60, 290, True, 40, 120, True)
# calculate('F', 70, 150, True, 40, 120, True)
# calculate('F', 70, 180, False, 40, 120, True)
# calculate('F', 70, 220, True, 40, 120, True)
# calculate('F', 70, 260, True, 40, 120, True)
# calculate('F', 70, 290, True, 40, 120, True)
# calculate('F', 35, 290, True, 40, 120, True)
# calculate('F', 45, 290, True, 40, 120, True)
# calculate('F', 55, 290, True, 40, 120, True)
# calculate('F', 65, 290, True, 40, 120, True)
# calculate('F', 70, 290, True, 40, 120, True)
# calculate('F', 75, 290, True, 40, 120, True)

# calculate('M', 40, 159, False, 55, 110, True)
# calculate('M', 40, 159, False, 30, 110, True)
# calculate('M', 40, 163, False, 55, 110, True)
# calculate('M', 40, 159, True, 55, 110, True)
# calculate('M', 40, 159, True, 30, 110, True)

# calculate('F', 40, 250, False, 45, 110, True)
# calculate('F', 40, 250, False, 30, 110, True)
# calculate('F', 40, 250, False, 30, 125, False)
# calculate('F', 40, 250, False, 30, 125, True)
# calculate('F', 40, 250, False, 45, 170, True)
# calculate('F', 75, 300, False, 45, 170, True)

# m_list.sort()
# f_list.sort()
# print(m_list)
# print(f_list)



  