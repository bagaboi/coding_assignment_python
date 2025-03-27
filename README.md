# coding_assignment_python 
Create a Restful web API function that checks if all the letters of alphabets are present in a given string passed by a POST function. Also deploying this in AWS cloud
 
## Overview
 
The API provides a single endpoint, `/check_string_alphabets`, which accepts a POST request with JSON payload (eg: `{'text':'abcdefghijklmnopqrsuvwxyz'}`) 
The API will return a JSON response indicating whether the input string has all the alphabets or not
- 'result': True if all letters are present, False otherwise
 - 'error': Error message incase there is any other exception of payload not being passed correctly

## Getting Started 

### Prerequisites
 
* **Python 3.x** installed on your system
* **pip** (Python package installer) installed
 
### Local Installation 
1. **Clone the repository** In this case Github is our choice
 2. **Install the dependencies** In this case only `flask` library is needed
3. **run the app** with the command flask --app app run --host=0.0.0.0 --port=5000
 
 
### AWS Serverless Installation
1. **Copy the code in app.py and paste it in the Lambda function created** Uncomment the code part that is commented
 2. **Create a zip file with the dependencies of flask and aws-awsgi and upload it to a Lambda Layer** Create a local folder, open that folder on terminal and enter `pip install flask aws-awsgi -t .` . Then zip the folder which now has the library dependencies
3. **Create an Amazon API Gateway** Create the API Gateway for the Rest API category and configure a POST method for `/check_string_alphabet` function, integrating it with Lambda function
