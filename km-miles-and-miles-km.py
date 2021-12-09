entry=int(input("To convert from kilometers to miles write 1\nTo convert from miles to kilometers write 2: "))

conversion_factor=0.621371

if entry==1:   # KM to miles
    kilometers=float(input("\nEnter value in kilometers: "))
    miles=kilometers*conversion_factor
    print("\n{0:.2f} Kilometers = {1:.2f} Miles\n".format(kilometers,miles))  # format presented in python version +2.6
    
elif entry==2:   # miles to KM
    miles=float(input("\nEnter value in miles: "))
    kilometers=miles/conversion_factor
    print('\n%.2f Miles = %.2f Kilometers\n' %(miles,kilometers))   # format presented in python before ver. 2.6
else:
    print('\nPlz try again and only write 1 or 2.')