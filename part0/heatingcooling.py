avgTemp = 0
heatingDays=0
coolingDays=0

while avgTemp >= -459: 
  avgTemp=input("Enter the average daily temperature: ")
  if avgTemp<60:
    heatingDays += 1
  else if avgTemp > 80:
    coolingDays +=1


print ("heating days: ",heatingDays)
print ("cooling days: ",coolingDays)
    
