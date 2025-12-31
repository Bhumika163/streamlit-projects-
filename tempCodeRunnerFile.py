import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data  = response.json()
    for post in data:
        print(data[11])
        
else:
    print("Failed with status:", response.status_code)    