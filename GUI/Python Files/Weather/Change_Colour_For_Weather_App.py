from tkinter import *
from PIL import ImageTk,Image
import requests
import json


root = Tk()
root.title("Weather")
root.iconbitmap("Pictures\weather.ico")
#root.geometry("400x40")

myLabel = Label(root)
myLabel.grid(row=0, column=0, columnspan=2)

def zipLookup():
    global myLabel
    myLabel.destroy()
    zipcode = zip.get()
    #Label(root, text = zipcode).grid(row=1, column=0, columnspan=2)
    
    try:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ str(zipcode) +"&distance=5&API_KEY=3EA2882D-D5D1-4110-BF97-2DE79E5B7E75")
        api = json.loads(api_request.content)
        City = api[0]["ReportingArea"]
        Quality =api[0]["AQI"]
        Category = api[0]["Category"]["Name"]
        
        if Category == "Good":
            weather_colour = "#0C0"  #Green
        elif Category == "Moderate":
            weather_colour = "#FFFF00" #Yellow
        elif Category == "Unhealthy for Sensitive Groups":
            weather_colour = "#ff9900" #Orange
        elif Category == "Unhealthy":
            weather_colour = "#FF0000" #Red
        elif Category == "Very Unhealthy":
            weather_colour = "#990066" #Purple
        elif Category == "Hazarddous":
            weather_colour ="#660000" #Maroon
        
        root.configure(background=weather_colour)    
        myLabel = Label(root, text=City + " Air Quality " + str(Quality) + " " + Category, font=("Helvetica", 20), background=weather_colour)
        myLabel.grid(row=1, column=0, columnspan=2)
        
    except Exception as e:
        api = "Error..."

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=3EA2882D-D5D1-4110-BF97-2DE79E5B7E75

zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(root, text = "Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, sticky=W+E)

root.mainloop()