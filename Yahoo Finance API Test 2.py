import json
import requests

#the URL for a part of the API
response = requests.get("https://query2.finance.yahoo.com/v10/finance/quoteSummary/AAPL?modules=financialData")

#converts request to json
data = response.text
parsed = json.loads(data)

#to print the full request remove the # in front of this next line
#print(json.dumps(parsed, indent=4))

#the request main API directory
resultsDirectory = parsed['quoteSummary']['result'][0]

#the specific data point request from the API directory
dataPoint = resultsDirectory['financialData']['debtToEquity']['fmt']
print(dataPoint)