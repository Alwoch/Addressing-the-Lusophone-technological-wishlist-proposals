import csv
import requests

CSV_FILE = 'urls.csv'

def get_urls_from_csv(csv_file):
    """
    read the csv file and gets the urls

    Args:
        - csv_file : csv file containing urls to be read

    Returns:
        - url: url string
    """
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            yield row[0]


def get_status_code(url):
    """
    makes a request to a url and prints the status code and url

    Args:
        - url (string): url to which a request is to be made

    Returns:
        - (STATUS CODE) URL : when a request is successfully made
        - Error URL : when an a request fails
    """
    try:
        response = requests.get(url)
        status_code = response.status_code
        print(f"({status_code}) {url}")
    except requests.exceptions.RequestException:
        print(f"(Error) {url}")


if __name__ == "__main__":
    for url in get_urls_from_csv(CSV_FILE):
        get_status_code(url)
