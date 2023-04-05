import requests

response = requests.get("http://localhost:8080/api/pet/findByStatus?status=available")
print(response.status_code)


url = "http://localhost:8080/api/pet"
params = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "DoggieDog"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "DoggieDog"
    }
  ],
  "status": "available"
}

req_post = requests.post(url, json=params)
print(req_post.status_code)