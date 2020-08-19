from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("AlarmClock.wav", winsound.SND_ASYNC)
            break


def setAlarm():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
tips_label = Label(clock, text="Tips: enter time in 24 hour format!",
                   fg="red", font="Times").place(x=60, y=120)
units_label = Label(clock, text=" Hour   Minute   Second", font=60).place(x=120)
alarmTime_label = Label(clock, text="Alarm Time",
                        fg="blue", relief="solid", font=("Helevetica", 11, "bold")).place(x=5, y=29)
hour = StringVar()
minute = StringVar()
second = StringVar()
hour_entry = Entry(clock, textvariable=hour, bg="pink", width=9).place(x=110, y=30)
minute_entry = Entry(clock, textvariable=minute, bg="pink", width=9).place(x=180, y=30)
second_entry = Entry(clock, textvariable=second, bg="pink", width=9).place(x=250, y=30)
setAlarm_Button = Button(clock, text="Set Alarm", fg="red", width=10, command=setAlarm).place(x=110, y=70)
clock.mainloop()
