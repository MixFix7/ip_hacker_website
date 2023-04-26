from django.shortcuts import render
import requests
import folium
from pyfiglet import Figlet

def home(request):
    return render(request, template_name='index.html')


def ip_calculate(request):
    ip = request.GET['ip-address']

    response = requests.get(url=f"http://ip-api.com/json/{ip}").json()

    data = {
        "IP": response.get("query"),
        "prov": response.get("isp"),
        "Org": response.get("org"),
        "Country": response.get("country"),
        "RegionName": response.get("regionName"),
        "City": response.get("city"),
        "ZIP": response.get("zip"),
        "Lat": response.get("lat"),
        "Lon": response.get("lon"),
        "Status": response.get("status"),
        "Timezone": response.get("timezone"),
        "AS": response.get("as"),

    }


    return render(request, template_name='index.html', context=data)



