import requests

# Make a request to https://<ENTER WEBSITE URL OF INTEREST>
# Store the result in 'res' variable
res = requests.get(
    'https://<ENTER WEBSITE URL OF INTEREST>')
txt = res.text
status = res.status_code

print(txt, status)
# print the result
