data = {
    
   "Store 1":{
       
        "Dates":{
            
        "05/02/2010":{
            "Weekly sales":1643690,
            "Holiday flag":0,
            "Temperature":"42.31F",
            "Fuel price":2.572,
            "CPI":211.096,
            "Unemployment":8.106},
        "12/02/2010":{
            "Weekly sales":1641957,
            "Holiday flag":1,
            "Temperature":"38.51F",
            "Fuel price":2.548,
            "CPI":211.242,
            "Unemployment":8.106
            },
        "19/02/2010":{
            "Weekly sales":1611968,
            "Holiday flag":0,
            "Temperature":"39.93F",
            "Fuel price":2.514,
            "CPI":211.289,
            "Unemployment":8.106
            },
        "26/02/2010":{
            "Weekly sales":1409727,
            "Holiday flag":0,
            "Temperature":"46.63F",
            "Fuel price":2.561,
            "CPI":211.319,
            "Unemployment":8.106
            },
        
        }
       
       },
   
   "Store 2":{
       
       "Dates":{
           "05/02/2010":{
               "Weekly sales":2136989,
               "Holiday flag":0,
               "Temperature":"40.19F",
               "Fuel price":2.572,
               "CPI":210.752,
               "Unemployment":8.324
               },
           "12/02/2010":{
               "Weekly sales":2137809,
               "Holiday flag":1,
               "Temperature":"38.49F",
               "Fuel price":2.548,
               "CPI":210.897,
               "Unemployment":8.324
               },
            "19/02/2010":{
               "Weekly sales":2124451,
               "Holiday flag":0,
               "Temperature":"39.69F",
               "Fuel price":2.514,
               "CPI":210.945,
               "Unemployment":8.324
               },
            "26/02/2010":{
               "Weekly sales":1865097,
               "Holiday flag":0,
               "Temperature":"46.1F",
               "Fuel price":2.561,
               "CPI":210.975,
               "Unemployment":8.324
               },
           }
       
       }
    
    }

store = input("Enter store: ")

def add():
    weekly_sales = 0

    for i in data[store]["Dates"].values():
        weekly_sales += i["Weekly sales"]

    return weekly_sales

weekly_sales = add()
print()
print("Total Weekly Sales:", weekly_sales)
print()
print("-------------------------------------------------------------------------")
print()


def week_sales():
    previous_sales = 0

    for date, info in data[store]["Dates"].items():
        current_sales = info["Weekly sales"]

        if previous_sales != 0:
            difference = current_sales - previous_sales
            percentage = (difference / weekly_sales) * 100

            print(f"Date       : {date}")
            print(f"Sales      : {current_sales}")
            print(f"Difference : {difference}")
            print(f"Percentage : {percentage:.2f}%")
            print()
            print("--------------------------------------------------------")
            print()

        previous_sales = current_sales

week_sales()
