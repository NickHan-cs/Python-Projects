import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk


class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        amount = round(amount / self.currencies[from_currency] * self.currencies[to_currency], 4)
        return amount


class CurrencyConverterUI(tk.Tk):
    def __init__(self, currency_converter):
        tk.Tk.__init__(self)
        self.title('Currency Converter')
        self.currency_converter = currency_converter
        self.geometry("500x200")
        self.intro_label = Label(self, text='Welcome to Real Time Currency Converter',
                                 fg='blue', relief=tk.RAISED, borderwidth=3, font=('Courier', 15, 'bold'))
        self.intro_label.place(x=10, y=5)
        self.date_label = Label(self, text=f"1 USD = {self.currency_converter.convert('USD', 'CNY', 1)} CNY \n "
                                           f"Date : {self.currency_converter.data['date']}",
                                relief=tk.GROOVE, borderwidth=5)
        self.date_label.place(x=160, y=50)
        # the frame of GUI
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_entry = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid,
                                  width=20)
        self.amount_entry.place(x=28, y=150)
        # the entry for amount
        self.converted_amount_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE,
                                            justify=tk.CENTER, width=20, borderwidth=3)
        self.converted_amount_label.place(x=338, y=150)
        # the label for converted amount
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("USD")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set('CNY')
        font = ('Courier', 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.currency_converter.currencies.keys()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)
        self.from_currency_dropdown.place(x=30, y=120)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.currencies.keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown.place(x=340, y=120)
        self.convert_button = Button(self, text='Convert', fg='black', command=self.perform,
                                     font=('Courier', 10, 'bold'))
        self.convert_button.place(x=225, y=135)

    def perform(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_variable.get()
        to_currency = self.to_currency_variable.get()
        converted_amount = round(self.currency_converter.convert(from_currency, to_currency, amount), 2)
        self.converted_amount_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string == "" or (string.count('.') <= 1) and result is not None


url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)
CurrencyConverterUI(converter)
mainloop()
