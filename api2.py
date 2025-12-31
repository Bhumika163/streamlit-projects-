import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

users = [
    {"userId": 1, "id": 1, "title": "post 1", "body": "this is new post for 1."},
    {"userId": 2, "id": 2, "title": "post 2", "body": "this is new post for 2."},
    {"userId": 3, "id": 3, "title": "post 3", "body": "this is new post for 3."}
]

for user in users:
    response = requests.post(url,json=user)
    print("Status Code:", response.status_code)
    print("response :", response.json())

       
        
   
