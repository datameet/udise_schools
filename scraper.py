import requests
import json
import os.path
from time import sleep

from requests.structures import CaseInsensitiveDict

file_name_format = "./raw/ud_dt_n_{udise_district_code}_page_{page_number_str}.geojson"


def get_data(udise_district_code, resultOffset):
    #sleep
    sleep(1)

    url = "https://geoportal.nic.in/nicgis/rest/services/SCHOOLGIS/Schooldata/MapServer/0/query?f=geojson&returnGeometry=true&outFields=*&where=ud_dt_n%3D'{udise_district_code}'&resultOffset={resultOffset}".format(udise_district_code=udise_district_code, resultOffset=resultOffset)
    print(url)
    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
    headers["Connection"] = "keep-alive"
    headers["Origin"] = "https://schoolgis.nic.in"
    headers["Referer"] = "https://schoolgis.nic.in/"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "cross-site"
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    #headers["sec-ch-ua"] = "" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91""
    headers["sec-ch-ua-mobile"] = "?0"
    resp = requests.get(url, headers=headers)
    print(resp)
    return resp.json()

def write_data(data, file_name):
    f = open(file_name, "w") 
    f.write(json.dumps(data))
    f.close()

def next_page_exists(data):
    if "exceededTransferLimit" in data:
        exceededTransferLimit = data["exceededTransferLimit"]
    else:
        exceededTransferLimit = False
    return exceededTransferLimit

def get_file_name(udise_district_code, page_number):
    page_number_str = "{:02d}".format(page_number)
    file_name = file_name_format.format(udise_district_code=udise_district_code, page_number_str=page_number_str)
    return file_name

def get_paged_data_and_save(udise_district_code, resultOffset, page_number):
    print("udise_district_code, resultOffset, page_number", udise_district_code, resultOffset, page_number)
    file_name = get_file_name(udise_district_code, page_number)
    data = get_data(udise_district_code, resultOffset)    
    print(data)
    write_data(data, file_name)
    return next_page_exists(data)
    
    

udise_district_codes = [101,102,103,104,105,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122]

for udise_district_code in udise_district_codes:
    resultOffset = 0
    page_number = 1

    file_name = get_file_name(udise_district_code, page_number)
    next_page = get_paged_data_and_save(udise_district_code, resultOffset, page_number)
    print(next_page)

    while next_page:
        page_number = page_number + 1
        resultOffset = resultOffset + 1000
        file_name = get_file_name(udise_district_code, page_number)
        next_page = get_paged_data_and_save(udise_district_code, resultOffset, page_number)        
