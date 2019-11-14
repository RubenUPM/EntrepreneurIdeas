## Summary
Sample project that will try to host the ideas of Entrepreneurs.
Please follow the steps described in this guide to launch the 
application.

# Contents
* [Installation guide](#installation-guide)
	* [Virtualenv](#virtualenv)
	* [Requirements](#requirements)
* [How To Launch It](#how-to-launch-it)
* [Important web pages](#important-web-pages)

## Installation guide <a name="installation-guide"></a>
This guide will show you how to install all the necessary data to run this project.

### Virtualenv <a name="virtualenv"></a>

Install **virtualenv** that use python3:
* virtualenv -p python3 venv 

This will install a virtual environment which directory name is venv.

**Source** the virtual environment:
* source venv/bin/activate 

### Requirements <a name="requirements"></a>

To install the requirements simply run:  

pip install -r requirements.txt

## How to launch it <a name="how-to-launch-it"></a>

To launch it simply run:  

python manage.py runserver

## Important web pages <a name="important-web-pages"></a>

By default the server is host in:   

http://127.0.0.1:8000

Admin web page:  

http://127.0.0.1:8000/admin/  

* Admin credentials:
    * USER:ruben - PASS:ruben1234

Home web page:   

http://127.0.0.1:8000/home/ 
