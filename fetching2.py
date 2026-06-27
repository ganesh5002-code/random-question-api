import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def fetch_fact():
    endpoint = requests.get(url)
    try:
        if endpoint.status_code == 200:
            data = endpoint.json()
            print(f"Interesting facts: Did you know {data['text']}")
            
        else:
            print(f"Error {endpoint.status_code}: Failed to fetch data from the server.")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error: Could not connect to the API. ({e})")



# Main interactive loop
while True:
    user_input = input("Select a a key to start. If you want to quit, press 'q'")
    
    if user_input.lower() == 'q':
        print("Bye!")
        break
        
    fetch_fact()
