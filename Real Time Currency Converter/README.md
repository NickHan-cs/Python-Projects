# Real Time Currency Converter

## 1. Introduction

Now we build an python project through which users can convert currencies. This project contains the source code `RealTImeCurrencyConverter.py` and the executable file `Real Time Currency Converter.exe`.

现在我们要搭建一个python项目，用户可以通过它进行货币换算。这个项目包含了源代码`RealTImeCurrencyConverter.py`和可执行文件`Real Time Currency Converter.exe`。

## 2. How to use

First, users can double clicked the executable file `Real Time Currency Converter.exe` or run the python file `RealTImeCurrencyConverter.py`:

首先，用户可以双击可执行文件`Real Time Currency Converter.exe`或者运行python文件`RealTImeCurrencyConverter.py`：

```
python RealTimeCurrencyConverter.py
```

Then, users would get a GUI as shown below. Users can choose the currency **from** which they want to convert and the currency **to** which they want to convert. Finally, after users input how much amount they want to convert and click the convert button, the GUI would return the converted amount.

然后，用户会得到一个GUI，如下所示。用户可以选择要转换前的货币和要转换后的货币。最后，在用户输入多少钱他们想转换并单击转换键后，GUI会返回转换后的钱。

![GUI.png](https://i.loli.net/2020/08/20/uEiRMa3w9tgrUvG.png)

To get real-time exchange rates, we will use `https://api.exchangerate-api.com/v4/latest/USD`. Here, we can see the data in JSON format and the data is updated daily.

我们将使用`https://api.exchangerate-api.com/v4/latest/USD`得到实时的汇率。这里，我们可以看到JSON格式的数据，而且数据是每日更新的。

```json
{"base":"USD","date":"2020-08-20","time_last_updated":1597881845,"rates":{"USD":1,"AED":3.67197,"ARS":73.385253,"AUD":1.381089,"BGN":1.638614,"BRL":5.471277,"BSD":1,"CAD":1.316599,"CHF":0.907553,"CLP":795.422883,"CNY":6.91043,"COP":3791.571429,"CZK":21.879119,"DKK":6.238515,"DOP":58.161432,"EGP":15.873804,"EUR":0.839853,"FJD":2.13078,"GBP":0.758011,"GTQ":7.673766,"HKD":7.750344,"HRK":6.311087,"HUF":292.961239,"IDR":14982.732127,"ILS":3.400197,"INR":74.82318,"ISK":135.496277,"JPY":105.578077,"KRW":1180.487856,"KZT":416.874346,"MVR":15.4,"MXN":22.12844,"MYR":4.175044,"NOK":8.854416,"NZD":1.512055,"PAB":1,"PEN":3.564002,"PHP":48.546256,"PKR":167.981013,"PLN":3.676886,"PYG":7238.454545,"RON":4.054754,"RUB":73.308341,"SAR":3.750135,"SEK":8.656051,"SGD":1.364459,"THB":31.212026,"TRY":7.337302,"TWD":29.371934,"UAH":27.305766,"UYU":42.601926,"ZAR":17.235789}}
```

## 3. How to develop

First we will create the CurrencyConverter class which will get the real time exchange rate and convert the curreny and return the converted amount.

首先我们会创建CurrencyConverter类，可以得到实时汇率并换算货币，得到转换后的数量。

`requests.get(url)` load the page in our python program and then `.json()` will convert the page into the json file.

在我们的python程序中，`requests.get(url)`加载页面，并且`.json()`会把页面转换成json文件。

```python
class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        amount = round(amount / self.currencies[from_currency] * self.currencies[to_currency], 4)
        return amount
```

As for how to create a UI for the currency converter, users could read the python code of CurrencyConverterUI class.

至于如何创建一个货币换算器的UI，用户可以阅读CurrencyConverterUI类的python代码。