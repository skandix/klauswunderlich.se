import requests

def getLatestIP(inputIp, url="http://ip-api.com/json/"):
    return requests.get(url+inputIp, stream=True).json()

def getInfo(inputIp, s=""):
    getiP = getLatestIP(inputIp)

    status      = getiP['status']
    aS          = getiP['as']
    city        = getiP['city']
    country     = getiP['country']
    CountryCode = getiP['countryCode']
    isp         = getiP['isp']
    org         = getiP['org']
    query       = getiP['query']

    s += str('Status: {:s} \nAs: {:s}\nCity: {:s}\nCountry: {:s}\nCountryCode: {:s}\nISP: {:s}\nORG: {:s}\nQuery: {:s}').format(status, aS, city, country, CountryCode, isp, org, query)
    return s

#print getInfo("8.8.8.8")
