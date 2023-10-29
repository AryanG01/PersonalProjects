MonthConversion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : 'April',
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    'Oct' : 'October',
    "Nov" : "November",
    "Dec" : "December"
}
print('Jan' in MonthConversion)
print(MonthConversion['Jan'])
print(MonthConversion.get("Dec" , "Not a Valid Key"))
print(MonthConversion.get("Luv" , "Not a Valid Key")) #Can give a default value if value is not in dictonary
