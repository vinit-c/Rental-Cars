#!/usr/bin/env python
# coding: utf-8

# In[ ]:


rentals = {
    "duster":{
        'color':'red',
        '24 hrs charges': 2500,
        'mileage': '22 km/ltr',
    },
    "eco sports":{
        'color':'cream',
        '24 hrs charges': 2800,
        'mileage': '24km/ltr',
    },
    "thar":{
        'color':'black',
        '24 hrs charges': 2200,
        'mileage': '20km/ltr',
    },
}


customer = input("Please enter your name: ")
print("\nHello " + customer.title() +"!")
print("\nThese are the cars available to rent out: ")


for cars, info in rentals.items():
    print("\nCar: " + cars.title())
    color = info['color']
    per_day_charges = info['24 hrs charges']
    mileage = info['mileage']
    
    print("Color: " + color.title())
    print("Per day charges: ₹"+ str(per_day_charges))
    print("Mileage: " + mileage)
    
vehicle = input("\nPlease enter the name of the car you want to rent out: ")

for cars in rentals.keys():
    if cars!=vehicle:
        continue
    print("\nCar selected: " + vehicle.title())
    for info in rentals.values():
        color = info['color']
        per_day_charges = info['24 hrs charges']
        mileage = info['mileage']
        if info !=rentals[vehicle]:
            continue
        print("Color: " + color.title())
        print("Per day charges: ₹"+ str(per_day_charges))
        print("Mileage: " + mileage)
        
        no_of_days = input("\nPlease enter the number of days you want to rent out the car: ")
        
        total_charges = int(no_of_days) * per_day_charges
        
        print("\nTotal rent for "+no_of_days+ " days: ₹" + str(total_charges))
        print("\nYou can either pay the total amount of ₹ " + str(total_charges) + " in advance," )
        print("or\nyou can pay half of the amount (₹" + str(total_charges//2)+ ") in advance and the rest (₹" +str(total_charges//2) + "), when you'll handover the car.")

print("\nNote: The total rent amount doesn't include the gas/fuel expenses.")


# In[ ]:




