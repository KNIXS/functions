data = {
    "electronics": {
        
        "mobile phone": {
            
            "Samsung Galaxy S25": {
                "Price": "74,999",
                "Rating": "4.5",
                "Features": [
                    "~AMOLED display with high refresh rate",
                    "~Multi-camera system",
                    "~Fast charging",
                    "~AI features",
                    "~5G support"]},
            
            "OnePlus Nord CE 5": {
                "Price": "24,999",
                "Rating": "4.4",
                "Features": [
                    "~AMOLED display",
                    "~Fast charging",
                    "~Large battery",
                    "~5G connectivity"]},
            
            "Motorola Edge 60 Pro": {
                "Price": "37,999",
                "Rating": "4.8",
                "Features": [
                    "~Curved AMOLED display",
                    "~Fast charging",
                    "~High refresh rate",
                    "~AI camera enhancements",
                    "~5G support"]},
            
            "Realme GT 7 5G Mobile Phone":{
                "Price":"39,999",
                "Rating": "4.8",
                "Features":[
                    "Gaming-focused processor",
                    "Large battery",
                    "Fast charging",
                    "High refresh display",
                    "Triple camera setup"]},
            
            "Google Pixel 10a 5G":{
                "Price": "47,790",
                "Rating": "4.6/5",
                "Features":[
                    "AI camera tools",
                    "Clean Android experience",
                    "Long software updates",
                    "Strong photography performance",
                    "5G connectivity"]},
            
            "Samsung Galaxy A36 5G":{
                "Price": "32,499",
                "Rating": "4.7",
                "Features":[
                    "Super AMOLED display",
                    "Multiple camera setup",
                    "Long battery life",
                    "Fast charging",
                    "5G support"]},



            
        },
        
        "Audio devices":{
            
            "Wireless Headphones":{
                
                "Sony WH-1000XM5 Wireless Noise Cancelling Headphones":{
                    "Price": "29,990",
                    "Rating": "4.6",
                    "Features":[
                        "Active Noise Cancellation (ANC)",
                        "Premium sound quality",
                        "Multi-device connection",
                        "Long battery life",
                        "Touch controls"]}
                },
            
            "Wired Earphones":{
                
                "Sony MDR-EX15AP In-Ear Wired Earphones":{
                    "Price": "649",
                    "Rating": "4.4",
                    "Features":[
                        "3.5mm audio jack",
                        "Built-in microphone",
                        "Lightweight design",
                        "Deep bass sound"]},
                
                "Apple EarPods":{
                    "Price": "947",
                    "Rating": "4.7",
                    "Features":[
                        "Built-in mic and controls",
                        "Comfortable fit",
                        "Clear voice quality",
                        "Wired connection"]}
                

                
                },
            
            "TWS (True Wireless Earbuds)":{
                
                "Samsung Galaxy Buds Core TWS Earbuds":{
                    "Price": "4,399",
                    "Rating": "4.5",
                    "Features":[
                        "Wireless charging case",
                        "Noise reduction",
                        "Touch controls",
                        "Long battery backup"]},
                
                "OnePlus Nord Buds 3 Pro Truly Wireless Bluetooth Earbuds":{
                    "Price":"2,999",
                    "Rating":"4.7",
                    "Features":[
                        "ANC support",
                        "Fast charging",
                        "Gaming low latency mode",
                        "AI call noise reduction"]},
                },
                
                "Bluetooth Speakers":{
                    
                    "JBL Go 4 Ultra-Portable Wireless Bluetooth Speaker":{
                        "Price": "3,999",
                        "Rating": "4.8/5",
                        "Features":[
                            "Portable design",
                            "Waterproof body",
                            "Bluetooth connectivity",
                            "Strong bass output"]},
                    
                    "boAt Stone 350 Bluetooth Speaker":{
                        "Price":"1,499",
                        "Rating":"4.6",
                        "Features":[
                            "IPX7 water resistance",
                            "Portable design",
                            "Bluetooth support",
                            "Long playback time"]}

                    
                    }


                
                
            
            }
        
    }
}

def search_device(device,appliances):

    mobile = data["electronics"]["mobile phone"]
    wireless = data["electronics"]["Audio devices"]["Wireless Headphones"]
    wired = data["electronics"]["Audio devices"]["Wired Earphones"]
    tws = data["electronics"]["Audio devices"]["TWS (True Wireless Earbuds)"]
    bluetooth = data["electronics"]["Audio devices"]["Bluetooth Speakers"]

    if device in mobile:
        print(device,": ", mobile[device])

    elif device in wireless:
        print(device,": ", wireless[device])

    elif device in wired:
        print(device,": ", wired[device])

    elif device in tws:
        print(device,": ", tws[device])

    elif device in bluetooth:
        print(device,": ", bluetooth[device])

    else:
        
        if appliances == "mobile phone":
            selected_devices = mobile
        
        elif appliances == "Wireless Headphones":
            selected_devices = wireless
            
        elif appliances == "Wired Earphones":
            selected_devices = wired
            
        elif appliances == "TWS":
            selected_devices = tws
            
        elif appliances == "Bluetooth Speakers":
            selected_devices = bluetooth
        
        else:
            selected_devices = {}
            print("Appliance not found")
            
    
    minprice = int(input("enter your minimum amount : "))
    maxprice = int(input("enter your maximum amount : "))
    

    for x, y in selected_devices.items():
        price = int(y["Price"].replace(",", ""))

        if price >= minprice and price <= maxprice :
            print(x)
            print("Price:", y["Price"])
            print("Rating:", y["Rating"])
            print("Features:", y["Features"])
            print()
    
            
        
d = input("Enter your device name: ")
a = input("Enter your appliances: ")
search_device(d,a)
    
    
    