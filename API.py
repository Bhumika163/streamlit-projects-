import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data  = response.json()
    print("first  10 posts:")
    for i in range(10):
        print(data[i])
       
        
else:
    print("Failed with status:", response.status_code)    