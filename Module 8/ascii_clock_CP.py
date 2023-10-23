# Parse input depending on clock type
# If a 12 hour clock is chosen
if clock_type == "12":
    # If the number entered is larger than 12:00
    time = time.split(":") 
    if int(time[0]) > 12 and int(time[1]) > 00:
        # Subtract 12 from the hour and display PM
        time[0] = int(time[0]) - 12
        time = str(time[0]) + ":" + str(time[1]) + "PM"
    # If hour is 12 return 12 + minutes + PM
    elif int(time[0]) == 12:
       time = "12" + ":" + str(time[1]) + "PM"
    # If hour is 0 return 12 + minutes + AM
    elif int(time[0]) == 0:
    # Otherwise display as AM
        time = "12" + ":" + str(time[1]) + "AM"
    else:
        time = str(time[0]) + ":" + str(time[1]) + "AM"
# If a 24 hour clock is chosen
elif clock_type == "24":
    # Keep it the same as the input
    time = time