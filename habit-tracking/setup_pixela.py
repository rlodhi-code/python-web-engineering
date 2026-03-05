# run this program to create pixela token only one time.
import requests
import secrets

USERNAME = "Enter Your Username"  # it will become part of https://pixe.la/@Username
TOKEN = secrets.token_urlsafe()
GRAPH_ID = "cycling1"

# Generate secure token
TOKEN = secrets.token_hex(16)

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print("User creation response:", response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print("Graph creation response:", response.text)

print("\nSAVE THESE VALUES IN YOUR .env FILE\n")
print(f"PIXELA_USERNAME={USERNAME}")
print(f"PIXELA_TOKEN={TOKEN}")
print(f"PIXELA_GRAPH_ID={GRAPH_ID}")