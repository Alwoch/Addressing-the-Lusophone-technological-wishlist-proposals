import csv
import concurrent.futures

import requests

CSV_FILE = "urls.csv"


def get_status_code(url):
    """
    makes a request to a url and prints the status code and url

    Args:
        - url (string): url to which a request is to be made

    Returns:
        - (STATUS CODE) URL : when a request is successfully made
        - (None) URL : when a request connection to the url fails
    """
    try:
        response = requests.get(url)
        status_code = response.status_code
    except requests.exceptions.RequestException as e:
        # get the status code of the error if it provides a response
        status_code = e.response.status_code if e.response else None

    print(f"({status_code}) {url}")


def process_csv(csv_file):
    """
    reads the csv file and prints its status codes and urls

    Args:
        - csv_file : csv file containing urls to be read

    Returns:
        - (STATUS CODE) URL : when a request is successfully made
        - (None) URL : when an a request connection to the url fails
    """
    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        urls=[row[0] for row in csv_reader]

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(get_status_code, urls)


if __name__ == "__main__":
    process_csv(CSV_FILE)
