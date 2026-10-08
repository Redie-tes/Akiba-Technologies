destiny = input("Destination: ")
distance = float(input("Distance in Kilometers: "))
avg_speed = float(input("ENter the speed in Km/h: ")) 
time = distance / avg_speed
time_in_hr = time//60
time_in_min = time % 60

print("Destination:", destiny)