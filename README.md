# Wrapper for Structures Service - Endpoint Tool

This is a tool built to interact with the DNA Apps Team Structures Service.
It enables the user to call various endpoints within the structures service via command line Python script, rather than having to submit verbose CURL commands.

## Setup 

To use this tool, setup should be quick and painless. Follow the following steps to get this tool ready to be used locally on your machine.

### 1. Clone the repository to your local machine.
Open up a terminal and go to the location you want to run the tool from, then copy the repository to that location.
```shell
git clone git@github.com:hmorgan-b/dev-structure-wrapper.git
```

From the command line, move into the location where you copied this repository to.
```shell
cd dev-structure-wrapper/
```

Here, you should see the following contents, at a minimum:
```properties
|-- README.md
|-- structures.py
|-- .env
|-- requirements.txt
|-- uploads/
    |-- README.md
```

### 2. Set Python version and create virtual environment

This tool requires Python 3.8 to run, so first set the Python version
```shell
pyenv shell 3.8.0
```

Next, create a virtual environment within the root directory of the project
```shell
python -m venv venv
```

### 3. Activate virtual environment and install dependencies
There should now be a folder within the project named `venv/`. Now, you need to activate the virtual environment via the following command:
```shell
source venv/bin/activate
```
Then, install the dependencies, which are located in the requirements.txt file
```shell
pip install -r requirements.txt
```
### 4. Verify the URL points to the Structures Service
The .env file should contain an environment variable pointing to the URL that the Structures Service is running on. For the dev instance, this is:
```editorconfig
URL=https://api.dev.az.eagleinvsys.com/svc-appstm-structure
```
This should automatically be populated, but this step is included just as a check, and a notice that it can be changed to point to any version of the Structures Service that is running.
If you are running the Structures Service locally, and want to point this wrapper to your local instance of the structures service, update this variable to the URL of your local version.

## Use

There are different command line arguments that can be passed to handle different uploads or call different endpoints within the Structures Service. This tool so far is set up for the following:
1. [Perform a health check](#1-perform-a-health-check)
2. [Upload a new structure](#2-upload-a-new-structure)
3. [Upload a new map](#3-upload-a-new-map)
4. [Upload new level 0 structure](#4-upload-new-level-0-structure)

### 1. Perform a health check
To verify that you've set this tool up correctly, run the following from the command line within the directory where you cloned the repository:
```shell
python -m structures -s health
```
The response returned should look like this:
```shell
{ 'status': 'UP' }
```
If it does not, review the steps above to ensure you've setup the tool correctly.

### 2. Upload a new structure

Add the CSV file containing the new structure information to the `uploads/` directory within this project.

Once the file is in this folder, you can run the following command from the terminal:
```shell
python -m structures -s structure -f filename.csv
```

If upload is successful, the response should look like this:
```shell
{'data': 'OK', 'status': 'success'}
```

### 3. Upload a new map
Add the CSV file containing the new mapping file to the `uploads/` directory within this project.

Once the file is in this folder, you can run the following command from the terminal:
```shell
python -m structures -s map -f filename.csv
```

If upload is successful, the response should look like this:
```shell
{'data': 'OK', 'status': 'success'}
```

### 4. Upload new level 0 structure
Level 0 structures are treated differently than the rest of the structures uploaded, so it has it's own endpoint. To upload a new level 0 structure,
add the CSV file containing the level 0 structure information to the `uploads/` directory within this project.

Once the file is in this folder, you can run the following command from the terminal:

```shell
python -m structures -s level0 -f filename.csv
```

If upload is successful, the response should look like this:
```shell
{'data': 'OK', 'status': 'success'}
```

## Common Errors
If the file can't be opened, or isn't found within the `uploads/` directory, you will get the following response:
```
ERROR: No file named <file.txt> found in uploads folder.
```
If your file has spaces in the filename - you need to call the command with the filename in between quotes.

For example, a file named `new level 0.csv` would be uploaded by the following command:
```shell
python -m structures -s level0 -f "new level 0.csv"
```