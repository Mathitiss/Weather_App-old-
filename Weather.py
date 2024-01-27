from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import ImageTk, Image

# Окно
root = Tk()
root.title('Weather App')
root.geometry('1280x712')
root.resizable(False, False)

root.iconbitmap('C:/Users/egorm/PycharmProjects/WeatherApp/Photos/WeatherSearhGlass_2.png')
root.config(bg='White')

def getWeather():
    city=search_text.get()

    geolocator=Nominatim(user_agent='geoapiExercises')
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime('%I:%M %p')
    clock.config(text=current_time)

    # Погода
    api='https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=6ba1c340e0a06c4505a5c73a4367c1bd'

    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-272.15)

    t.config(text=(temp,'°C'))
    c.config(text=condition)

# Поисковая строка
my_image = ImageTk.PhotoImage(Image.open('C:/Users/egorm/PycharmProjects/WeatherApp/Photos/SearchBar.png'))
my_label = Label(image=my_image)
my_label.pack()
my_label.place(x=20, y=20)

search_text = tk.Entry(root, justify='center', width=23, font=('poppins',25,'bold'), bg='white', border=0, fg='black')
search_text.place(x=50, y=35)
search_text.focus()

# Лупа
loopa_icon = PhotoImage(file='C:/Users/egorm/PycharmProjects/WeatherApp/Photos/WeatherSearhGlass_2.png')
loopa_button = Button(image=loopa_icon, borderwidth=0, cursor='hand2', bg='white', border=0, command=getWeather)
loopa_button.place(x=520, y=20)

# Логотип
logo_image = PhotoImage(file='C:/Users/egorm/PycharmProjects/WeatherApp/Photos/WeatherLogo.png')
logo = Label(image=logo_image, border=0, background="white")
logo.place(x=650, y=80)
search_text.focus()

# Задний фон
info_bar = ImageTk.PhotoImage(Image.open('C:/Users/egorm/PycharmProjects/WeatherApp/Photos/InfoBar.png'))
bar_image = Label(image=info_bar, border=0, background="white")
bar_image.place(x=60, y=155)

# Время
name=Label(root,font=('poppins',20,'bold'), border=0, fg='white', bg='#4361ee')
name.place(x=80, y=530)
clock=Label(root,font=('Helvetica',40,'bold'), border=0, fg='white', bg='#4361ee')
clock.place(x=136, y=560)

# Информация (темпа, описание, время)
t=Label(font=('arial',50,'bold'), border=0, fg='white', bg='#4361ee')
t.place(x=165,y=245)
c=Label(font=('arial',50,'bold'), border=0, fg='white', bg='#4361ee')
c.place(x=150,y=390)

temp=Label(root, text='Temperature:', font=('poppins',20,'bold'), border=0, fg='white', bg='#4361ee')
temp.place(x=80, y=200)
descrip=Label(root, text='Description:', font=('poppins',20,'bold'), border=0, fg='white', bg='#4361ee')
descrip.place(x=80, y=350)
curr_time=Label(root, text='Current Time:', font=('poppins',20,'bold'), border=0, fg='white', bg='#4361ee')
curr_time.place(x=80, y=500)

# Вкл/Выкл
root.mainloop()