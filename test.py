import requests 

hash_microservice_url = "http://localhost:3000/hash"

def hashing_service():
    test_cases = [
        {"input": "hello world", "hash": "sha1"},
        {"input": "hello world", "hash": "sha256"},
        {"input": "hello world"}
    ]

    for case in test_cases:
        response = requests.post(hash_microservice_url, json=case)
        assert response.status_code == 200, f"Status code not 200: {response.status_code}"  # test assertion for 200 
        result = response.json() 
        assert "hash" in result, f"No hash returned in response: {result}"                  # return boolean if hash exists in result 
        print(f"Input: {case['input']}, Algorithm: {case.get('hash', 'sha256')}, Hash: {result['hash']}")

if __name__ == "__main__":
    hashing_service()
