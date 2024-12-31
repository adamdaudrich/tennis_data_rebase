import requests
from bs4 import BeautifulSoup

login_url = "https://book.stadeiga.com/courtbooking/home/login.do"
clay_url = "https://book.stadeiga.com/courtbooking/home/calendarDayView.do?id=18"


# "/calendarDayView.do?id=18&iYear=2024$Month=11&iDate=31"
# month 11 = december

#get a request code back
try:

    response = requests.get(login_url)
    print(f"status code: {response.status_code}")

        # Optional: Additional status code handling
    if response.status_code == 200:
        print("Success: The request was successful.")
    else:
        print("Received an unexpected status code.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


# attempt login
payload = {
    "userId": "adam.daudrich@pm.me",
    "Password": "a95b5c42"
}

# # Create a session to maintain cookies
session = requests.Session()
session.cookies.clear()
login_response = session.post(login_url, data=payload)


if login_response.status_code == 200:
    print("Login successful!")

    # Access another authenticated page
    target_response = session.get(clay_url)
    print(target_response.text)
else:
    print("Login failed!")

