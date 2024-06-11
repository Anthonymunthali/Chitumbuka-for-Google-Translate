import requests
from bs4 import BeautifulSoup


def fetch_url_text(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract and return the text from the HTML
        return soup.get_text()

    except requests.exceptions.RequestException as e:
        # Handle any exceptions (e.g., network problems, invalid URL)
        return f"An error occurred: {e}"


if __name__ == "__main__":
    # Prompt the user to enter a base URL with a placeholder for the page number
    base_url = input("Enter a base URL with a placeholder for the page number (e.g., 'https://example.com/page/{}'): ")

    # Prompt the user to enter the number of pages
    num_pages = int(input("Enter the number of pages to fetch: "))

    for page_num in range(1, num_pages + 1):
        # Format the URL with the current page number
        url = base_url.format(page_num)

        # Fetch the text from the URL
        page_text = fetch_url_text(url)

        # Print the page number and the text
        print(f"\n\n=== Page {page_num} ===\n")
        print(page_text)
