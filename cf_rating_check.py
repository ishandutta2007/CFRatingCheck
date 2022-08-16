import urllib.request, json

only_active = "false"
query = "https://codeforces.com/api/user.ratedList?activeOnly=" + only_active + "?lang=en"
with urllib.request.urlopen(query) as url:
	data = json.loads(url.read().decode())
	print(data)
Statistic outputter:

import ast

european_countries = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom"];

res = []
with open('codeforces_users.json') as json_file:
	lit = json_file.read()
	data = ast.literal_eval(lit)
	for acc in data['result']:
		# if 'country' in acc and acc['country'] in european_countries and acc['country'] != "Russia":
		# 	res.append((acc['maxRating'], acc['country'], acc['handle']))
		if 'country' in acc:
			res.append((acc['maxRating'], acc['country'], acc['handle']))
		else:
			res.append((acc['maxRating'], "Unknown", acc['handle']))
			
res = sorted(res, key=lambda x: -x[0])
for i in range(200):
	print(res[i][0], res[i][1], "[user:" + res[i][2] + "]")
