import requests

def get_user_data(user_id):
    # This URL is a fake API that returns JSON data
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        # .json() converts the text response into a Python Dictionary
        data = response.json()
        print(f"User Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"City: {data['address']['city']}")
    else:
        print("User not found!")

# Test it
get_user_data(1)