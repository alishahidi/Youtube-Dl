from modules import loading


def access():
    ipDetails = loading.json.loads(loading.requests.get("http://ip-api.com/json/?fields=country").text)
    country = ipDetails["country"]
    if country == "Iran":
        print(loading.colored(f"Access Denied on {country}", "red"))
        exit()