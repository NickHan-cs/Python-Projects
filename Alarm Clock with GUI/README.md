# README

## 1. Introduction

This is a python project - Alarm Clock with GUI, which can alert us at the setting time.

这是一个python项目——带GUI的闹钟，它可以在设定的时间警告我们。

## 2. How to use

First, users can run the file named AlarmClockWithGUI.py:

首先，用户可以运行这个名为AlarmClockWithGUI.py的文件

```
python AlarmClockWithGUI.py
```

Then, users would get a display window for input as shown below. Users can input the Alarm Time in 24 hour format and click the Set Alarm button. When the setting time is up, it would play the wav file we prepared before. In this project, we prepared a wav file called AlarmClock.wav for users.

然后，用户会得到一个展示窗口用来输入，如下图所示。用户可以设置闹铃的24小时制的时间，并单击Set Alarm按钮。当到达设定的时间时，它会播放我们提前准备的wav文件。在这个项目中，我们为用户准备了一个名为AlarmClock.wav的wav文件。

![GUI.png](https://i.loli.net/2020/08/19/9IkEYiOleJK4SQB.png)

## 3. How to develop

First, we need to define a function named alarm which takes the argument of (set_alarm_timer). `time.sleep(1)` halts the execution of the further commands given for 1 second, which makes the program check whether the current time equals to the setting time every second. Using `datetime.datetime.now()` can get the current time. Besides, `strftime()` can convert the current time into the format like "%H:%M:%S". `winsound.PlaySound("AlarmClock.wav", winsound.SND_ASYNC)` plays the wav file as soon the condition satisfies.

首先，我们需要定义一个名为alarm的函数，参数为set_alarm_timer。`time.sleep(1)`暂停执行指令1秒钟，这使得程序可以每一秒都检查当前的时间是否等于设定的时间。使用`datetime.datetime.now()` 可以得到当前的时间。另外，`strftime()`可以把当前的时间转换为"%H:%M:%s"的格式。`winsound.PlaySound("AlarmClock.wav", winsound.SND_ASYNC)` 会播放wav文件一旦条件满足。

We also need to define another function named setAlarm() which takes in the user value for setting the alarm.

我们还需要定义一个名为setAlarm()的函数，用来接收用户设置闹铃的值。

```python
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
```

Finally, we need to create GUI using tkinter. Python when combined with Tkinter provides a fast and easy way to create GUI appilications. Users can search how to create GUI using tkinter on the Internet if users would like to know the details.

最后，我们需要去创建一个GUI通过tkinter。Python的Tkinter提供了一种快速又方便的方法来创建GUI应用。用户如果想知道如何使用tkinter创建GUI，可以上网搜索细节。

```python
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")  # size of GUI
tips_label = Label(clock, text="Tips: enter time in 24 hour format!",
                   fg="red", font="Times").place(x=60, y=120)
# fg-color of text
units_label = Label(clock, text=" Hour   Minute   Second", font=60).place(x=120)
alarmTime_label = Label(clock, text="Alarm Time",
                        fg="blue", relief="solid", font=("Helevetica", 11, "bold")).place(x=5, y=29)
# relief-style of border
hour = StringVar()
minute = StringVar()
second = StringVar()
hour_entry = Entry(clock, textvariable=hour, bg="pink", width=9).place(x=110, y=30)
# bg - background color of entry
minute_entry = Entry(clock, textvariable=minute, bg="pink", width=9).place(x=180, y=30)
second_entry = Entry(clock, textvariable=second, bg="pink", width=9).place(x=250, y=30)
setAlarm_Button = Button(clock, text="Set Alarm", fg="red", width=10, command=setAlarm).place(x=110, y=70)
clock.mainloop()
```

