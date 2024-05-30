import requests

# Define the text you want to classify
text ="دخيلك لا تتركني هيك "

# Define the URL of the Flask API endpoint
url = "http://127.0.0.1:5000/predict"

# Create a JSON payload
payload = {"text": text}

# Send a POST request to the API endpoint
response = requests.post(url, json=payload)

# Print the response status code
print("Response Status Code:", response.status_code)

# Print the response content
print("Response Content:", response.text)
