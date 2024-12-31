import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL
url = "https://example.com/booking"

# Step 2: Fetch the HTML content
response = requests.get(url)

if response.status_code == 200:
    # Step 3: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 4: Locate the booking table
    table = soup.find('table', {'id': 'bookingTable'})  # Replace 'id' or other attributes as needed

    if table:
        # Step 5: Extract all rows from the table
        rows = table.find_all('tr')
        available_slots = []

        # Step 6: Iterate through rows
        for row in rows[1:]:  # Skip the header row
            columns = row.find_all('td')  # Extract columns from the row
            
            if len(columns) >= 3:  # Ensure the row has the expected number of columns
                time = columns[0].text.strip()  # Time column
                date = columns[1].text.strip()  # Date column
                status = columns[2].text.strip()  # Status column
                
                # Step 7: Check if the slot is available
                if status.lower() == "available":
                    available_slots.append(f"{date} at {time}")

        # Step 8: Display the result
        if available_slots:
            print("Available slots:")
            for slot in available_slots:
                print(slot)
        else:
            print("No available slots found.")
    else:
        print("Booking table not found on the page.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
