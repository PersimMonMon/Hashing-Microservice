# Hashing Microservice
A HTTP microservice written in Go that computes SHA-1 or SHA-256 hash from JSON POST requests.

## How to Run the Hash Microservice
Enter in terminal go run main.go and it'll start a server on http://localhost:3000/hash 

## Communication Contract
|Field  |  Type    |  Required  |  Description                                      |
|-------|----------|------------|---------------------------------------------------|
|input  |  string  |  Yes       |  The string you want to hash                      |
|hash   |  string  |  No        |  Takes in "sha1" or "sha256" (defaults to sha256) | 

## How to REQUEST Data 
Example Call (Python) 
```python
  import requests
  url = "http://localhost:3000/hash"

  payload = {
    "input": "hello world",
    "hash": "sha1"
  }

  response = requests.post(url, json=payload)
  print(response.json())
```

What this does 
  -Sends a POST request with the input "hello world"  
  -Request the hash to be computed using SHA-1  
  -Receives back a JSON object containing the computed hash   
  -Takes in the fields "input" and "hash". Where "input" is a string that's required and "hash" is a string not required. 

How it is being used      
  -This expample shows basic usage of the microservice, the client determines which hashing algorithm to use   
  -Useful when the user needs a specific hash type (for example, SHA-1 for legacy systems)    
  -Demostrates how to structure a valid JSON request for the /hash endpoint   
  -Helps developers understand how to override the default hashing behavior by giving the "hash" input field   

Notes/Reminders: The program will default to SHA256 if users do not specify an input for "hash". 

## How to RECEIEVE Data
The service will respond with JSON containing: 
{"hash": "computed_hash"}

Example Call (Python)
```python
  import requests
  url = "http://localhost:3000/hash"
  response = requests.post(url, json={"input": "hello world"})

  if response.ok:
    data = response.json()
    print("Hash computed:", data["hash"])
  else:
    print("Error:", response.text)
```

What this does
  -Sends "hello world" with no hash algorithm specified  
  -The service automatically uses SHA-256  
  -If successful, it prints the computed hash  
  -If an error occurs, it prints the server's error message.   
  -Takes in the fields "input" and "hash". Where "input" is a string that's required and "hash" is a string not required.   

How it is being used       
  -This example illustrates default behavior of the microservice when "hash" is not provided.     
  -Useful when the user doesn't care which algorithm is used or prefers the more secure SHA-256    
  -Shows developers how to safely check for successful responses (response.ok)    
  -Helps users understance how to integrate this service into applications where SHA-256 is the standard    

## UML Sequence Diagram
<img width="671" height="466" alt="image" src="https://github.com/user-attachments/assets/eddc9e08-46ff-4451-a1df-656afb69efda" />


Notes: You may see the test.py file for a full example of what sending and receiving data would look like if implementing to a python program. 
