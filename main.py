def angle(h,m):
    # covert to 12hr-notation
    if h>12:
        h-=12
    # hour angle
    a = (h*60+m)*0.5
    print("Angle made by hour-hand =",str(a)+"°")
    # min angle
    b = m*6
    print("Angle made by minute-hand =",str(b)+"°")
    # angle b/w min & hour
    r = abs(int(a-b))
    print("Angle between hour-hand and minute-hand =",str(r)+"°")
# time input
print("-----------------------------------------------")
print("Give a time in hh:mm format in 24-hour notation")
print("-----------------------------------------------")
# hour
h = int(input("hour: "))
# minute
m = int(input("minute: "))
if 0<=h<=24 and 0<=m<=60:
    angle(h,m)
else:
    print("Invalid-input")