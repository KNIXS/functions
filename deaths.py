data = {
    "Deaths by Cause": {

        "Afghanistan": {

            2007: {
                "Number of executions": 15,
                "Deaths": {
                    "Meningitis": 2933,
                    "Alzheimer": 1402,
                    "Parkinson": 450,
                    "Nutritional deficiencies": 2488,
                    "Malaria": 393,
                    "Drowning": 2127
                }
            },

            2008: {
                "Number of executions": 17,
                "Deaths": {
                    "Meningitis": 2731,
                    "Alzheimer": 1424,
                    "Parkinson": 455,
                    "Nutritional deficiencies": 2277,
                    "Malaria": 255,
                    "Drowning": 1973
                }
            },

            2009: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 2460,
                    "Alzheimer": 1449,
                    "Parkinson": 460,
                    "Nutritional deficiencies": 2040,
                    "Malaria": 239,
                    "Drowning": 1852
                }
            },

            2010: {
                "Number of executions": 1,
                "Deaths": {
                    "Meningitis": 2395,
                    "Alzheimer": 1478,
                    "Parkinson": 466,
                    "Nutritional deficiencies": 1958,
                    "Malaria": 310,
                    "Drowning": 1813
                }
            },

            2011: {
                "Number of executions": 2,
                "Deaths": {
                    "Meningitis": 2327,
                    "Alzheimer": 1508,
                    "Parkinson": 473,
                    "Nutritional deficiencies": 1876,
                    "Malaria": 390,
                    "Drowning": 1775
                }
            }
        },

        "African Region": {

            2007: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 195161,
                    "Alzheimer": 43425,
                    "Parkinson": 11069,
                    "Nutritional deficiencies": 151048,
                    "Malaria": 835237,
                    "Drowning": 27732
                }
            },

            2008: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 189839,
                    "Alzheimer": 45053,
                    "Parkinson": 11469,
                    "Nutritional deficiencies": 143418,
                    "Malaria": 821742,
                    "Drowning": 26969
                }
            },

            2009: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 187657,
                    "Alzheimer": 46598,
                    "Parkinson": 11840,
                    "Nutritional deficiencies": 136904,
                    "Malaria": 821742,
                    "Drowning": 26969
                }
            },

            2010: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 182351,
                    "Alzheimer": 48285,
                    "Parkinson": 12232,
                    "Nutritional deficiencies": 131125,
                    "Malaria": 804031,
                    "Drowning": 26638
                }
            },

            2011: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 172992,
                    "Alzheimer": 50114,
                    "Parkinson": 12632,
                    "Nutritional deficiencies": 127263,
                    "Malaria": 764244,
                    "Drowning": 26284
                }
            }
        },

        "India": {

            2007: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 41027,
                    "Alzheimer": 28215,
                    "Parkinson": 8456,
                    "Nutritional deficiencies": 71652,
                    "Malaria": 16945,
                    "Drowning": 51382
                }
            },

            2008: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 40218,
                    "Alzheimer": 29483,
                    "Parkinson": 8731,
                    "Nutritional deficiencies": 69384,
                    "Malaria": 16237,
                    "Drowning": 50714
                }
            },

            2009: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 39462,
                    "Alzheimer": 30876,
                    "Parkinson": 9018,
                    "Nutritional deficiencies": 67105,
                    "Malaria": 15486,
                    "Drowning": 49963
                }
            },

            2010: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 38641,
                    "Alzheimer": 32397,
                    "Parkinson": 9325,
                    "Nutritional deficiencies": 64958,
                    "Malaria": 14792,
                    "Drowning": 49105
                }
            },

            2011: {
                "Number of executions": 0,
                "Deaths": {
                    "Meningitis": 37895,
                    "Alzheimer": 34082,
                    "Parkinson": 9651,
                    "Nutritional deficiencies": 62831,
                    "Malaria": 14125,
                    "Drowning": 48376
                }
            }
        }
    }
}

def total_deaths(country):
    total = 0
    for key, info in data["Deaths by Cause"][country].items():
        for deaths in info["Deaths"].values():
            total += deaths
            
        total += info["Number of executions"]

    return total


country = input("Country name: ")
print(f"Total deaths in {country}: {total_deaths(country)}")
print()


def meningitis(Meningitis):
    
    if Meningitis == "YES":
        for country, years in data["Deaths by Cause"].items():
            print("_____"*15)
           
            print(country)
            print("_____"*15)
            
            for year, info in years.items():
                print(year, ":", info["Deaths"]["Meningitis"])

Meningitis = input("Do you want people died from Meningitis: ").upper()

meningitis(Meningitis)


def alzheimer(Alzheimer):
    
    if Alzheimer == "YES":
        for country, years in data["Deaths by Cause"].items():
            print("_____"*15)
           
            print(country)
            print("_____"*15)
            
            for year, info in years.items():
                print(year, ":", info["Deaths"]["Alzheimer"])

Alzheimer = input("Do you want people died from Alzheimer: ").upper()

alzheimer(Alzheimer)


def parkinson(Parkinson):
    
    if Parkinson == "YES":
        for country, years in data["Deaths by Cause"].items():
            print("_____"*15)
           
            print(country)
            print("_____"*15)
            
            for year, info in years.items():
                print(year, ":", info["Deaths"]["Parkinson"])

Parkinson = input("Do you want people died from Parkinson: ").upper()

parkinson(Parkinson)


def nutritional_deficiencies(Nutritional_deficiencies):
    
    if Nutritional_deficiencies == "YES":
        for country, years in data["Deaths by Cause"].items():
            print("_____"*15)
           
            print(country)
            print("_____"*15)
            
            for year, info in years.items():
                print(year, ":", info["Deaths"]["Nutritional deficiencies"])

Nutritional_deficiencies = input("Do you want people died from Nutritional_deficiencies: ").upper()

nutritional_deficiencies(Nutritional_deficiencies)


def malaria(Malaria):
    
    if Malaria == "YES":
        for country, years in data["Deaths by Cause"].items():
            print("_____"*15)
           
            print(country)
            print("_____"*15)
            
            for year, info in years.items():
                print(year, ":", info["Deaths"]["Malaria"])

Malaria = input("Do you want people died from Malaria: ").upper()

malaria(Malaria)


def drowning(Drowning):
    
    if Drowning == "YES":
        for country, years in data["Deaths by Cause"].items():
            print("_____"*15)
           
            print(country)
            print("_____"*15)
            
            for year, info in years.items():
                print(year, ":", info["Deaths"]["Drowning"])

Drowning = input("Do you want people died from Drowning: ").upper()

drowning(Drowning)


def years(country, min_year, max_year):

    total = 0

    for year, info in data["Deaths by Cause"][country].items():

        if min_year <= year <= max_year:

            total += info["Number of executions"]

            for disease, deaths in info["Deaths"].items():
                total += deaths

    return total


country = input("Country name: ").title()
min_year = int(input("Enter starting year: "))
max_year = int(input("Enter ending year: "))

print(f"Total deaths from {min_year}-{max_year}: {years(country, min_year, max_year)}")
