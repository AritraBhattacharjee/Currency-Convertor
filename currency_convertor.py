"""
    Author: Aritra Bhattacharjee
    Date of Working: 27.04.2022 to 28.04.2022
    Tech Stack: Python, Tkinter.
    About: A python based currency convertor app.
"""
import requests
from tkinter import *
class RealTimeCurrencyConverter():
    def __init__(self):
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.data =  requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self,from_curr,to_curr,amount):
        initial_amount = amount
        if from_curr != 'USD':
            amount = amount/self.currencies[from_curr]
        amount = round(amount*self.currencies[to_curr],4)

        return amount

if __name__=='__main__':

    convertor = RealTimeCurrencyConverter()
    print(convertor.convert('INR','USD',100))
