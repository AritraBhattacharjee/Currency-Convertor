import requests
from tkinter import *
import tkinter as tk



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
