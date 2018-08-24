import json


def readjson(province,city,area,street):
    with open("./analysis/json/areadata.json", 'r', encoding='utf-8') as json_file:
        t = json.load(json_file)
        data={}
        data["provice"] = t["86"][province]
        data["city"] = t[province][city]
        data["area"] = t[city][area]
        data["street"] = t[area][street]
        return data

def localjson(province,city,area,street):
    with open("./analysis/json/areadata.json", 'r', encoding='utf-8') as json_file:
        t = json.load(json_file)
        data=t["86"][province] + t[province][city] + t[city][area] + t[area][street]
        return data

def ReadMapJson(centercounts):
    with open("./analysis/json/areadata.json", 'r', encoding='utf-8') as json_file:
        t = json.load(json_file)
        print(centercounts)
        citytotle = []
        for centercs in centercounts:
            cityal={}
            city=t[centercs['center__province']][centercs['center__city']][:-1]
            if city == "市辖":
                city = t["86"][centercs['center__province']][:-1]

            cityal["value"]= int(centercs['count'])
            cityal["name"] = city
            citytotle.append(cityal)
        print(citytotle)

        return citytotle