# aws-metadata-json

## What it does
- Query the metadata of an ec2 instance within AWS and provide a json formatted output. 
- Retrieve the value of a particular data key.

## How to install
- [Create an EC2 Linux instance on AWS]
- [SSH into the instance]
- Install Python 3 and git on your instance 
    - `sudo yum install python3 git`
- Craete a folder with name "aws-metadata-json" @ EC2 instance 
- Place the shared folder at the ec2 instance 
- Install pipenv
  - `sudo pip3 install pipenv`
- Open the repository on your instance
  - `cd aws-metadata-json`
- Install project dependancies
  - `pipenv install`


## How to run
- Open the `src` folder
  - `cd aws-metadata-json/src`
- Run whichever script you need:
  - `python3 get_metadata.py`
  - `python3 get_key.py`

## How it works
- It makes use of the http://hostmachine/latest/meta-data link-local address. Instance metatada is provided at this link, but only when you visit it from a running instance.
