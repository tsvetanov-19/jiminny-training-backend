# Installation
Clone this repo to your machine.

You need python3 with activated virtual environment to run this project

## How to install virtualenv:

### Install **pip** first

    sudo apt-get install python3-pip

### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

### Now create a virtual environment 

    virtualenv venv 
    
### Active your virtual environment:    

    source venv/bin/activate

### To deactivate:

    deactivate
## Configuration
In order to set custom file location for user-channel or customer-channel files
 
 change variables in lines `7` and `8`  in `main.py` 
```python
CUSTOMER_DATAFILE = 'https://raw.githubusercontent.com/jiminny/join-the-team/master/assets/customer-channel.txt'
USER_DATAFILE = 'https://raw.githubusercontent.com/jiminny/join-the-team/master/assets/user-channel.txt'
```
## Running
```python 
python main.py
```