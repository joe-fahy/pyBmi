import tkinter
top = tkinter.Tk()
top.title("Fitness Program")
#Label for weight.
tkinter.Label(top,text="Weight in kgs: ").grid(row=0)

#Label for height
tkinter.Label(top,text="Height in metres: ").grid(row=1)

#Label for age
tkinter.Label(top,text="Age in years: ").grid(row=2)

#Entry box for weight
weightEntry = tkinter.Entry(top).grid(row = 0, column=1)

#Entry box for height
heightEntry = tkinter.Entry(top).grid(row = 1, column=1)

#Entry box for age
ageEntry = tkinter.Entry(top).grid(row = 2, column=1)

#Quit Button
tkinter.Button(top,text="Quit",command=top.quit).grid(row=3,column=0)

#Calculation button.
tkinter.Button(top,text="Calculate Fitness Info",command=top.quit).grid(row=3,column=1)

top.mainloop()

print("This is a program to calculate your bmi...")

weight = float(input("Please input your weight in kgs:"))
height = float(input("Please input your height in metres:"))
age = float(input("Please input your age in years:"))

#print(weight,height)

def bmiCalc(w,h):
	
	hSquared = h*h
	#print(hSquared)
	bmi = w/hSquared
	return bmi



def bmrCalc(w,h,a):
	wn = w*9.6
	ho = (h*100)*1.8
	af = a*4.7
	subtotal = (wn + ho) - af
	finalTotal = subtotal + 655
	return finalTotal

def tDeeCalc(bmr):
	print("0 - Sedentary - Little to no excercise, desk job.\n")
	print("1 - Lightly Active - Light Excercise 1-3 days per week.\n")
	print("2 - Moderately Active - Moderate Excercise 3-5 days per week.\n")
	print("3 - Very Active - Heavy Excercise 6-7 days per week.\n")
	print("4 - Extremely Active - Extremely Heavy Excercise, twice per day.\n")
	print("5 - FBG workouts\n")
	activityFactorSelection = int(input("Please enter the number which corresponds to your activity level:"))
	
	activityFactorList = [1.2,1.375,1.55,1.725,1.9,1.63]

	activityFactor = activityFactorList[activityFactorSelection]
	print("Your activity factor is {}".format(activityFactor))

	tdee = bmr * activityFactor
	return tdee

def dailyCalNeeds(tDee):
	dailyCalNeed = tDee - 500
	return dailyCalNeed

myBmr = bmrCalc(weight,height,age)
	
myBmi = bmiCalc(weight,height)

myTDee = tDeeCalc(myBmr)
print("Your bmi is {}.".format(myBmi))
print("Your bmr is {} calories per day.".format(myBmr))
print("Your tDee is {}".format(myTDee))
print("Your daily calory need is {}".format(dailyCalNeeds(myTDee)))


