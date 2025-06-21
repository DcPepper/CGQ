import requests

fields = [
 "name",
 "cca2",
 "capital",
 "flags",
 "maps",
 "population",
 "continents",
 "languages",
 "area",
 "latlng"
 ]

url = f"https://restcountries.com/v3.1/all?fields={",".join(fields)}"
r = requests.get(url)
for country in r.json():
    geo = Geophraphy(
name=country["name"]["common"],
iso=country["cca2"],
capital=country["capital"][0],
population=country["population"],
area=round(country["area"]),
langue=list(country['languages'].values())[0],
continent=country["continents"][0],
lat=country["latlng"][0],
long=country["latlng"][1],
flag=country["flags"]["png"],
    )
    geo.save()