avgTemp = 0
heatingDays=0
coolingDays=0

while avgTemp >= -459: 
  avgTemp=int(input("Enter the average daily temperature: "))
  if avgTemp < 60 and avgTemp >=-459:
    heatingDays += 1
  elif avgTemp > 80:
    coolingDays +=1


print ("heating days: ",heatingDays)
print ("cooling days: ",coolingDays)
    
