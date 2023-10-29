from tkinter import *
from PIL import ImageTk,Image
import requests
import json


root = Tk()
root.title("Weather")
root.iconbitmap("Pictures\weather.ico")
root.geometry("400x40")
root.configure(background="Green")

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=3EA2882D-D5D1-4110-BF97-2DE79E5B7E75
#https://docs.airnowapi.org/CurrentObservationsByZip/query

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=3EA2882D-D5D1-4110-BF97-2DE79E5B7E75")
    api = json.loads(api_request.content)
    City = api[0]["ReportingArea"]
    Quality =api[0]["AQI"]
    Category = api[0]["Category"]["Name"]
except Exception as e:
    api = "Error..."

myLabel = Label(root, text=City + " Air Quality " + str(Quality) + " " + Category, font=("Helvetica", 20), background="Green")
myLabel.pack()

root.mainloop()