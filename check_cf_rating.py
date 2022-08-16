import urllib.request, json

import ast

european_countries = [
    "Albania",
    "Andorra",
    "Armenia",
    "Austria",
    "Azerbaijan",
    "Belarus",
    "Belgium",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czechia",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Georgia",
    "Germany",
    "Greece",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Kazakhstan",
    "Kosovo",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Moldova",
    "Monaco",
    "Montenegro",
    "Netherlands",
    "Macedonia",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "Russia",
    "San Marino",
    "Serbia",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
    "Turkey",
    "Ukraine",
    "United Kingdom",
]

res_all = []
with open("codeforces_users.json") as json_file:
    lit = json_file.read()
    data = ast.literal_eval(lit)
    for acc in data["result"]:
        # if 'country' in acc and acc['country'] in european_countries and acc['country'] != "Russia":
        #    res_all.append((acc['maxRating'], acc['country'], acc['handle']))
        if "country" in acc:
            res_all.append((acc["maxRating"], acc["country"], acc["handle"]))
        else:
            res_all.append((acc["maxRating"], "Unknown", acc["handle"]))

res_all = sorted(res_all, key=lambda x: -x[0])

with open("README.md", "w") as fw:
    fw.write("| Rank     |      Rating   |    Country    |  Handle |\n")
    fw.write("|----------|:-------------:|:-------------:|------:|\n")
    for i in range(200):
        print(i + 1, res_all[i][0], res_all[i][1], "[user:" + res_all[i][2] + "]")
        fw.write(
            "| {} |  {} | {} | [user: {}]|\n".format(
                i + 1, res_all[i][0], res_all[i][1], res_all[i][2]
            )
        )
    fw.write("\n")
    fw.write("\n")

print()
print()

res_india = []
with open("codeforces_users.json") as json_file:
    lit = json_file.read()
    data = ast.literal_eval(lit)
    for acc in data["result"]:
        if "country" in acc and acc["country"] == "India":
            res_india.append((acc["maxRating"], acc["country"], acc["handle"]))

res_india = sorted(res_india, key=lambda x: -x[0])

with open("README.md", "a") as fw:
    for i in range(200):
        print(i + 1, res_india[i][0], res_india[i][1], "[user:" + res_india[i][2] + "]")
        fw.write(
            "{} {} {}".format(
                i + 1,
                res_india[i][0],
                res_india[i][1],
                "[user:" + res_india[i][2] + "]",
            )
            + "\n"
        )
    fw.write("\n")
    fw.write("\n")
