import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = 'https://book.stadeiga.com/courtbooking/home/calendarDayView.do?id=16'
response = requests.get(url)


login_url = "https://book.stadeiga.com/courtbooking/login"
target_url = "https://book.stadeiga.com/courtbooking/home/calendarDayView.do?id=16"

# Replace with your credentials
payload = {
    "username": "adam.daudrich@pm.me",
    "password": "a95b5c42"
}


# Create a session to maintain cookies
session = requests.Session()
session.post(login_url, data=payload)

# Access the target page
response = session.get(target_url)

print(response.text)



# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the headings (e.g., <h1> tags)
headings = soup.find_all('td')

# Print each heading's text content
for heading in headings:
    print(heading.text)
headings = soup.find_all('td')