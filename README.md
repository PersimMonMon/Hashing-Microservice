# Hashing Microservice
A HTTP microservice written in Go that computes SHA-1 or SHA-256 hash from JSON POST requests.

## How to Run the Hash Microservice
Enter in terminal go run main.go and it'll start a server on http://localhost:3000/hash 

## How to REQUEST Data 
|Field  |  Type    |  Required  |  Description--------------------------------------|
|-------|----------|------------|---------------------------------------------------|
|input  |  string  |  Yes       |  The string you want to hash----------------------|
|hash   |  string  |  No        |  Takes in "sha1" or "sha256" (defaults to sha256)-| 

Example Call (Python) 
  import requests
  url = "http://localhost:3000/hash"

  payload = {
    "input": "hello world",
    "hash": "sha1"
  }

  response = requests.post(url, json=payload)
  print(response.json())

## How to RECEIEVE Data
The service will respond with JSON containing: 
{"hash": "computed_hash"}

Example Call (Python)
  import requests
  url = "http://localhost:3000/hash"
  response = requests.post(url, json={"input": "hello world"})

  if response.ok:
    data = response.json()
    print("Hash computed:", data["hash"]
  else:
    print("Error:", response.text)



Notes: You may see the test.py file for a full example of what sending and receiving data would look like if implementing to a python program. 
