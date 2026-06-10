import requests
from lib.generate_log import generate_log

def fetch_data():
    """Fetches data from a public API."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    return {}

if __name__ == "__main__":
    # Fetch data from the API
    post = fetch_data()

    # Prepare log data
    title = post.get("title", "No title found")
    log_data = [
        "User logged in",
        f"Fetched Post Title: {title}",
        "Report exported"
    ]

    # Generate the log file
    generate_log(log_data)
