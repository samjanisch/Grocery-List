import random
from tkinter import *

window = Tk()
window.geometry("700x500")

def calc_bill():
    bread = e1.get()
    turkey = e2.get()
    apple = e3.get()
    onion = e4.get()
    olive_oil = e5.get()
    flank_steak = e6.get()
    salmon = e7.get()
    pretzels = e8.get()
    total = (int(bread)*2.99 + int(turkey)*3.99 + int(apple)*1.00 + int(onion)*0.50 + int(olive_oil)*5.00 +
             int(flank_steak)*12.00 + int(salmon)*8.00 + int(pretzels)*2.99)
    label9 = Label(window, text="Your Total is: $" + str(round(total, 2)), font="times= 10 bold")
    label9.place(x=200, y=350)


label1 = Label(window, text="Store Inventory", font="times= 26 bold")
label1.place(x=225, y=0)

label10 = Label(window, text="Please Enter the Quantity of Available Items", font="times= 15 bold")
label10.place(x=140, y=50)

label2 = Label(window, text="Bread: $2.99", font="times= 10 bold")
label2.place(x=100, y=100)

e1 = Entry(window)
e1.place(x=200, y=100)

label3 = Label(window, text="Turkey: $3.99", font="times= 10 bold")
label3.place(x=100, y=150)

e2 = Entry(window)
e2.place(x=200, y=150)

label4 = Label(window, text="Apple: $1.00", font="times= 10 bold")
label4.place(x=100, y=200)

e3 = Entry(window)
e3.place(x=200, y=200)

label5 = Label(window, text="Onion: $0.50", font="times= 10 bold")
label5.place(x=100, y=250)

e4 = Entry(window)
e4.place(x=200, y=250)

label6 = Label(window, text="Olive Oil: $5.00", font="times= 10 bold")
label6.place(x=400, y=100)

e5 = Entry(window)
e5.place(x=500, y=100)

label7 = Label(window, text="Flank Steak: $12.00", font="times= 10 bold")
label7.place(x=400, y=150)

e6 = Entry(window)
e6.place(x=530, y=150)

label8 = Label(window, text="Salmon: $8.00", font="times= 10 bold")
label8.place(x=400, y=200)

e7 = Entry(window)
e7.place(x=500, y=200)

label9 = Label(window, text="Bag of Pretzels: $2.99", font="times= 10 bold")
label9.place(x=400, y=250)

e8 = Entry(window)
e8.place(x=540, y=250)

b1 = Button(window, text="Check Out", width=20, command=calc_bill)
b1.place(x=260, y=300)

label9 = Label(window, text="Your Total is: ", font="times= 10 bold")
label9.place(x=200, y=350)

window.mainloop()

store_options = {"Bread": 2.99, "Turkey": 3.99, "Apple": 1.00, "Onion": 0.50,
                 "Olive Oil": 5.00, "Flank Steak": 12.00, "Salmon": 8.00,
                 "Bag of Pretzels": 1.99}
total = 0

for key in store_options:
    num_of_items = random.randrange(0, 6)
    price_of_item = (store_options[key] * num_of_items)
    if num_of_items % 2 == 0:
        price_of_item = round(price_of_item * 0.50, 2)
    total += price_of_item
    total = round(total, 2)
    print("Your list contains " + str(num_of_items) + " " + key +
          " at a price of " + str(price_of_item))

print("The total cost of your shopping trip is " + str(total))