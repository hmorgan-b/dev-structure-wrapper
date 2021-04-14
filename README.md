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

