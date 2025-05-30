year = input("Please type the year range: 2000-2004, 2005-2009, 2010-2014, 2015-2019 or all\n")
if year == "2000-2004":
    year_code = ["2000", "2001", "2002", "2003", "2004"]
elif year == "2005-2009":
    year_code = ["2005", "2006", "2007", "2008", "2009"]
elif year == "2010-2014":
    year_code = ["2010", "2011", "2012", "2013", "2014"]
elif year == "2015-2019":
    year_code = ["2015", "2016", "2017", "2018", "2019"]
else:
    print("You typed the year wrong, please restart the program")
    exit()

gender = input("Please type which gender you want as M or F or all\n")
def get_gender_code(gender):
    if gender == "M":
        return "M"
    elif gender == "F":
        return "F"
    elif gender == "all":
        return "*All*"
    else:
        print("You typed the gender wrong, please restart the program")
        exit()

gender_code = get_gender_code(gender)

race = input("Please type the race you want Black (B) or everything but black (NB) or all \n")

def get_race_code(race):
    if race == "B":
        return "2054-5"
    elif race == "NB":
        return ["1002-5", "A-PI", "2106-3"]
    elif race == "all":
        return "*All*"
    else:
        print("You typed the race wrong, please restart the program")
        exit()

race_code = get_race_code(race)




b_parameters = {
        "B_1": "D77.V2-level2", 
        "B_2": "*None*", 
        "B_3": "*None*", 
        "B_4": "*None*", 
        "B_5": "*None*"
    }

m_parameters = {
        "M_1": "D77.M1",   # Deaths, must be included
        "M_2": "D77.M2",   # Population, must be included
        "M_3": "D77.M3",   # Crude rate, must be included
        "M_31": "D77.M31",        # Standard error (crude rate)
        #"M_32": "D76.M32",         # 95% confidence interval (crude rate)
        #"M_41": "D76.M41", # Standard error (age-adjusted rate)
        #"M_42": "D76.M42",  # 95% confidence interval (age-adjusted rate)
        "M_9": "D77.M9" # Percent of Total deaths
    }


f_parameters = {
        "F_D77.V1": year_code, # year/month
        "F_D77.V10": ["*All*"], # Census Regions - dont change
        "F_D77.V13": ["*All*"], # Census Regions - dont change
        "F_D77.V2": ["*All*"], # ICD-10 Codes
        "F_D77.V25": ["*All*"], # ICD-10 Codes
        "F_D77.V26": ["*All*"], # ICD-10 Codes
        "F_D77.V27": ["*All*"], # HHS Regions - dont change
        "F_D77.V9": ["*All*"] # State County - dont change
    }

i_parameters = {
        "I_D77.V1": "2000 (2000)",  # year/month
        "I_D77.V10": "*All* (The United States)", # Census Regions - dont change
        "I_D77.V2": "*All* (All Causes of Death)", # ICD-10 Codes
        "I_D77.V25": "All Causes of Death", # ICD-10 Codes
        "I_D77.V27": "*All* (The United States)", # HHS Regions - dont change
        "I_D77.V9": "*All* (The United States)" # State County - dont change
    }


v_parameters = {
        "V_D77.V1": "",         # Year/Month
        "V_D77.V10": "",        # Census Regions
        "V_D77.V11": "*All*",   # 2006 Urbanization
        "V_D77.V12": "*All*",   # ICD-10 130 Cause List (Infants)
        "V_D77.V13": "*All*",
        "V_D77.V13_AND": "",
        "V_D77.V15": "",
        "V_D77.V15_AND": "",
        "V_D77.V16": "",
        "V_D77.V16_AND": "",
        "V_D77.V17": "*All*",   # Hispanic Origin
        "V_D77.V19": "*All*",   # 2013 Urbanization
        "V_D77.V2": "",         # ICD-10 Codes
        "V_D77.V20": "*All*",   # Autopsy
        "V_D77.V21": "*All*",   # Place of Death
        "V_D77.V22": "*All*",   # Injury Intent
        "V_D77.V23": "*All*",   # Injury Mechanism and All Other Leading Causes
        "V_D77.V24": "*All*",   # Weekday
        "V_D77.V25": "",   # Drug/Alcohol Induced Causes
        "V_D77.V26": "",
        "V_D77.V26_AND": "",
        "V_D77.V27": "",        # HHS Regions
        "V_D77.V4": "*All*",    # ICD-10 113 Cause List
        "V_D77.V5": "85+", # Ten-Year Age Groups
        "V_D77.V51": "*All*",   # Five-Year Age Groups
        "V_D77.V52": "*All*",   # Single-Year Ages
        "V_D77.V6": "00",       # Infant Age Groups
        "V_D77.V7": gender_code,    # Gender
        "V_D77.V8": race_code,    # Race
        "V_D77.V9": "",          # State/County
    }

