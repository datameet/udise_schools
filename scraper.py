import requests
import json
import os.path
from time import sleep

from requests.structures import CaseInsensitiveDict

file_name_format = "./raw/ud_dt_n_{udise_district_code}_page_{page_number_str}.geojson"


def get_data(udise_district_code, resultOffset):
    #sleep
    sleep(2)

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
    
    
# udise_district_codes_st_1 = [101,102,103,104,105,106,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
# udise_district_codes_st_2 = [201,202,203,204,205,206,207,208,209,210,211,212]
# udise_district_codes_st_3 = [301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322]
# udise_district_codes_st_4 = [401]
# udise_district_codes_st_5 = [501,502,503,504,505,506,507,508,509,510,511,512,513]
# udise_district_codes_st_6 = [601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622]
# udise_district_codes_st_7 = [710,711,712,713,714,715,716,717,718,719,720,721,722]
# udise_district_codes_st_8 = [801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833]
# udise_district_codes_st_9 = [901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975]
# udise_district_codes_st_10 = [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038]
# udise_district_codes_st_11 = [1101,1102,1103,1104]
# udise_district_codes_st_12 = [1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226]
# udise_district_codes_st_13 = [1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311]
# udise_district_codes_st_14 = [1401,1402,1403,1404,1405,1406,1407,1408,1409,1410,1411,1412,1413,1414,1415,1416]
# udise_district_codes_st_15 = [1503,1504,1502,1507,1506,1501,1508,1505]
# udise_district_codes_st_16 = [1601,1602,1603,1604,1605,1606,1607,1608]
# udise_district_codes_st_17 = [1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711]
# udise_district_codes_st_18 = [1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827,1828,1829,1830,1831,1832,1833]
# udise_district_codes_st_19 = [1901,1902,1903,1904,1905,1906,1907,1908,1910,1911,1912,1913,1914,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926]
# udise_district_codes_st_20 = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
# udise_district_codes_st_21 = [2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130]
# udise_district_codes_st_22 = [2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2216,2217,2218,2219,2220,2221,2222,2223,2224,2225,2226,2227]
# udise_district_codes_st_23 = [2301,2302,2303,2304,2305,2306,2307,2308,2309,2310,2311,2312,2313,2314,2315,2316,2317,2318,2319,2320,2321,2322,2323,2324,2325,2326,2327,2328,2329,2330,2331,2332,2333,2334,2335,2336,2337,2338,2339,2340,2341,2342,2343,2344,2345,2346,2347,2348,2349,2350,2351,2352]
# udise_district_codes_st_24 = [2401,2402,2403,2404,2405,2406,2407,2408,2409,2410,2411,2412,2413,2414,2415,2416,2417,2418,2419,2420,2421,2422,2423,2424,2425,2426,2427,2428,2429,2430,2431,2432]
# udise_district_codes_st_25 = [2502, 2501]
# udise_district_codes_st_26 = [2601]
# udise_district_codes_st_27 = [2701,2702,2703,2704,2705,2706,2707,2708,2709,2710,2711,2712,2713,2714,2715,2716,2717,2718,2719,2720,2721,2722,2723,2724,2725,2726,2727,2728,2729,2730,2731,2732,2733,2734,2735,2736]
# udise_district_codes_st_28 = [2811,2812,2813,2814,2815,2816,2817,2818,2819,2820,2821,2822,2823]
# udise_district_codes_st_29 = [2901,2902,2903,2904,2905,2906,2907,2908,2909,2910,2911,2912,2913,2914,2915,2916,2917,2918,2919,2920,2921,2922,2923,2924,2925,2926,2927,2928,2929,2930,2931,2932,2933,2934]
# udise_district_codes_st_30 = [3001, 3002]

# udise_district_codes_st_31  = [3101]
# udise_district_codes_st_32  = [3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214]
# udise_district_codes_st_33  = [3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3318,3319,3320,3321,3322,3323,3324,3325,3326,3327,3328,3329,3330,3331,3332,3333]
# udise_district_codes_st_34  = [3401,3402,3403,3404]
# udise_district_codes_st_35  = [3501,3503,3502]

udise_district_codes_st_36  = [3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613,3614,3615,3616,3617,3618,3619,3620,3621,3622,3623,3624,3625,3626,3627,3628,3629,3630,3631,3632,3633]
udise_district_codes_st_37  = [3708,3707]


udise_district_codes = udise_district_codes_st_36 + udise_district_codes_st_37 

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
