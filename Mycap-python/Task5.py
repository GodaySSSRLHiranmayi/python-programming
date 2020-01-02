print("List of months:January,Febraury,March.April,May,June,July,August,September,October,November,December")
month_name=input("Enter name of the month:")
if month_name=="Febraury":
    print("Number of days:28/29 days")
elif month_name in ("April","June","September","November"):
     print("Number of days:30 days")
elif month_name in("January","March","May","July","August","October","December"):
     print("Number of days:31 days")
else:
     print("Wrong month name")
    
