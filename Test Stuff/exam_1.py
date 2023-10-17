fluids = ['Oil 769K            Critical Point 8648', 'Motor Oil 612K      Random Point 279', 'Motor Oil 511K      Critical Point 8829', 'Oil 375K            Random Point 4478', 'Motor Oil 536K      Boiling Point 4721', 'Milk 877K           Melting Point 6566', 'Water 852K          Melting Point 3916', 'Milk 307K           Critical Point 6035', 'Gasoline 724K       Random Point 8237', 'Motor Oil 398K      Melting Point 6139', 'Honey 941K          Random Point 9626', 'Oil 150K            Melting Point 4793', 'Milk 746K           Melting Point 4899', 'Honey 441K          Melting Point 9712', 'Motor Oil 633K      Boiling Point 844', 'Oil 187K            Boiling Point 5424', 'Cellulose 686K      Critical Point 0', 'Gasoline 667K       Melting Point 2642', 'Honey 603K          Critical Point 6898', 'Gasoline 756K       Critical Point 5009', 'Honey 816K          Melting Point 1190', 'Milk 983K           Random Point 8540', 'Honey 281K          Random Point 8932', 'Water 345K          Random Point 5290', 'Honey 183K          Boiling Point 6048', 'Water 489K          Critical Point 3734', 'Cellulose 869K      Boiling Point 2865', 'Cellulose 870K      Random Point 5353', 'Motor Oil 513K      Melting Point 2869', 'Water 556K          Boiling Point 5207', 'Gasoline 735K       Boiling Point 5546', 'Milk 310K           Melting Point 4008', 'Milk 143K           Melting Point 9398', 'Milk 920K           Random Point 494', 'Water 579K          Random Point 4884', 'Water 294K          Random Point 2456', 'Milk 564K           Boiling Point 3235', 'Water 170K          Random Point 3132', 'Gasoline 102K       Random Point 5924', 'Oil 586K            Random Point 9650', 'Water 712K          Critical Point 2187', 'Oil 342K            Boiling Point 6587', 'Honey 681K          Boiling Point 8492', 'Honey 291K          Critical Point 1156', 'Motor Oil 145K      Random Point 7688', 'Gasoline 621K       Melting Point 4169', 'Motor Oil 719K      Critical Point 3595', 'Milk 182K           Critical Point 8837', 'Oil 527K            Random Point 8844', 'Cellulose 596K      Random Point 3060', 'Cellulose 287K      Random Point 5361', 'Honey 730K          Melting Point 1963', 'Milk 160K           Random Point 732', 'Honey 169K          Random Point 3830', 'Gasoline 682K       Random Point 8947', 'Water 953K          Melting Point 3725', 'Motor Oil 860K      Melting Point 8664', 'Water 433K          Melting Point 4279', 'Cellulose 284K      Random Point 9633', 'Oil 220K            Boiling Point 3944', 'Cellulose 414K      Critical Point 5654', 'Oil 365K            Boiling Point 1380', 'Milk 724K           Boiling Point 979', 'Cellulose 606K      Critical Point 3929', 'Motor Oil 574K      Random Point 5280', 'Milk 693K           Random Point 7292', 'Milk 179K           Boiling Point 1724', 'Motor Oil 241K      Random Point 4883', 'Water 156K          Boiling Point 8704', 'Gasoline 683K       Critical Point 133', 'Gasoline 788K       Critical Point 607', 'Water 851K          Melting Point 2839', 'Water 824K          Critical Point 9458', 'Milk 624K           Melting Point 1723', 'Cellulose 311K      Critical Point 3217', 'Cellulose 909K      Melting Point 3570', 'Motor Oil 881K      Critical Point 7790', 'Water 847K          Critical Point 7734', 'Cellulose 125K      Melting Point 2955', 'Motor Oil 449K      Melting Point 7531', 'Honey 719K          Critical Point 8495', 'Milk 444K           Melting Point 2696', 'Water 967K          Boiling Point 262', 'Cellulose 357K      Melting Point 4499', 'Motor Oil 510K      Random Point 9691', 'Cellulose 254K      Melting Point 1489', 'Oil 944K            Melting Point 9717', 'Gasoline 293K       Critical Point 971', 'Water 970K          Random Point 4669', 'Water 307K          Melting Point 4905', 'Motor Oil 518K      Melting Point 5060', 'Gasoline 910K       Boiling Point 4151', 'Cellulose 765K      Random Point 3841', 'Oil 255K            Boiling Point 3550', 'Gasoline 196K       Melting Point 4822', 'Cellulose 562K      Boiling Point 5717', 'Water 924K          Random Point 5008', 'Honey 511K          Boiling Point 2860', 'Cellulose 216K      Melting Point 6017', 'Gasoline 389K       Boiling Point 9314']
# Prompt user for desired temperature
user_temp = input('Enter a temperature: ')

# Loop through fluids list until a string with the temperature is found
for fluid in fluids:
  if user_temp in fluid:
    matching_fluid = fluid
    break # Exit loop once a match is found

# Split fluid string into two separate strings and strip them of trailing or leading spaces
name_raw = matching_fluid[0:20]
name_raw = name_raw.strip()
property_raw = matching_fluid[20:]
property_raw = property_raw.strip()

# Split both strings by " " into lists. Join all strings except the last in each list to get the fluid name and property name respectively
name_list = name_raw.split(" ")
property_list = property_raw.split(" ")
print(name_list)
fluid_name = " ".join(name_list[:-1])
property_name = " ".join(property_list[:-1])

# Loop through fluids list and count the number of occurrences of the property
counter = 0
for fluid in fluids:
  if property_name in fluid:
    counter += 1

# Print information with proper formatting
print(f'The first fluid with temperature {user_temp} is below')
print(f'Fluid: {fluid_name}')
print(f'Property at {user_temp}: {property_raw}')
if counter == 1: # Guaranteed to have at least 1 match from the original fluid
  print(f'No other fluids found with property {property_name}')
else:
  print(f'Found {counter} more fluid(s) with property {property_name}')
