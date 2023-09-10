from tkinter import *
from functools import partial
from tkinter import messagebox
import random
from tkinter import font


# ------ CONSTANTS -------
DEEPBLUE = "#27374D"
LIGHTBLUE = "#ADD8E6"
LIGHTRED = "#FFCCCB"
GREY = "#9DB2BF"
OFFWHITE = "#DDE6ED"


# ------- UI SETUP -------
window = Tk()
window.title("My window")
window.minsize(height=650, width=500)
window.config(padx=50, pady=50, background=OFFWHITE)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=OFFWHITE, )
#lock_img = PhotoImage(file="img.jpg")
#canvas.create_image(10, 10, image=lock_img)

Label(text="The Python Restaurant",height=5, width=50, font = font.Font(size = 30), bg= "#97FFF4").grid(row=0, column=1)

global food
foods = ["DOSA - ₹60",
         "VADA SAMOSA - ₹50",
         "IDLI - ₹80",
         "VEG MEAL - ₹150",
         "NON-VEG MEAL - ₹300",
         "PANEER ROLL - ₹80",
         "EGG-CHICKEN ROLL - ₹140",
         "VEG-PIZZA - ₹150",
         "NON VEG-PIZZA - ₹200",
         "MASALA COLD DRINKS - ₹50"]
time = ["9am", "12pm", "2pm", "5pm", "6pm", "8pm", "10pm"]
delivery_time = ["10min", "15min", "20min", "30min", "45min"]
buttons = []
coupon_num = 0


def order_placement(x):
    global coupon_num
    a = messagebox.askokcancel("Order Confirmation",f"Estimated time for preparing {foods[x]}: \n{time[random.randint(0, len(time))]}")
    if a:
        coupon_num += 1
        b = messagebox.showinfo('Thank you for placing your order', f"Your order has been placed\nPlease come at the specified time to collect your food\nYour coupon number is {coupon_num}")


# Buttons
w = 30
h = 2
btn_1 = Button(text=foods[0], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 0))
btn_1.grid(column=1, row=2)
btn_2 = Button(text=foods[1], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 1))
btn_2.grid(column=1, row=3)
btn_3 = Button(text=foods[2], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 2))
btn_3.grid(column=1, row=4)
btn_4 = Button(text=foods[3], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 3))
btn_4.grid(column=1, row=5)
btn_5 = Button(text=foods[4], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 4))
btn_5.grid(column=1, row=6)
btn_6 = Button(text=foods[5], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 5))
btn_6.grid(column=1, row=7)
btn_7 = Button(text=foods[6], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 6))
btn_7.grid(column=1, row=8)
btn_8 = Button(text=foods[7], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 7))
btn_8.grid(column=1, row=9)
btn_9 = Button(text=foods[8], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 8))
btn_9.grid(column=1, row=10)
btn_10 = Button(text=foods[9], width=w, height=h, bg=LIGHTBLUE, command=partial(order_placement, 9))
btn_10.grid(column=1, row=11)


# labels
menu_label = Label(text="Menu", font=("Courier", 12), highlightthickness=0, pady=10, padx=10, bg=GREY)
menu_label.grid(column=1, row=1)



window.mainloop()
