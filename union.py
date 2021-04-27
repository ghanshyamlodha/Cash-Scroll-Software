from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox

w=Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500,mode='determinate')

def  mainFrame():
    window = Tk()
    window.geometry("435x420+10+50")
    window.title("Union Bank")
    window.resizable(0, 0)
    photo = PhotoImage(file="ulogo.png")
    window.iconphoto(False, photo)

    qe1 = StringVar(window, value='00')
    qe2 = StringVar(window, value='00')
    qe3 = StringVar(window, value='00')
    qe4 = StringVar(window, value='00')
    qe5 = StringVar(window, value='00')
    qe6 = StringVar(window, value='00')
    qe7 = StringVar(window, value='00')
    qe8 = StringVar(window, value='00')
    qe9 = StringVar(window, value='00')
    qe10 = StringVar(window, value='00')
    qe11 = StringVar(window, value='00')
    qe12 = StringVar(window, value='00')
    qe13 = StringVar(window, value='00')
    qe14 = StringVar(window, value='00')
    qe15 = StringVar(window, value='00')
    head_total_qe = StringVar(window, value='00')

    aqe1 = StringVar(window, value='00')
    aqe2 = StringVar(window, value='00')
    aqe3 = StringVar(window, value='00')
    aqe4 = StringVar(window, value='00')
    aqe5 = StringVar(window, value='00')
    aqe6 = StringVar(window, value='00')
    aqe7 = StringVar(window, value='00')
    aqe8 = StringVar(window, value='00')
    aqe9 = StringVar(window, value='00')
    aqe10 = StringVar(window, value='00')
    aqe11 = StringVar(window, value='00')
    aqe12 = StringVar(window, value='00')
    aqe13 = StringVar(window, value='00')
    aqe14 = StringVar(window, value='00')
    aqe15 = StringVar(window, value='00')
    head_total_aq = StringVar(window, value='00')

    def deposit():
        top = Toplevel()
        top.geometry("435x420+455+50")
        top.title("Deposit")
        top.resizable(0, 0)
        photo1 = PhotoImage(file="ulogo.png")
        top.iconphoto(False, photo1)

        d_qe1 = StringVar(top, value=00)
        d_qe2 = StringVar(top, value=00)
        d_qe3 = StringVar(top, value=00)
        d_qe4 = StringVar(top, value=00)
        d_qe5 = StringVar(top, value=00)
        d_qe6 = StringVar(top, value=00)
        d_qe7 = StringVar(top, value=00)
        d_qe8 = StringVar(top, value=00)
        d_qe9 = StringVar(top, value=00)
        d_qe10 = StringVar(top, value=00)
        d_qe11 = StringVar(top, value=00)
        d_qe12 = StringVar(top, value=00)
        d_qe13 = StringVar(top, value=00)
        d_qe14 = StringVar(top, value=00)
        d_qe15 = StringVar(top, value=00)
        d_head_total_qe = StringVar(top, value=00)

        d_aqe1 = StringVar(top, value=00)
        d_aqe2 = StringVar(top, value=00)
        d_aqe3 = StringVar(top, value=00)
        d_aqe4 = StringVar(top, value=00)
        d_aqe5 = StringVar(top, value=00)
        d_aqe6 = StringVar(top, value=00)
        d_aqe7 = StringVar(top, value=00)
        d_aqe8 = StringVar(top, value=00)
        d_aqe9 = StringVar(top, value=00)
        d_aqe10 = StringVar(top, value=00)
        d_aqe11 = StringVar(top, value=00)
        d_aqe12 = StringVar(top, value=00)
        d_aqe13 = StringVar(top, value=00)
        d_aqe14 = StringVar(top, value=00)
        d_aqe15 = StringVar(top, value=00)
        d_head_total_aq = StringVar(top, value=00)

        def addQuantityDeposit():
            d_e1 = int(d_qe1.get())
            d_dump_aqe1 = 2000 * d_e1
            d_aqe1.set(d_dump_aqe1)

            d_e2 = int(d_qe2.get())
            d_dump_aqe2 = 500 * d_e2
            d_aqe2.set(d_dump_aqe2)

            d_e3 = int(d_qe3.get())
            d_dump_aqe3 = 200 * d_e3
            d_aqe3.set(d_dump_aqe3)

            d_e4 = int(d_qe4.get())
            d_dump_aqe4 = 100 * d_e4
            d_aqe4.set(d_dump_aqe4)

            d_e5 = int(d_qe5.get())
            d_dump_aqe5 = 50 * d_e5
            d_aqe5.set(d_dump_aqe5)

            d_e6 = int(d_qe6.get())
            d_dump_aqe6 = 20 * d_e6
            d_aqe6.set(d_dump_aqe6)

            d_e7 = int(d_qe7.get())
            d_dump_aqe7 = 10 * d_e7
            d_aqe7.set(d_dump_aqe7)

            d_e8 = int(d_qe8.get())
            d_dump_aqe8 = 5 * d_e8
            d_aqe8.set(d_dump_aqe8)

            d_e9 = int(d_qe9.get())
            d_dump_aqe9 = 2 * d_e9
            d_aqe9.set(d_dump_aqe9)

            d_e10 = int(d_qe10.get())
            d_dump_aqe10 = 1 * d_e10
            d_aqe10.set(d_dump_aqe10)

            d_e11 = int(d_qe11.get())
            d_dump_aqe11 = 20 * d_e11
            d_aqe11.set(d_dump_aqe11)

            d_e12 = int(d_qe12.get())
            d_dump_aqe12 = 10 * d_e12
            d_aqe12.set(d_dump_aqe12)

            d_e13 = int(d_qe13.get())
            d_dump_aqe13 = 5 * d_e13
            d_aqe13.set(d_dump_aqe13)

            d_e14 = int(d_qe14.get())
            d_dump_aqe14 = 2 * d_e14
            d_aqe14.set(d_dump_aqe14)

            d_e15 = int(d_qe15.get())
            d_dump_aqe15 = 2 * d_e15
            d_aqe15.set(d_dump_aqe15)

            d_result_q = d_e1 + d_e2 + d_e3 + d_e4 + d_e5 + d_e6 + d_e7 + d_e8 + d_e9 + d_e10 + d_e11 + d_e12 + d_e13 + d_e14 + d_e15
            d_result_qa = d_dump_aqe1 + d_dump_aqe2 + d_dump_aqe3 + d_dump_aqe4 + d_dump_aqe5 + d_dump_aqe6 + d_dump_aqe7 + d_dump_aqe8 + d_dump_aqe9 + d_dump_aqe10 + d_dump_aqe11 + d_dump_aqe12 + d_dump_aqe13 + d_dump_aqe14 + d_dump_aqe15
            d_head_total_qe.set(d_result_q)
            d_head_total_aq.set(d_result_qa)


        def bankDeposit():

            if int(d_qe1.get()):
                bd_qe1 = int(qe1.get()) + int(d_qe1.get())
                qe1.set(bd_qe1)
                aq_bd_aq1 = 2000 * bd_qe1
                aqe1.set(aq_bd_aq1)
            else:
                bd_qe1 = int(qe1.get()) + 0
                aq_bd_aq1 = 2000 * bd_qe1

            if int(d_qe2.get()):
                bd_qe2 = int(qe2.get()) + int(d_qe2.get())
                qe2.set(bd_qe2)
                aq_bd_aq2 = 500 * bd_qe2
                aqe2.set(aq_bd_aq2)
            else:
                bd_qe2 = int(qe2.get()) + 0
                aq_bd_aq2 = 500 * bd_qe2

            if int(d_qe3.get()):
                bd_qe3 = int(qe3.get()) + int(d_qe3.get())
                qe3.set(bd_qe3)
                aq_bd_aq3 = 200 * bd_qe3
                aqe3.set(aq_bd_aq3)
            else:
                bd_qe3 = int(qe3.get()) + 0
                aq_bd_aq3 = 200 * bd_qe3

            if int(d_qe4.get()):
                bd_qe4 = int(qe4.get()) + int(d_qe4.get())
                qe4.set(bd_qe4)
                aq_bd_aq4 = 100 * bd_qe4
                aqe4.set(aq_bd_aq4)
            else:
                bd_qe4 = int(qe4.get()) + 0
                aq_bd_aq4 = 100 * bd_qe4

            if int(d_qe5.get()):
                bd_qe5 = int(qe5.get()) + int(d_qe5.get())
                qe5.set(bd_qe5)
                aq_bd_aq5 = 50 * bd_qe5
                aqe5.set(aq_bd_aq5)
            else:
                bd_qe5 = int(qe5.get()) + 0
                aq_bd_aq5 = 50 * bd_qe5

            if int(d_qe6.get()):
                bd_qe6 = int(qe6.get()) + int(d_qe6.get())
                qe6.set(bd_qe6)
                aq_bd_aq6 = 20 * bd_qe6
                aqe6.set(aq_bd_aq6)
            else:
                bd_qe6 = int(qe6.get()) + 0
                aq_bd_aq6 = 20 * bd_qe6

            if int(d_qe7.get()):
                bd_qe7 = int(qe7.get()) + int(d_qe7.get())
                qe7.set(bd_qe7)
                aq_bd_aq7 = 10 * bd_qe7
                aqe7.set(aq_bd_aq7)
            else:
                bd_qe7 = int(qe7.get()) + 0
                aq_bd_aq7 = 10 * bd_qe7

            if int(d_qe8.get()):
                bd_qe8 = int(qe8.get()) + int(d_qe8.get())
                qe8.set(bd_qe8)
                aq_bd_aq8 = 5 * bd_qe8
                aqe8.set(aq_bd_aq8)
            else:
                bd_qe8 = int(qe8.get()) + 0
                aq_bd_aq8 = 5 * bd_qe8

            if int(d_qe9.get()):
                bd_qe9 = int(qe9.get()) + int(d_qe9.get())
                qe9.set(bd_qe9)
                aq_bd_aq9 = 2 * bd_qe9
                aqe9.set(aq_bd_aq9)
            else:
                bd_qe9 = int(qe9.get()) + 0
                aq_bd_aq9 = 2 * bd_qe9

            if int(d_qe10.get()):
                bd_qe10 = int(qe10.get()) + int(d_qe10.get())
                qe10.set(bd_qe10)
                aq_bd_aq10 = 1 * bd_qe10
                aqe10.set(aq_bd_aq10)
            else:
                bd_qe10 = int(qe10.get()) + 0
                aq_bd_aq10 = 1 * bd_qe10

            if int(d_qe11.get()):
                bd_qe11 = int(qe11.get()) + int(d_qe11.get())
                qe11.set(bd_qe11)
                aq_bd_aq11 = 20 * bd_qe11
                aqe11.set(aq_bd_aq11)
            else:
                bd_qe11 = int(qe11.get()) + 0
                aq_bd_aq11 = 20 * bd_qe11

            if int(d_qe12.get()):
                bd_qe12 = int(qe12.get()) + int(d_qe12.get())
                qe12.set(bd_qe12)
                aq_bd_aq12 = 10 * bd_qe12
                aqe12.set(aq_bd_aq12)
            else:
                bd_qe12 = int(qe12.get()) + 0
                aq_bd_aq12 = 10 * bd_qe12

            if int(d_qe13.get()):
                bd_qe13 = int(qe13.get()) + int(d_qe13.get())
                qe13.set(bd_qe13)
                aq_bd_aq13 = 5 * bd_qe13
                aqe13.set(aq_bd_aq13)
            else:
                bd_qe13 = int(qe13.get()) + 0
                aq_bd_aq13 = 5 * bd_qe13

            if int(d_qe14.get()):
                bd_qe14 = int(qe14.get()) + int(d_qe14.get())
                qe14.set(bd_qe14)
                aq_bd_aq14 = 2 * bd_qe14
                aqe14.set(aq_bd_aq14)
            else:
                bd_qe14 = int(qe14.get()) + 0
                aq_bd_aq14 = 2 * bd_qe14

            if int(d_qe15.get()):
                bd_qe15 = int(qe15.get()) + int(d_qe15.get())
                qe15.set(bd_qe15)
                aq_bd_aq15 = 1 * bd_qe15
                aqe15.set(aq_bd_aq15)
            else:
                bd_qe15 = int(qe15.get()) + 0
                aq_bd_aq15 = 1 * bd_qe15

            total_bd_qe = bd_qe1 + bd_qe2 + bd_qe3 + bd_qe4 + bd_qe5 + bd_qe6 + bd_qe7 + bd_qe8 + bd_qe9 + bd_qe10 + bd_qe11 + bd_qe12 + bd_qe13 + bd_qe14 + bd_qe15
            total_bd_aq = aq_bd_aq1 + aq_bd_aq2 + aq_bd_aq3 + aq_bd_aq4 + aq_bd_aq5 + aq_bd_aq6 + aq_bd_aq7 + aq_bd_aq8 + aq_bd_aq9 + aq_bd_aq10 + aq_bd_aq11 + aq_bd_aq12 + aq_bd_aq13 + aq_bd_aq14 + aq_bd_aq15
            head_total_qe.set(total_bd_qe)
            head_total_aq.set(total_bd_aq)

            top.destroy()

        def clear():
            d_qe1.set("0")
            d_qe2.set("0")
            d_qe3.set("0")
            d_qe4.set("0")
            d_qe5.set("0")
            d_qe6.set("0")
            d_qe7.set("0")
            d_qe8.set("0")
            d_qe9.set("0")
            d_qe10.set("0")
            d_qe11.set("0")
            d_qe12.set("0")
            d_qe13.set("0")
            d_qe14.set("0")
            d_qe15.set("0")
            d_head_total_qe.set("0")

            d_aqe1.set("0")
            d_aqe2.set("0")
            d_aqe3.set("0")
            d_aqe4.set("0")
            d_aqe5.set("0")
            d_aqe6.set("0")
            d_aqe7.set("0")
            d_aqe8.set("0")
            d_aqe9.set("0")
            d_aqe10.set("0")
            d_aqe11.set("0")
            d_aqe12.set("0")
            d_aqe13.set("0")
            d_aqe14.set("0")
            d_aqe15.set("0")
            d_head_total_aq.set("0")

        d_head_A = Label(top, text=" Amount", fg='black', bg="SlateGray2", font='Arial 10 bold').grid(row=1, column=1)
        d_head_total_A = Label(top, text=" TOTAL", fg='black', bg="lime green", font='Arial 10 bold').grid(row=18,
                                                                                                           column=1)
        d_two_thousand = Label(top, text=" 2000", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=2, column=1)
        d_five_hundred = Label(top, text=" 500  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=3,
                                                                                                         column=1)
        d_two_hundred = Label(top, text=" 200  ", fg='black', bg="thistle1", font='Arial 10 bold', ).grid(row=4,
                                                                                                          column=1)
        d_one_hundred = Label(top, text=" 100  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=5, column=1)
        d_fifty = Label(top, text="  50  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=6, column=1)
        d_twenty = Label(top, text="   20  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=7, column=1)
        d_ten = Label(top, text="   10  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=8, column=1)
        d_five = Label(top, text="    5   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=9, column=1)
        d_two = Label(top, text="    2   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=10, column=1)
        d_one = Label(top, text="    1   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=11, column=1)
        d_coin = Label(top, text=" COIN ", fg='black', bg="goldenrod1", font='Arial 10 bold').grid(row=12, column=1)
        d_twenty_coin = Label(top, text="  20  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=13,
                                                                                                        column=1)
        d_ten_coin = Label(top, text="  10  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=14, column=1)
        d_five_coin = Label(top, text="   5   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=15, column=1)
        d_two_coin = Label(top, text="   2   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=16, column=1)
        d_one_coin = Label(top, text="   1   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=17, column=1)
        d_app_label = Label(top, text=" Application is Developed by GHANSHYAM LODHA (IET-DAVV)", fg='black', bg="PaleGoldenrod", font='Arial 10 bold').place(x=20, y=398)

        d_head_B = Label(top, text=" Quantity", fg='black', bg="SlateGray2", font='Arial 10 bold').grid(row=1, column=2)
        d_head_total_B = Entry(top, textvariable=d_head_total_qe, state='disabled', fg='black', bg="white",
                               font='Arial 10 bold', justify='center').grid(row=18, column=2)
        d_q1_entry = Entry(top, textvariable=d_qe1, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=2, column=2)
        d_q2_entry = Entry(top, textvariable=d_qe2, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=3, column=2)
        d_q3_entry = Entry(top, textvariable=d_qe3, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=4, column=2)
        d_q4_entry = Entry(top, textvariable=d_qe4, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=5, column=2)
        d_q5_entry = Entry(top, textvariable=d_qe5, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=6, column=2)
        d_q6_entry = Entry(top, textvariable=d_qe6, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=7, column=2)
        d_q7_entry = Entry(top, textvariable=d_qe7, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=8, column=2)
        d_q8_entry = Entry(top, textvariable=d_qe8, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=9, column=2)
        q9_entry = Entry(top, textvariable=d_qe9, fg='black', bg="peach puff", font='Arial 10 bold',
                         justify='center').grid(
            row=10, column=2)
        q10_entry = Entry(top, textvariable=d_qe10, fg='black', bg="peach puff", font='Arial 10 bold',
                          justify='center').grid(
            row=11, column=2)
        d_q11_entry = Entry(top, textvariable=d_qe11, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=13, column=2)
        d_q12_entry = Entry(top, textvariable=d_qe12, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=14, column=2)
        d_q13_entry = Entry(top, textvariable=d_qe13, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=15, column=2)
        d_q14_entry = Entry(top, textvariable=d_qe14, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=16, column=2)
        d_q15_entry = Entry(top, textvariable=d_qe15, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=17, column=2)

        d_head_C = Label(top, text="Amount X Quantity", fg='black', bg="SlateGray2", font='Arial 10 bold').grid(row=1,
                                                                                                                column=3)
        d_head_total_C = Entry(top, textvariable=d_head_total_aq, state='disable', fg='black', bg="white",
                               font='Arial 10 bold', justify='center').grid(row=18, column=3)
        d_aq1 = Entry(top, textvariable=d_aqe1, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=2, column=3)
        d_aq2 = Entry(top, textvariable=d_aqe2, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=3, column=3)
        d_aq3 = Entry(top, textvariable=d_aqe3, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=4, column=3)
        d_aq4 = Entry(top, textvariable=d_aqe4, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=5, column=3)
        d_aq5 = Entry(top, textvariable=d_aqe5, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=6, column=3)
        d_aq6 = Entry(top, textvariable=d_aqe6, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=7, column=3)
        d_aq7 = Entry(top, textvariable=d_aqe7, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=8, column=3)
        d_aq8 = Entry(top, textvariable=d_aqe8, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=9, column=3)
        d_aq9 = Entry(top, textvariable=d_aqe9, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=10, column=3)
        d_aq10 = Entry(top, textvariable=d_aqe10, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=11, column=3)
        d_aq11 = Entry(top, textvariable=d_aqe11, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=13, column=3)
        d_aq12 = Entry(top, textvariable=d_aqe12, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=14, column=3)
        d_aq13 = Entry(top, textvariable=d_aqe13, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=15, column=3)
        d_aq14 = Entry(top, textvariable=d_aqe14, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=16, column=3)
        d_aq15 = Entry(top, textvariable=d_aqe15, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=17, column=3)

        d_b1 = Button(top, text=" Calculate", fg='black', bg="light cyan", font='Arial 10 bold', width=9, height=7,
                      command=addQuantityDeposit).place(x=350, y=23)

        d_b2 = Button(top, text=" Deposit", command=bankDeposit, fg='black', bg="wheat2", font='Arial 10 bold', width=9,
                      height=7).place(x=350, y=148)

        d_b3 = Button(top, text="Clear", command=clear, bg="snow3", font='Arial 10 bold', width=9, height=7).place(
            x=350, y=273)

    def withdraw():
        top = Toplevel()
        top.geometry("435x420+900+50")
        top.title("Withdraw")
        top.resizable(0, 0)
        photo2 = PhotoImage(file="ulogo.png")
        top.iconphoto(False, photo2)

        w_qe1 = StringVar(top, value=00)
        w_qe2 = StringVar(top, value=00)
        w_qe3 = StringVar(top, value=00)
        w_qe4 = StringVar(top, value=00)
        w_qe5 = StringVar(top, value=00)
        w_qe6 = StringVar(top, value=00)
        w_qe7 = StringVar(top, value=00)
        w_qe8 = StringVar(top, value=00)
        w_qe9 = StringVar(top, value=00)
        w_qe10 = StringVar(top, value=00)
        w_qe11 = StringVar(top, value=00)
        w_qe12 = StringVar(top, value=00)
        w_qe13 = StringVar(top, value=00)
        w_qe14 = StringVar(top, value=00)
        w_qe15 = StringVar(top, value=00)
        w_head_total_qe = StringVar(top, value=00)

        w_aqe1 = StringVar(top, value=00)
        w_aqe2 = StringVar(top, value=00)
        w_aqe3 = StringVar(top, value=00)
        w_aqe4 = StringVar(top, value=00)
        w_aqe5 = StringVar(top, value=00)
        w_aqe6 = StringVar(top, value=00)
        w_aqe7 = StringVar(top, value=00)
        w_aqe8 = StringVar(top, value=00)
        w_aqe9 = StringVar(top, value=00)
        w_aqe10 = StringVar(top, value=00)
        w_aqe11 = StringVar(top, value=00)
        w_aqe12 = StringVar(top, value=00)
        w_aqe13 = StringVar(top, value=00)
        w_aqe14 = StringVar(top, value=00)
        w_aqe15 = StringVar(top, value=00)
        w_head_total_aq = StringVar(top, value=00)

        def addQuantityWithdraw():
            w_e1 = int(w_qe1.get())
            w_dump_aqe1 = 2000 * w_e1
            w_aqe1.set(w_dump_aqe1)

            w_e2 = int(w_qe2.get())
            w_dump_aqe2 = 500 * w_e2
            w_aqe2.set(w_dump_aqe2)

            w_e3 = int(w_qe3.get())
            w_dump_aqe3 = 200 * w_e3
            w_aqe3.set(w_dump_aqe3)

            w_e4 = int(w_qe4.get())
            w_dump_aqe4 = 100 * w_e4
            w_aqe4.set(w_dump_aqe4)

            w_e5 = int(w_qe5.get())
            w_dump_aqe5 = 50 * w_e5
            w_aqe5.set(w_dump_aqe5)

            w_e6 = int(w_qe6.get())
            w_dump_aqe6 = 20 * w_e6
            w_aqe6.set(w_dump_aqe6)

            w_e7 = int(w_qe7.get())
            w_dump_aqe7 = 10 * w_e7
            w_aqe7.set(w_dump_aqe7)

            w_e8 = int(w_qe8.get())
            w_dump_aqe8 = 5 * w_e8
            w_aqe8.set(w_dump_aqe8)

            w_e9 = int(w_qe9.get())
            w_dump_aqe9 = 2 * w_e9
            w_aqe9.set(w_dump_aqe9)

            w_e10 = int(w_qe10.get())
            w_dump_aqe10 = 1 * w_e10
            w_aqe10.set(w_dump_aqe10)

            w_e11 = int(w_qe11.get())
            w_dump_aqe11 = 20 * w_e11
            w_aqe11.set(w_dump_aqe11)

            w_e12 = int(w_qe12.get())
            w_dump_aqe12 = 10 * w_e12
            w_aqe12.set(w_dump_aqe12)

            w_e13 = int(w_qe13.get())
            w_dump_aqe13 = 5 * w_e13
            w_aqe13.set(w_dump_aqe13)

            w_e14 = int(w_qe14.get())
            w_dump_aqe14 = 2 * w_e14
            w_aqe14.set(w_dump_aqe14)

            w_e15 = int(w_qe15.get())
            w_dump_aqe15 = 1 * w_e15
            w_aqe15.set(w_dump_aqe15)

            w_result_q = w_e1 + w_e2 + w_e3 + w_e4 + w_e5 + w_e6 + w_e7 + w_e8 + w_e9 + w_e10 + w_e11 + w_e12 + w_e13 + w_e14 + w_e15
            w_result_qa = w_dump_aqe1 + w_dump_aqe2 + w_dump_aqe3 + w_dump_aqe4 + w_dump_aqe5 + w_dump_aqe6 + w_dump_aqe7 + w_dump_aqe8 + w_dump_aqe9 + w_dump_aqe10 + w_dump_aqe11 + w_dump_aqe12 + w_dump_aqe13 + w_dump_aqe14 + w_dump_aqe15
            w_head_total_qe.set(w_result_q)
            w_head_total_aq.set(w_result_qa)

        def bankWithdraw():

            if int(w_qe1.get()):
                bw_qe1 = int(qe1.get()) - int(w_qe1.get())
                if bw_qe1 < 0:
                    messagebox.showerror('Quantity','insufficient Quantity[2000] is %s' %(bw_qe1))
                else:
                    pass
                aq_bw_aq1 = 2000 * bw_qe1
                if aq_bw_aq1 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' %(aq_bw_aq1))
                else:
                    pass
            else:
                bw_qe1 = int(qe1.get()) - 0
                aq_bw_aq1 = 2000 * bw_qe1

             #------------------------------------------------------------

            if int(w_qe2.get()):
                bw_qe2 = int(qe2.get()) - int(w_qe2.get())
                if bw_qe2 < 0:
                    messagebox.showerror('Quantity','insufficient Quantity[500] %s' %(bw_qe2))
                else:
                    pass
                aq_bw_aq2 = 500 * bw_qe2
                if aq_bw_aq2 < 0:
                    messagebox.showerror('Amount','insufficient Amount %s' %(aq_bw_aq2))
                else:
                    pass
            else:
                bw_qe2 = int(qe2.get()) - 0
                aq_bw_aq2 = 500 * bw_qe2

            # -------------------------------------------------------------------------

            if int(w_qe3.get()):
                bw_qe3 = int(qe3.get()) - int(w_qe3.get())
                if bw_qe3 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[200] %s' % (bw_qe3))
                else:
                    pass
                aq_bw_aq3 = 200 * bw_qe3
                if aq_bw_aq3 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' %(aq_bw_aq3))
                else:
                    pass
            else:
                bw_qe3 = int(qe3.get()) - 0
                aq_bw_aq3 = 200 * bw_qe3

            #-------------------------------------------------------------------------

            if int(w_qe4.get()):
                bw_qe4 = int(qe4.get()) - int(w_qe4.get())
                if bw_qe4 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[100] %s' % (bw_qe4))
                else:
                    pass
                aq_bw_aq4 = 100 * bw_qe4
                if aq_bw_aq4 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq4))
                else:
                    pass
            else:
                bw_qe4 = int(qe4.get()) - 0
                aq_bw_aq4 = 100 * bw_qe4

            #-------------------------------------------------------------------------

            if int(w_qe5.get()):
                bw_qe5 = int(qe5.get()) - int(w_qe5.get())
                if bw_qe5 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[50] %s' % (bw_qe5))
                else:
                    pass
                aq_bw_aq5 = 50 * bw_qe5
                if aq_bw_aq5 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq5))
                else:
                    pass
            else:
                bw_qe5 = int(qe5.get()) - 0
                aq_bw_aq5 = 50 * bw_qe5

            # -------------------------------------------------------------------------

            if int(w_qe6.get()):
                bw_qe6 = int(qe6.get()) - int(w_qe6.get())
                if bw_qe6 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[20] %s' % (bw_qe6))
                else:
                    pass
                aq_bw_aq6 = 20 * bw_qe6
                if aq_bw_aq6 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq6))
                else:
                    pass
            else:
                bw_qe6 = int(qe6.get()) - 0
                aq_bw_aq6 = 20 * bw_qe6

            # -------------------------------------------------------------------------

            if int(w_qe7.get()):
                bw_qe7 = int(qe7.get()) - int(w_qe7.get())
                if bw_qe7 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[10] %s' % (bw_qe7))
                else:
                    pass
                aq_bw_aq7 = 10 * bw_qe7
                if aq_bw_aq7 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq7))
                else:
                    pass
            else:
                bw_qe7 = int(qe7.get()) - 0
                aq_bw_aq7 = 10 * bw_qe7

            # -------------------------------------------------------------------------

            if int(w_qe8.get()):
                bw_qe8 = int(qe8.get()) - int(w_qe8.get())
                if bw_qe8 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[5] %s' % (bw_qe8))
                else:
                    pass
                aq_bw_aq8 = 5 * bw_qe8
                if aq_bw_aq8 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq8))
                else:
                    pass
            else:
                bw_qe8 = int(qe8.get()) - 0
                aq_bw_aq8 = 5 * bw_qe8

            # -------------------------------------------------------------------------

            if int(w_qe9.get()):
                bw_qe9 = int(qe9.get()) - int(w_qe9.get())
                if bw_qe9 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[2] %s' % (bw_qe9))
                else:
                    pass
                aq_bw_aq9 = 2 * bw_qe9
                if aq_bw_aq9 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq9))
                else:
                    pass
            else:
                bw_qe9 = int(qe9.get()) - 0
                aq_bw_aq9 = 2 * bw_qe9

            # -------------------------------------------------------------------------

            if int(w_qe10.get()):
                bw_qe10 = int(qe10.get()) - int(w_qe10.get())
                if bw_qe10 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[1] %s' % (bw_qe10))
                else:
                    pass
                aq_bw_aq10 = 1 * bw_qe10
                if aq_bw_aq10 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq10))
                else:
                    pass
            else:
                bw_qe10 = int(qe10.get()) - 0
                aq_bw_aq10 = 1 * bw_qe10

            # -------------------------------------------------------------------------

            if int(w_qe11.get()):
                bw_qe11 = int(qe11.get()) - int(w_qe11.get())
                if bw_qe11 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[20] %s' % (bw_qe11))
                else:
                    pass
                aq_bw_aq11 = 20 * bw_qe11
                if aq_bw_aq11 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq11))
                else:
                    pass
            else:
                bw_qe11 = int(qe11.get()) - 0
                aq_bw_aq11 = 20 * bw_qe11

            # -------------------------------------------------------------------------

            if int(w_qe12.get()):
                bw_qe12 = int(qe12.get()) - int(w_qe12.get())
                if bw_qe12 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[10] %s' % (bw_qe12))
                else:
                    pass
                aq_bw_aq12 = 10 * bw_qe12
                if aq_bw_aq12 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq12))
                else:
                    pass
            else:
                bw_qe12 = int(qe12.get()) - 0
                aq_bw_aq12 = 10 * bw_qe12

            # -------------------------------------------------------------------------

            if int(w_qe13.get()):
                bw_qe13 = int(qe13.get()) - int(w_qe13.get())
                if bw_qe13 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[5] %s' % (bw_qe13))
                else:
                    pass
                aq_bw_aq13 = 5 * bw_qe13
                if aq_bw_aq13 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq13))
                else:
                    pass
            else:
                bw_qe13 = int(qe13.get()) - 0
                aq_bw_aq13 = 5 * bw_qe13

            # -------------------------------------------------------------------------

            if int(w_qe14.get()):
                bw_qe14 = int(qe14.get()) - int(w_qe14.get())
                if bw_qe14 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[2] %s' % (bw_qe14))
                else:
                    pass
                aq_bw_aq14 = 2 * bw_qe14
                if aq_bw_aq14 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq14))
                else:
                    pass
            else:
                bw_qe14 = int(qe14.get()) - 0
                aq_bw_aq14 = 2 * bw_qe14

            # -------------------------------------------------------------------------

            if int(w_qe15.get()):
                bw_qe15 = int(qe15.get()) - int(w_qe15.get())
                if bw_qe15 < 0:
                    messagebox.showerror('Quantity', 'insufficient Quantity[1] %s' % (bw_qe15))
                else:
                    pass
                aq_bw_aq15 = 1 * bw_qe15
                if aq_bw_aq15 < 0:
                    messagebox.showerror('Amount', 'insufficient Amount %s' % (aq_bw_aq15))
                else:
                    pass
            else:
                bw_qe15 = int(qe15.get()) - 0
                aq_bw_aq15 = 1 * bw_qe15

            # -------------------------------------------------------------------------

            if bw_qe1 < 0 or bw_qe2 < 0 or bw_qe3 < 0 or bw_qe4 < 0 or bw_qe5 < 0 or bw_qe6 < 0 or bw_qe7 < 0 or bw_qe8 < 0 or bw_qe9 < 0 or bw_qe10 < 0 or bw_qe11 < 0 or bw_qe12 < 0 or bw_qe13 < 0 or bw_qe14 < 0 or bw_qe15:
                top.destroy()
            else:
                qe1.set(bw_qe1)
                qe2.set(bw_qe2)
                qe3.set(bw_qe3)
                qe4.set(bw_qe4)
                qe5.set(bw_qe5)
                qe6.set(bw_qe6)
                qe7.set(bw_qe7)
                qe8.set(bw_qe8)
                qe9.set(bw_qe9)
                qe10.set(bw_qe10)
                qe11.set(bw_qe11)
                qe12.set(bw_qe12)
                qe13.set(bw_qe13)
                qe14.set(bw_qe14)
                qe15.set(bw_qe15)

                total_bw_qe = bw_qe1 + bw_qe2 + bw_qe3 + bw_qe4 + bw_qe5 + bw_qe6 + bw_qe7 + bw_qe8 + bw_qe9 + bw_qe10 + bw_qe11 + bw_qe12 + bw_qe13 + bw_qe14 + bw_qe15
                head_total_qe.set(total_bw_qe)

            if aq_bw_aq1 < 0 or aq_bw_aq2 < 0 or aq_bw_aq3 < 0 or aq_bw_aq4 < 0 or aq_bw_aq5 < 0 or aq_bw_aq6 < 0 or aq_bw_aq7 < 0 or aq_bw_aq8 < 0 or aq_bw_aq9 < 0 or aq_bw_aq10 < 0 or aq_bw_aq11 < 0 or aq_bw_aq12 < 0 or aq_bw_aq13 < 0 or aq_bw_aq14 < 0 or aq_bw_aq15:
                top.destroy()
            else:
                aqe1.set(aq_bw_aq1)
                aqe2.set(aq_bw_aq2)
                aqe3.set(aq_bw_aq3)
                aqe4.set(aq_bw_aq4)
                aqe5.set(aq_bw_aq5)
                aqe6.set(aq_bw_aq6)
                aqe7.set(aq_bw_aq7)
                aqe8.set(aq_bw_aq8)
                aqe9.set(aq_bw_aq9)
                aqe10.set(aq_bw_aq10)
                aqe11.set(aq_bw_aq11)
                aqe12.set(aq_bw_aq12)
                aqe13.set(aq_bw_aq13)
                aqe14.set(aq_bw_aq14)
                aqe15.set(aq_bw_aq15)

                total_bw_aq = aq_bw_aq1 + aq_bw_aq2 + aq_bw_aq3 + aq_bw_aq4 + aq_bw_aq5 + aq_bw_aq6 + aq_bw_aq7 + aq_bw_aq8 + aq_bw_aq9 + aq_bw_aq10 + aq_bw_aq11 + aq_bw_aq12 + aq_bw_aq13 + aq_bw_aq14 + aq_bw_aq15
                head_total_aq.set(total_bw_aq)

            #head_total_qe.set(total_bw_qe)
            #head_total_aq.set(total_bw_aq)

            top.destroy()

        def clear():
            w_qe1.set("0")
            w_qe2.set("0")
            w_qe3.set("0")
            w_qe4.set("0")
            w_qe5.set("0")
            w_qe6.set("0")
            w_qe7.set("0")
            w_qe8.set("0")
            w_qe9.set("0")
            w_qe10.set("0")
            w_qe11.set("0")
            w_qe12.set("0")
            w_qe13.set("0")
            w_qe14.set("0")
            w_qe15.set("0")
            w_head_total_qe.set("0")

            w_aqe1.set("0")
            w_aqe2.set("0")
            w_aqe3.set("0")
            w_aqe4.set("0")
            w_aqe5.set("0")
            w_aqe6.set("0")
            w_aqe7.set("0")
            w_aqe8.set("0")
            w_aqe9.set("0")
            w_aqe10.set("0")
            w_aqe11.set("0")
            w_aqe12.set("0")
            w_aqe13.set("0")
            w_aqe14.set("0")
            w_aqe15.set("0")
            w_head_total_aq.set("0")

        w_heaw_A = Label(top, text=" Amount", fg='black', bg="SlateGray2", font='Arial 10 bold').grid(row=1, column=1)
        w_heaw_total_A = Label(top, text=" TOTAL", fg='black', bg="lime green", font='Arial 10 bold').grid(row=18,
                                                                                                           column=1)
        w_two_thousand = Label(top, text=" 2000", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=2, column=1)
        w_five_hundred = Label(top, text=" 500  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=3,
                                                                                                         column=1)
        w_two_hundred = Label(top, text=" 200  ", fg='black', bg="thistle1", font='Arial 10 bold', ).grid(row=4,
                                                                                                          column=1)
        w_one_hundred = Label(top, text=" 100  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=5, column=1)
        w_fifty = Label(top, text="   50  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=6, column=1)
        w_twenty = Label(top, text="   20  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=7, column=1)
        w_ten = Label(top, text="   10  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=8, column=1)
        w_five = Label(top, text="    5   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=9, column=1)
        w_two = Label(top, text="    2   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=10, column=1)
        w_one = Label(top, text="    1   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=11, column=1)
        w_coin = Label(top, text=" COIN ", fg='black', bg="goldenrod1", font='Arial 10 bold').grid(row=12, column=1)
        w_twenty_coin = Label(top, text="  20  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=13,
                                                                                                        column=1)
        w_ten_coin = Label(top, text="  10  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=14, column=1)
        w_five_coin = Label(top, text="   5   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=15, column=1)
        w_two_coin = Label(top, text="   2   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=16, column=1)
        w_one_coin = Label(top, text="   1   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=17, column=1)
        w_app_label = Label(top, text=" Application is Developed by GHANSHYAM LODHA (IET-DAVV)", fg='black', bg="PaleGoldenrod", font='Arial 10 bold').place(x=20, y=398)

        w_heaw_B = Label(top, text=" Quantity", fg='black', bg="SlateGray2", font='Arial 10 bold').grid(row=1, column=2)
        w_heaw_total_B = Entry(top, textvariable=w_head_total_qe, state='disabled', fg='black', bg="white",
                               font='Arial 10 bold', justify='center').grid(row=18, column=2)
        w_q1_entry = Entry(top, textvariable=w_qe1, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=2, column=2)
        w_q2_entry = Entry(top, textvariable=w_qe2, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=3, column=2)
        w_q3_entry = Entry(top, textvariable=w_qe3, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=4, column=2)
        w_q4_entry = Entry(top, textvariable=w_qe4, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=5, column=2)
        w_q5_entry = Entry(top, textvariable=w_qe5, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=6, column=2)
        w_q6_entry = Entry(top, textvariable=w_qe6, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=7, column=2)
        w_q7_entry = Entry(top, textvariable=w_qe7, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=8, column=2)
        w_q8_entry = Entry(top, textvariable=w_qe8, fg='black', bg="peach puff", font='Arial 10 bold',
                           justify='center').grid(
            row=9, column=2)
        q9_entry = Entry(top, textvariable=w_qe9, fg='black', bg="peach puff", font='Arial 10 bold',
                         justify='center').grid(
            row=10, column=2)
        q10_entry = Entry(top, textvariable=w_qe10, fg='black', bg="peach puff", font='Arial 10 bold',
                          justify='center').grid(
            row=11, column=2)
        w_q11_entry = Entry(top, textvariable=w_qe11, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=13, column=2)
        w_q12_entry = Entry(top, textvariable=w_qe12, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=14, column=2)
        w_q13_entry = Entry(top, textvariable=w_qe13, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=15, column=2)
        w_q14_entry = Entry(top, textvariable=w_qe14, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=16, column=2)
        w_q15_entry = Entry(top, textvariable=w_qe15, fg='black', bg="peach puff", font='Arial 10 bold',
                            justify='center').grid(
            row=17, column=2)

        w_heaw_C = Label(top, text="Amount X Quantity", fg='black', bg="SlateGray2", font='Arial 10 bold').grid(row=1,
                                                                                                                column=3)
        w_heaw_total_C = Entry(top, textvariable=w_head_total_aq, state='disable', fg='black', bg="white",
                               font='Arial 10 bold', justify='center').grid(row=18, column=3)
        w_aq1 = Entry(top, textvariable=w_aqe1, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=2, column=3)
        w_aq2 = Entry(top, textvariable=w_aqe2, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=3, column=3)
        w_aq3 = Entry(top, textvariable=w_aqe3, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=4, column=3)
        w_aq4 = Entry(top, textvariable=w_aqe4, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=5, column=3)
        w_aq5 = Entry(top, textvariable=w_aqe5, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=6, column=3)
        w_aq6 = Entry(top, textvariable=w_aqe6, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=7, column=3)
        w_aq7 = Entry(top, textvariable=w_aqe7, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=8, column=3)
        w_aq8 = Entry(top, textvariable=w_aqe8, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=9, column=3)
        w_aq9 = Entry(top, textvariable=w_aqe9, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=10, column=3)
        w_aq10 = Entry(top, textvariable=w_aqe10, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=11, column=3)
        w_aq11 = Entry(top, textvariable=w_aqe11, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=13, column=3)
        w_aq12 = Entry(top, textvariable=w_aqe12, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=14, column=3)
        w_aq13 = Entry(top, textvariable=w_aqe13, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=15, column=3)
        w_aq14 = Entry(top, textvariable=w_aqe14, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=16, column=3)
        w_aq15 = Entry(top, textvariable=w_aqe15, state='disable', fg='black', bg="white", font='Arial 10 bold',
                       justify='center').grid(row=17, column=3)

        w_b1 = Button(top, text=" Calculate", fg='black', bg="light cyan", font='Arial 10 bold', width=9, height=7,
                      command=addQuantityWithdraw).place(x=350, y=23)
        w_b2 = Button(top, text="  Withdraw", command=bankWithdraw, fg='black', bg="wheat2", font='Arial 10 bold',
                      width=9, height=7).place(x=350, y=148)
        w_b3 = Button(top, text="Clear", command=clear, bg="snow3", font='Arial 10 bold', width=9, height=7).place(x=350, y=273)


    heaw_A = Label(window, text=" Amount", fg='black', bg="SlateGray2", font='Arial 10 bold').grid(row=1, column=1)
    heaw_total_A = Label(window, text=" TOTAL", fg='black', bg="lime green", font='Arial 10 bold').grid(row=18,
                                                                                                        column=1)
    two_thousand = Label(window, text=" 2000", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=2, column=1)
    five_hundred = Label(window, text=" 500  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=3, column=1)
    two_hundred = Label(window, text=" 200  ", fg='black', bg="thistle1", font='Arial 10 bold', ).grid(row=4, column=1)
    one_hundred = Label(window, text=" 100  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=5, column=1)
    fifty = Label(window, text="  50  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=6, column=1)
    twenty = Label(window, text="  20  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=7, column=1)
    ten = Label(window, text="  10  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=8, column=1)
    five = Label(window, text="   5   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=9, column=1)
    two = Label(window, text="   2   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=10, column=1)
    one = Label(window, text="   1   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=11, column=1)
    coin = Label(window, text=" COIN ", fg='black', bg="goldenrod1", font='Arial 10 bold').grid(row=12, column=1)
    twenty_coin = Label(window, text="  20  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=13, column=1)
    ten_coin = Label(window, text="  10  ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=14, column=1)
    five_coin = Label(window, text="   5   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=15, column=1)
    two_coin = Label(window, text="   2   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=16, column=1)
    one_coin = Label(window, text="   1   ", fg='black', bg="thistle1", font='Arial 10 bold').grid(row=17, column=1)
    app_label = Label(window, text=" Application is Developed by GHANSHYAM LODHA (IET-DAVV)", fg='black', bg="PaleGoldenrod", font='Arial 10 bold').place(x=20, y= 398)

    heaw_B = Label(window, text=" Quantity", fg='black', bg="SlateGray2", font='Arial 10 bold').grid(row=1, column=2)
    heaw_total_B = Entry(window, textvariable=head_total_qe, fg='black', bg="peach puff", font='Arial 10 bold',
                         state='disable', justify='center').grid(row=18, column=2)
    q1_entry = Entry(window, textvariable=qe1, state='disable', fg='black', bg="white", font='Arial 10 bold',
                     justify='center').grid(row=2, column=2)
    q2_entry = Entry(window, textvariable=qe2, state='disable', fg='black', bg="white", font='Arial 10 bold',
                     justify='center').grid(row=3, column=2)
    q3_entry = Entry(window, textvariable=qe3, state='disable', fg='black', bg="white", font='Arial 10 bold',
                     justify='center').grid(row=4, column=2)
    q4_entry = Entry(window, textvariable=qe4, state='disable', fg='black', bg="white", font='Arial 10 bold',
                     justify='center').grid(row=5, column=2)
    q5_entry = Entry(window, textvariable=qe5, state='disable', fg='black', bg="white", font='Arial 10 bold',
                     justify='center').grid(row=6, column=2)
    q6_entry = Entry(window, textvariable=qe6, state='disable', fg='black', bg="white", font='Arial 10 bold',
                     justify='center').grid(row=7, column=2)
    q7_entry = Entry(window, textvariable=qe7, state='disable', fg='black', bg="white", font='Arial 10 bold',
                     justify='center').grid(row=8, column=2)
    q8_entry = Entry(window, textvariable=qe8, state='disable', fg='black', bg="white", font='Arial 10 bold',
                     justify='center').grid(row=9, column=2)
    q9_entry = Entry(window, textvariable=qe9, state='disable', fg='black', bg="white", font='Arial 10 bold',
                     justify='center').grid(row=10, column=2)
    q10_entry = Entry(window, textvariable=qe10, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=11, column=2)
    q11_entry = Entry(window, textvariable=qe11, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=13, column=2)
    q12_entry = Entry(window, textvariable=qe12, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=14, column=2)
    q13_entry = Entry(window, textvariable=qe13, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=15, column=2)
    q14_entry = Entry(window, textvariable=qe14, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=16, column=2)
    q15_entry = Entry(window, textvariable=qe15, state='disable', fg='black', bg="white", font='Arial 10 bold',
                      justify='center').grid(row=17, column=2)

    heaw_C = Label(window, text="Amount X Quantity", fg='black', bg="SlateGray2", font='Arial 10 bold').grid(row=1,
                                                                                                             column=3)
    heaw_total_C = Entry(window, textvariable=head_total_aq, state='disable', fg='black', bg="white",
                         font='Arial 10 bold', justify='center').grid(row=18, column=3)
    aq1 = Entry(window, textvariable=aqe1, state='disable', fg='black', bg="white", font='Arial 10 bold',
                justify='center').grid(row=2, column=3)
    aq2 = Entry(window, textvariable=aqe2, state='disable', fg='black', bg="white", font='Arial 10 bold',
                justify='center').grid(row=3, column=3)
    aq3 = Entry(window, textvariable=aqe3, state='disable', fg='black', bg="white", font='Arial 10 bold',
                justify='center').grid(row=4, column=3)
    aq4 = Entry(window, textvariable=aqe4, state='disable', fg='black', bg="white", font='Arial 10 bold',
                justify='center').grid(row=5, column=3)
    aq5 = Entry(window, textvariable=aqe5, state='disable', fg='black', bg="white", font='Arial 10 bold',
                justify='center').grid(row=6, column=3)
    aq6 = Entry(window, textvariable=aqe6, state='disable', fg='black', bg="white", font='Arial 10 bold',
                justify='center').grid(row=7, column=3)
    aq7 = Entry(window, textvariable=aqe7, state='disable', fg='black', bg="white", font='Arial 10 bold',
                justify='center').grid(row=8, column=3)
    aq8 = Entry(window, textvariable=aqe8, state='disable', fg='black', bg="white", font='Arial 10 bold',
                justify='center').grid(row=9, column=3)
    aq9 = Entry(window, textvariable=aqe9, state='disable', fg='black', bg="white", font='Arial 10 bold',
                justify='center').grid(row=10, column=3)
    aq10 = Entry(window, textvariable=aqe10, state='disable', fg='black', bg="white", font='Arial 10 bold',
                 justify='center').grid(row=11, column=3)
    aq11 = Entry(window, textvariable=aqe11, state='disable', fg='black', bg="white", font='Arial 10 bold',
                 justify='center').grid(row=13, column=3)
    aq12 = Entry(window, textvariable=aqe12, state='disable', fg='black', bg="white", font='Arial 10 bold',
                 justify='center').grid(row=14, column=3)
    aq13 = Entry(window, textvariable=aqe13, state='disable', fg='black', bg="white", font='Arial 10 bold',
                 justify='center').grid(row=15, column=3)
    aq14 = Entry(window, textvariable=aqe14, state='disable', fg='black', bg="white", font='Arial 10 bold',
                 justify='center').grid(row=16, column=3)
    aq15 = Entry(window, textvariable=aqe15, state='disable', fg='black', bg="white", font='Arial 10 bold',
                 justify='center').grid(row=17, column=3)

    b1 = Button(window, text=" Deposit", command=deposit, fg='black', bg="wheat2", font='Arial 10 bold', width=9,
                height=11).place(x=350, y=25)

    b2 = Button(window, text="  Withdraw", command=withdraw, fg='black', bg="powder blue", font='Arial 10 bold',
                width=9, height=11).place(x=350, y=210)

    def exitApp():
        msg = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application', default='no')
        if msg == 'yes':
            window.destroy()
        else:
            pass

    window.protocol("WM_DELETE_WINDOW", exitApp)

    window.mainloop()


def bar():
    l4 = Label(w, text='Loading...', fg='white', bg=a)
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=190)

    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.03)
        r = r + 1

    w.destroy()
    mainFrame()


progress.place(x=-10, y=230)

#############
# frame 333333333333333333333333

'''

def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''
a = '#249794'
Frame(w, width=427, height=221, bg=a).place(x=0, y=0)  # 249794
b1 = Button(w, width=10, height=1, text='Get Started', command=bar, border=0, fg=a, bg='white')
b1.place(x=170, y=190)

######## Label
p1 = PhotoImage(file='rb.png')

l1 = Label(w, image=p1)
#lst1 = ('Calibri (Body)', 18, 'bold')
#l1.config(font=lst1)
l1.place(x=5, y=25)

'''
l2 = Label(w, text='BANK', fg='white', bg=a)
lst2 = ('Calibri (Body)', 18, 'bold')
l2.config(font=lst2)
l2.place(x=135, y=80)

l3 = Label(w, text='PROGRAMMED BY SHYAM', fg='white', bg=a)
lst3 = ('Calibri (Body)', 13)
l3.config(font=lst3)
l3.place(x=50, y=110)
'''

w.mainloop()


