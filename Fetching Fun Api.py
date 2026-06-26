import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def facts():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Interesting fact, did you know {data['text']}.")
    else:
        print("Error 404, failed to find question")
    
while True:
    user_input = input("Press q if you want to exit.")
    if user_input.lower() == 'q':
        break
    
    facts()
    
        