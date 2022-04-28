
"""
    Author: Aritra Bhattacharjee
    Date of Working: 27.04.2022 to 28.04.2022
    Tech Stack: Python, Tkinter.
    About: A python based currency convertor app.
"""
from tkinter import *
import currency_convertor
from tkinter import ttk
class Currency_Convertor_UIX(Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Convertor")
        self.convertor = currency_convertor.RealTimeCurrencyConverter()
        self.geometry("700x500")

        # Intro Label
        self.label = Label(self,text="Welcome to Currency Convertor",borderwidth=3,relief=RAISED,bg='blue',fg='white',font=('Courier',20,'bold'))
        # self.label.place(x=10,y=5)
        self.label.pack(fill=X,pady=10)

        font = ('Courier',15,'bold')
        self.amount_field = Entry(self,bd=3,relief=RIDGE,justify=CENTER,font=font)
        self.converted_field = Label(self,text='',fg='black',bg='white',relief=RIDGE,width=17,borderwidth=3,font = font)

        # drop down
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR")
        self.to_currency_variable =StringVar(self)
        self.to_currency_variable.set("USD")
        
        self.option_add('*TCombobox*Listbox.font',font)

        self.from_currency_dropdown = ttk.Combobox(self,textvariable=self.from_currency_variable,values=list(self.convertor.currencies.keys()),font=font,justify=CENTER,state='readonly')

        self.to_currency_dropdown = ttk.Combobox(self,textvariable=self.to_currency_variable,values=list(self.convertor.currencies.keys()),font=font,justify=CENTER,state='readonly')


        # placing the dropdown and the field
        self.from_currency_dropdown.place(x=20,y=170)
        self.amount_field.place(x=20,y=220)
        self.to_currency_dropdown.place(x=400,y=170)
        self.converted_field.place(x=400,y=220)

        # Button to convert currency
        self.convert_button = Button(self,text="Convert",fg="black",command=self.perform)
        self.convert_button.config(font=font)
        self.convert_button.place(x=290,y=250)


        # curr1 = self.from_currency_variable.get()
        # curr2 = self.to_currency_variable.get()

        # self.label2 = Label(self,text=f"1 {curr1} = {self.convertor.convert(curr1,curr2,1)} {curr2} \n Date : {self.convertor.data['date']}",relief=GROOVE,borderwidth=5,font=('Courier',20,'bold'),bg='grey',fg='black')
        # self.label2.pack(pady=10)
    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.convertor.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount,3)

        self.converted_field.config(text=str(converted_amount))
    # def test(self):
        # curr1 = from_curr
        # self.label2 = Label(self,text=f"1 Indian Rupee = {self.convertor.convert('INR','USD',1)} USD \n Date : {self.convertor.data['date']}",relief=GROOVE,borderwidth=5,font=('Courier',20,'bold'),bg='grey',fg='black')
        # self.label2.pack(pady=10)

if __name__ == '__main__':
    obj = Currency_Convertor_UIX()
    # obj.test()
    obj.mainloop()
