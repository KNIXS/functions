data = {
    "SKU0": {
        "Product type": "haircare",
        "Price": 69.80,
        "Availability": 55,
        "Number of products sold": 802,
        "Revenue generated": 8661.99,
        "Stock levels": 58,
    },

    "SKU1": {
        "Product type": "skincare",
        "Price": 14.84,
        "Availability": 95,
        "Number of products sold": 736,
        "Revenue generated": 7460.90,
        "Stock levels": 53,
    },
    
    "SKU2":{
        "Product type": "haircare",
        "Price": 11.31,
        "Availability": 34,
        "Number of products sold": 8,
        "Revenue generated": 9677.74,
        "Stock levels": 1,
        },
    
    "SKU3":{
        "Product type": "skincare",
        "Price": 61.16,
        "Availability": 68,
        "Number of products sold": 83,
        "Revenue generated": 7766.83,
        "Stock levels": 23,
        },
    
    "SKU4":{
        "Product type": "skincare",
        "Price": 4.80,
        "Availability": 26,
        "Number of products sold": 871,
        "Revenue generated": 2686.83,
        "Stock levels": 5,
        },
    
    "SKU5":{
        "Product type": "haircare",
        "Price": 1.69,
        "Availability": 87,
        "Number of products sold": 147,
        "Revenue generated": 2828.34,
        "Stock levels": 90,
        }
}

def info(stock_keeping_unit):   
    if stock_keeping_unit in data:
        for key, value in data[stock_keeping_unit].items():
            print(f"{key}: {value}")
    else:
        print("SKU not found.")

sku = input("Enter SKU: ")     
info(sku)

def count(product_type):
    count =0   
    for key,value in data.items():
        if product_type == value["Product type"]:
            count += 1
    print(product_type,": ",count)
            
pt = input("Enter product type: ").lower()
count(pt)

def price(total_price, revenue_generated):
    price = 0
    revenue = 0

    if total_price == "YES":
        for key, value in data.items():
            price += value["Price"]
        print("Total Price:", price)

    if revenue_generated == "YES":
        for key, value in data.items():
            revenue += value["Revenue generated"]
        print("Total Revenue Generated:", revenue)

p = input("Do you want total price: ").upper()
r = input("Do you want total Revenue Generated: ").upper()

price(p, r)
        