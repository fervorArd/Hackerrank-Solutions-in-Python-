import math

AB,BC = int(input()),int(input())
#Right angled triangle median theorem
result = math.degrees(math.acos((BC/2)/(math.hypot(AB,BC)/2))) 
print(str(round(result)) + '\u00b0')
