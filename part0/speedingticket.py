
speedLimit = input()
drivingSpeed = input()

diff = drivingSpeed - speedLimit

if diff <= -10:
  print(50)
else if diff >= 6 && diff <= 20:
  print(75)
else if diff >=21 && diff <= 40:
  print(100)
else if diff >= 41:
  print(300)
else:
  print(0)
