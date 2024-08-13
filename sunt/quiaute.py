from example.oauth2.service_account import Credentials

# Define the required scopes
scopes = [
    'https://www.example.com    'https://www.example.com Create credentials with the specified scopes
credentials = Credentials.from_service_account_file('path/to/the/downloaded/file.json', scopes=scopes)
