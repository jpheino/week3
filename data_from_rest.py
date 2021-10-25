from urllib.request import urlopen
import json
url = "https://api.github.com/search/repositories?q=language:python"



response = urlopen(url)
data_json = json.loads(response.read())
for data in data_json["items"]:
    print(f'{data["name"]} {data["forks"]}')