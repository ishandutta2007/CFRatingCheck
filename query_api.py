import urllib.request, json

only_active = "false"
query = (
    "https://codeforces.com/api/user.ratedList?activeOnly=" + only_active + "?lang=en"
)
print("Quering API: {}".format(query))
with urllib.request.urlopen(query) as url:
    data = json.loads(url.read().decode())
    print(data)
    json_string = json.dumps(data)
    with open("codeforces_users.json", "w") as json_file:
        json_file.write(json_string)
        json_file.close()
