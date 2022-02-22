#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################

hr = float(input("What hour is the bus departing? "))
mins = float(input("How many minutes on the hour is the bus departing? "))
dist = float(input("How far is the bus traveling? (km) "))
stops = float(input("How many stops is the bus stopping at? "))

#constant variables
stoptime = 30
speed = 40

totalsec = stoptime * stops

hr += ((dist / speed))
if hr >= 24:
    hr -= 24

if (hr % 1 != 0):
    mins+=hr%1*60
    hr = int(hr)
    
mins += (totalsec) // 60
mins=round(mins, 1)

sec = (totalsec % 60)

if (mins % 1 == 0.50 and sec == 30.0):
    sec = 0.0
    mins += 0.5
elif (mins%1!=0.50 and sec == 30.0):
    sec=30
elif (mins%1==0.50 and sec==0):
    mins=int(mins)
    sec=30
else:
    mins +=0.50
    sec = 0


hr += mins // 60
mins = mins % 60

hr = int(hr)
mins = int(mins)
sec=int(sec)

print(f'You will arrive in: {hr:02d}:{mins:02d}:{sec:02d}')
