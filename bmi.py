import tkinter
#import tkMessageBox

#Define method to calculate BMI
def bmiCalc(w,h):
	
	hSquared = h*h
	#print(hSquared)
	bmi = w/hSquared
	return bmi

#Method to calc bmr
def bmrCalc(w,h,a):
	wn = w*9.6
	ho = (h*100)*1.8
	af = a*4.7
	subtotal = (wn + ho) - af
	finalTotal = subtotal + 655
	return finalTotal

#Method to calc tDee
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

#Method to calc daily cal needs
def dailyCalNeeds(tDee):
	dailyCalNeed = tDee - 500
	return dailyCalNeed


#Declare main window for GUI
top = tkinter.Tk()
top.title("Fitness Program")

#Add an icon to window.
top.iconphoto(False,tkinter.PhotoImage(file=r'/home/joe/programming/pythonFiles/pyBmi/fitnessIcon.png'))

#Label for weight.
tkinter.Label(top,text="Weight in kgs: ").grid(row=0)

#Label for height
tkinter.Label(top,text="Height in metres: ").grid(row=1)

#Label for age
tkinter.Label(top,text="Age in years: ").grid(row=2)

#Entry box for weight
weightEntry = tkinter.Entry(top)
weightEntry.grid(row = 0, column=1)

#Entry box for height
heightEntry = tkinter.Entry(top)
heightEntry.grid(row = 1, column=1)

#Entry box for age
ageEntry = tkinter.Entry(top)
ageEntry.grid(row = 2, column=1)

#Radio Buttons for activity level.
activityFactor = tkinter.IntVar(top).get()

levelZero = tkinter.Radiobutton(top, text="Zero",variable=activityFactor, value = 0)
levelZero.grid(row = 0, column = 2)

levelOne = tkinter.Radiobutton(top, text="One",variable=activityFactor, value = 1)
levelOne.grid(row = 1, column = 2)

levelTwo = tkinter.Radiobutton(top, text="Two",variable=activityFactor, value = 2)
levelTwo.grid(row = 2, column = 2)

levelThree = tkinter.Radiobutton(top, text="Three",variable=activityFactor, value = 3)
levelThree.grid(row = 3, column = 2)

levelFour = tkinter.Radiobutton(top, text="Four",variable=activityFactor, value = 4)
levelFour.grid(row = 4, column = 2)

levelFive = tkinter.Radiobutton(top, text="Five",variable=activityFactor, value = 5)
levelFive.grid(row = 5, column = 2)

#Quit method for button.
def quit():
	global top
	top.destroy()

#Method to get entry field data, and make a calculation.
def calculationMethod():
			
	
	#Get the users stats into vars from entry boxes.
	we = weightEntry.get()
	he = heightEntry.get()
	age = ageEntry.get()

	#Convert to appropriate types
	we = float(we)
	he = float(he)
	age = float(age)

	bmi = bmiCalc(we,he)
	
	
	#Display the users stats on the GUI
	userTitleLabel = tkinter.Label(top,text="Your info: ",font='Helvetica 18 bold')
	userTitleLabel.grid(row = 5, column =0)	
	
	weLabel = tkinter.Label(top,text="Weight= {}".format(we))
	weLabel.grid(row = 7, column =0)

	heLabel = tkinter.Label(top,text="Height= {}".format(he))
	heLabel.grid(row = 8, column =0)

	ageLabel = tkinter.Label(top,text="Age= {}".format(age))
	ageLabel.grid(row = 9, column =0)

	bmiLabel = tkinter.Label(top,text="BMI= {}".format(bmi))
	bmiLabel.grid(row = 10, column =0)

	#weLabel = tkinter.Label(top,text="Weight= {}".format(bmi))
	#weLabel.grid(row = 11, column =0)
	
	#Print info for debug.
	print("+++++++++++++++++")
	print("Age = {} , Weight = {} , Height = {}".format(ageEntry.get(),we,heightEntry.get()))
	print("Your bmi is: {}".format(bmiCalc(we,he)))
	print("Activity Factor Selection is : {}".format(activityFactor))
	print("+++++++++++++++++")

#Quit Button
tkinter.Button(top,text="Quit",command=quit).grid(row=3,column=0)

#Calculation button.
#tkinter.Button(top,text="Calculate Fitness Info",command=calculationMethod(weightEntry,heightEntry,ageEntry)).grid(row=3,column=1)
tkinter.Button(top,text="Calculate Fitness Info",command=calculationMethod).grid(row=3,column=1)


top.mainloop()

print("This is a program to calculate your bmi...")

weight = float(input("Please input your weight in kgs:"))
height = float(input("Please input your height in metres:"))
age = float(input("Please input your age in years:"))

#print(weight,height)






myBmr = bmrCalc(weight,height,age)
	
myBmi = bmiCalc(weight,height)

myTDee = tDeeCalc(myBmr)
print("Your bmi is {}.".format(myBmi))
print("Your bmr is {} calories per day.".format(myBmr))
print("Your tDee is {}".format(myTDee))
print("Your daily calory need is {}".format(dailyCalNeeds(myTDee)))


