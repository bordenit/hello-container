import requests

def fetch_path(route):
    try:
        # Fetch content from the Flask web server running on container1
        response = requests.get(f'http://server:5000{route}')
        response.raise_for_status()  # Raise an error for bad status codes
        print(response.text)  # Print the content of the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")

if __name__ == "__main__":
    fetch_path("/")
    fetch_path("/skills")
    fetch_path("/weaknesses")
    fetch_path("/finalthought")