o_parameters = {
        "O_V10_fmode": "freg",    # Use regular finder and ignore v parameter value
        "O_V1_fmode": "freg",     # Use regular finder and ignore v parameter value
        "O_V13_fmode": "fadv",     # Use regular finder and ignore v parameter value
        "O_V15_fmode": "fadv",     # Use regular finder and ignore v parameter value
        "O_V16_fmode": "fadv",     # Use regular finder and ignore v parameter value
        "O_V2_fmode": "freg",     # Use regular finder and ignore v parameter value
        "O_V25_fmode": "freg",     # Use regular finder and ignore v parameter value
        "O_V26_fmode": "fadv",     # Use regular finder and ignore v parameter value
        "O_V27_fmode": "freg",    # Use regular finder and ignore v parameter value
        "O_V9_fmode": "freg",     # Use regular finder and ignore v parameter value
        "O_aar": "aar_none",       # age-adjusted rates
        "O_aar_pop": "0000",      # population selection for age-adjusted rates
        "O_age": "D77.V5",        # select age-group (e.g. ten-year, five-year, single-year, infant groups)
        "O_javascript": "on",     # Set to on by default
        "O_location": "D77.V9",   # select location variable to use (e.g. state/county, census, hhs regions)
        "O_mcd": "D77.V13",
        "O_oc-sect1-request": "open",
        "O_precision": "2",       # decimal places
        "O_rate_per": "1000000",   # rates calculated per X persons
        "O_show_totals": "true",  # Show totals for 
        "O_timeout": "600",
        "O_title": "",    # title for data run
        "O_ucd": "D77.V2",        # select underlying cause of death category
        "O_urban": "D77.V19"      # select urbanization category
    }


vm_parameters = {
        "VM_D77.M6_D77.V10": "",        # Location
        "VM_D77.M6_D77.V17": "*All*",   # Hispanic-Origin
        "VM_D77.M6_D77.V1_S": "*All*",  # Year
        "VM_D77.M6_D77.V7": "*All*",    # Gender
        "VM_D77.M6_D77.V8": "*All*"     # Race
    }

misc_parameters = {
        "action-Send": "Send",
        "finder-stage-D77.V1": "codeset",
        "finder-stage-D77.V10": "codeset",
        "finder-stage-D77.V13": "codeset",
        "finder-stage-D77.V15": "",
        "finder-stage-D77.V16": "",
        "finder-stage-D77.V2": "codeset",
        "finder-stage-D77.V25": "codeset",
        "finder-stage-D77.V26": "codeset",
        "finder-stage-D77.V27": "codeset",
        "finder-stage-D77.V9": "codeset",
        "stage": "request"
    }

def createParameterList(parameterList):
        """Helper function to create a parameter list from a dictionary object"""
        
        parameterString = ""
        
        for key in parameterList:
            parameterString += "<parameter>\n"
            parameterString += "<name>" + key + "</name>\n"
            
            if isinstance(parameterList[key], list):
                for value in parameterList[key]:
                    parameterString += "<value>" + value + "</value>\n"
            else:
                parameterString += "<value>" + parameterList[key] + "</value>\n"
            
            parameterString += "</parameter>\n"
            
        return parameterString

xml_request = "<request-parameters>\n"
xml_request += createParameterList(b_parameters)
xml_request += createParameterList(m_parameters)
xml_request += createParameterList(f_parameters)
xml_request += createParameterList(i_parameters)
xml_request += createParameterList(o_parameters)
xml_request += createParameterList(vm_parameters)
xml_request += createParameterList(v_parameters)
xml_request += createParameterList(misc_parameters)
xml_request += "</request-parameters>"

print(xml_request)
input()

import requests

url = "https://wonder.cdc.gov/controller/datarequest/D77"
response = requests.post(url, data={"request_xml": xml_request, "accept_datause_restrictions": "true"})


if response.status_code == 200:
    print("Data retreived from CDC Wonder!")
    data = response.text
else:
    print("something went wrong")

    
print(data)
input()

