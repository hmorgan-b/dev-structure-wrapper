
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
                        default='upload',
                        choices=['upload', 'health'],
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
        r = requests.get(url = url)
        data = r.json()
        print(data)

    # Handle file uploads
    if args['service'] == 'upload':

        # Build url with env var and endpoint
        endpoint = '/structures'
        url = os.getenv('URL') + endpoint

        # Ensure a filename is given
        if args['filename'] is None:
            print("Please provide a filename to upload.")
            return

        else:
            print(f"Processing file {args['filename']} to upload.")

            # Build file dict to pass to requests
            files = {
                'file': open('uploads/' + args['filename'], 'rb')
            }

            r = requests.post(url, files=files)
            data = r.json()
            print(data)




if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    wrapper(args)