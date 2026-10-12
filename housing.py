data = {

    "Index": {

        "0": {
            "Title": "1 BHK Ready to Occupy Flat for sale in Srushti Siddhi Mangal Murti Complex Bhiwandi",
            "Description": "Bhiwandi, Thane has an attractive 1 BHK Flat for sale. The property is ideally located in a strategic",
            "Amount": "42 Lac",
            "Price": 6000,
            "Location": "Thane",
            "Carpet Area": "500 sqft",
            "Status": "Ready to move",
            "Floor": "10 to 11",
            "Transaction": "Resale"
        },

        "1": {
            "Title": "2 BHK Ready to Occupy Flat for sale in Dosti Vihar Pokhran Road",
            "Description": "One can find this stunning 2 BHK flat for sale in Pokhran Road, Thane. It enjoys an excellent location",
            "Amount": "98 Lac",
            "Price": 13799,
            "Location": "Thane",
            "Carpet Area": "473 sqft",
            "Status": "Ready to move",
            "Floor": "3 out of 22",
            "Transaction": "Resale"
        },
        "2": {
            "Title": "2 BHK Ready to Occupy Flat for sale in Sunrise by Kalpataru Kolshet Road",
            "Description": "Up for immediate sale is a 2 BHK apartment in Kolshet Road, Thane. Don't miss this bargain flat",
            "Amount": "1.40cr",
            "Price": 17500,
            "Location": "Thane",
            "Carpet Area": "779sqft",
            "Status": "Ready to move",
            "Floor": "10 out of 29",
            "Transaction": "Resale"
        },
        "3": {
            "Title": "1 BHK Ready to Occupy Flat for sale Kasheli",
            "Description": "This beautiful 1 BHK Flat is available for sale in Kasheli, Thane. This flat for resale has a desirable location",
            "Amount": "25 Lac",
            "Price": None,
            "Location": "Thane",
            "Carpet Area": "530 sqft",
            "Status": "Ready to move",
            "Floor": "1 out of 3",
            "Transaction": "Resale"
        },
        "4": {
            "Title": "2 BHK Ready to Occupy Flat for sale in TenX Habitat Raymond Realty Pokhran Road",
            "Description": "This lovely 2 BHK Flat in Pokhran Road, Thane is up for sale. This flat is situated in the Tenx Habitat Raymond Realty township",
            "Amount": "1.60cr",
            "Price": 18824,
            "Location": "Thane",
            "Carpet Area": "635 sqft",
            "Status": "Ready to move",
            "Floor": "20 out of 42",
            "Transaction": "Resale"
        },
        "5": {
            "Title": "1 BHK Ready to Occupy Flat for sale in Virat Aangan Titwala",
            "Description": "Creatively planned and constructed is a 1 BHK flat for sale in Titwala, Thane. It is housed in the well-planned Virat Aangan township",
            "Amount": "45 Lac",
            "Price": 6618,
            "Location": "Thane",
            "Carpet Area": "680 sqft",
            "Status": "Ready to move",
            "Floor": "2 out of 7",
            "Transaction": "Resale"
        },
        "6": {
            "Title": "1 BHK Ready to Occupy Flat for sale Mumbra",
            "Description": "This magnificent 1 BHK Flat is available for sale in Mumbra, Thane. This premium flat is available for resale at an unbelievable price",
            "Amount": "16.5 Lac",
            "Price": 2538,
            "Location": "Thane",
            "Carpet Area": "550 sqft",
            "Status": "Ready to move",
            "Floor": "4 out of 5",
            "Transaction": "Resale"
        },

    }
}

def amount(amount_str):
    
    amount_str = amount_str.strip().lower()
    
    if "Cr" in amount_str:
        return float(amount_str.replace("cr","")*10000000)
    if "lac" in amount_str:
        return float(amount_str.replace("lac","")*1000000)
    
def price(min,max):
    
    for key,value in data["Index"].items():
        amount_filter = amount(value["Amount"])
        if min >= amount_filter  and max <= amount_filter:
            print(key)
            print("Title",": ",value["Title"])
            print("Description",": ",value["Description"])
            print("Amount",": ",value["Amount"])
            print("Price",": ",value["Price"])
            print("Location",": ",value["Location"])
        
        
min = input("Enter minimum value: ")
max = input("Enter maximum value: ")

price(min,max)
