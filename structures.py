
# Import requests library
import requests
import argparse
import sys, os
from dotenv import load_dotenv

load_dotenv()


def parse_args(args):
    """
    This method is used to define and parse the command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s',
                        '--service',
                        default='health',
                        choices=['health', 'structure'],
                        help=("Specify the service you'd like to perform"
                              "within structures service (endpoint)")
                        )
    parser.add_argument('-f',
                        '--filename',
                        default=None,
                        help=("Specify the structures csv file"
                              "to be uploaded to structures service.")
                        )
    args_, unknown = parser.parse_known_args(args)
    args = vars(args_)
    return args


def wrapper(args):
    """
    This function takes in command line arguments and performs requests
    as requested by user
    """
    # Handle health check requests
    if args['service'] == "health":
        
        endpoint = '/actuator/health'
        url = os.getenv('URL') + endpoint
        r = requests.get(url=url)
        data = r.json()
        print(data)
        return

    # If service is any other, we need a file from uploads folder
    else:
        # Ensure a filename is given
        if args['filename'] is None:
            print("Please provide a filename to upload.")
            return
        else:
            print(f"Uploading file: {args['filename']} to structures service.")

    # Get endpoint to add to URL depending on service request (only 1 upload endpoint now)
    if args['service'] == 'structure':
        endpoint = '/load'

    # Build final URL with appropriate endpoint
    url = os.getenv('URL') + endpoint

    # Build file dict to pass to requests
    try:
        files = {
            'file': open('uploads/' + args['filename'], 'rb')
        }
        r = requests.post(url, files=files)
        data = r.json()
        print(data)

    except FileNotFoundError:
        print(f"ERROR: No file named {args['filename']} found in uploads folder.")


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    wrapper(args)