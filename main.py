from tkinter import *

window=Tk()
window.title("BMI Calculator")
window.minsize(300,100)
window.config(padx=30,pady=30)

def calculate_bmi():
    height=height_input.get()
    weight=weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height")
    else:
        try:
            bmi = float(weight) / (float(height)/100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except: result_label.config(text="Enter a valid number")

weight_label=Label(text="Enter your weight(kg)")
weight_label.pack()

weight_input=Entry(width=20)
weight_input.pack()

height_label=Label(text="Enter your height(cm)")
height_label.pack()

height_input=Entry(width=20)
height_input.pack()


my_button=Button(text="calculate",command=calculate_bmi,width=20)
my_button.pack()

result_label=Label()
result_label.pack()

def write_result(bmi):
    result_string=f"Your BMI is: {round(bmi,2)}. You are "
    if bmi < 16.0:
        result_string +="Severely Underweight"
    elif 16 <= bmi <18.5:
        result_string +="Underweight"
    elif 18.5 <= bmi <25:
        result_string +="Normal"
    elif 25 <= bmi <30:
        result_string +="Overweight"
    elif 30 <= bmi < 35:
        result_string +="Moderately Obese"
    elif 35 <= bmi < 40:
        result_string +="Severely Obese"
    else:
        result_string +="Mordily Obese"
    return result_string




window.mainloop()
