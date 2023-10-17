import random as rand

def average(lst):
  return sum(lst) / len(lst)

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

# Setup main variables
total_rolls = 0
finished = False

# Prompt to get starting values
total_tickets = int(input('Enter the total number of tickets: '))
owned_tickets = int(input('Enter the number of tickets you own: '))
total_prizes = int(input('Enter the number of prizes: '))
roll_interval = int(input('Enter the number of simulations to run: '))
print()

# Create possible values for tickets
simulated_wins = []
all_tickets = set(range(total_tickets))
your_tickets = set(range(owned_tickets))

# Setup values for progress bar
progress_max = 20
progress_ticks = [round(x * roll_interval / progress_max) for x in range(0, progress_max + 1)]

# Run simulations until prompted to finish
while not finished:
  print(f'{"=" * progress_max} {total_rolls + roll_interval} rolls')
  for roll in range(roll_interval):
    if roll in progress_ticks:
      print('■', end='')
    total_rolls += 1
    shuffled_tickets = list(all_tickets)
    rand.shuffle(shuffled_tickets)

    winning_tickets = set(shuffled_tickets[:total_prizes])
    raffles_won = len(winning_tickets.intersection(your_tickets))

    simulated_wins.append(raffles_won)
  finished = True if input('\nContinue simulating? (Y/N): ') == 'N' else False

# Calculate percent yield
num_yield = len([1 for i in simulated_wins if i > 0])
percent_yield = num_yield / len(simulated_wins) * 100
  
print('------------------------------------')
print(f'You simulated {total_rolls} drawings of {total_tickets} tickets with {total_prizes} prizes, where you have {owned_tickets} owned tickets.')
print(f'In the end, you averaged {average(simulated_wins):.2f} wins per raffle simulation.')
print(f'You won at least one prize {percent_yield:.2f}% of the time.')
print()
maximum = max(simulated_wins)
minimum = min(simulated_wins)
print(f'Your highest yield was {maximum}, first seen on Roll {simulated_wins.index(maximum)}.')
print(f'Your lowest yield was {minimum}, first seen on Roll {simulated_wins.index(minimum)}.')
print()

max_boxes = 35
mode = max(set(simulated_wins), key=simulated_wins.count)
box_scale = max_boxes / (simulated_wins.count(mode) / total_rolls)
for number in range(minimum, maximum + 1):
  distribution = simulated_wins.count(number)
  percentage = distribution / total_rolls
  boxes = '■' * int(percentage * box_scale)
  print(f'{number}\t|{boxes} {human_format(distribution)}')





