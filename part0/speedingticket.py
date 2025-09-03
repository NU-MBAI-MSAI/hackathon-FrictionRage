speedLimit = int(input())
drivingSpeed = int(input())

diff = drivingSpeed - speedLimit
if drivingSpeed < 0 or speedLimit < 0:
  sys.end()
if diff <= -10:
  print(50)
elif diff >= 6 and diff <= 20:
  print(75)
elif diff >=21 and diff <= 40:
  print(100)
elif diff >= 41:
  print(300)
else:
  print(0)
