from tkinter import*
#tkinter is the python standard(gul) graphical user interface tool kit  
# which provide the tools  to create the desktop applications with window
from configparser import ConfigParser
#configparser is a bulit-in python module  it used 
# to handle the configuration files
from tkinter import messagebox
import requests
url_api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file="weather.key"
file_a=ConfigParser()
file_a.read(api_file)
api_key=file_a['api_key']["key"]



def weather_find(city):
    final=requests.get(url_api.format(city,api_key))
    if final:
        json_file=final.json()
        city=json_file['name']
        country_name=json_file['sys']['country']
        k_temp=json_file['main']['temp']
        c_temp=k_temp-273.5
        f_temp=(k_temp-273.5)*9/5+32
        weather_display=json_file['weather'][0]['main']
        result=(city,country_name,k_temp,c_temp,f_temp,weather_display)
        return result
    else:
        return None
def print_weather():
    city=search_city.get()
    weather=weather_find(city)
    if weather:
        location_entry['text']='{},{}'.format(weather[0],weather[1])
        temprature_entry['text']='{:.2f} c,{:.2f} F'.format(weather[2],weather[3])
        weather_entry['text']=weather[4]
    else:
        messagebox.showerror('error','please vaild coorect city')

root=Tk()
root.title("my own  weather app")
root .config(background="blue")
root.geometry("700x700")
search_city=StringVar()
enter_city=Entry(root, textvariable=search_city,fg="blue",font=("Arial",20,"bold"))
enter_city.pack()



search_button=Button(root,text="SEARCH WEATHER !",width=20,bg="red",fg="white",font=("Arial",20,"bold"),command=print_weather)
search_button.pack()



location_entry=Label(root,text="",font=("Arial",35,"bold",),bg="lightblue")
location_entry.pack()


temprature_entry=Label(root,text="",font=("Arial",35,"bold"),bg="lightpink")
temprature_entry.pack()



weather_entry=Label(root,text="",font=("Arial",35,"bold"),bg="lightgreen")
weather_entry.pack()

root.mainloop()