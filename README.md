# unwind
As the name suggests, use unwind to plan out your day!

# unwind Installation Steps

- Install Virtual Env and Virtual Env wrapper

- Make a new virtual env with python version as 3.5
	
	- mkvirtualenv --python=(*path to your python3.5 installation directory*) (*name of virtual enviornment*)
	- eg : **mkvirtualenv --python=/usr/local/bin/python3.5 unwind**

- activate the virtual environment that you have made

- sudo pip install -r requirements.txt
	
	- in case you face problem installing psycopg2 , try installing it with this command instead _pip3.5_ _install_ _psycopg2_

- install postgres database and create a new database

- make a copy of local_settings.py.sample file from nongit folder and move it to unwind folder

- rename this file copied file to **local_settings.py** 

- change all these database parameters: NAME,USER,PASSWORD,PORT,HOST as per your postgres database setup

- run the migrate command, to add/update database schema tables: python manage.py migrate 

- type the following command using command line - python manage.py runserver 0:8000 

- open browser and type localhost:8000, you should see the default django page

#Project Directory Structure
	
	Unwind/
      |--nongit/
      |  |--local_settings.py.sample
      |--static/
      |  |--css/
      |     |--materialize.css
      |     |--materialize.min.css
      |     |--style.css
      |  |--font/
      |  |--images/
      |  |--js/
      |     |--init.js
      |     |--materialize.js
      |     |--materialize.min.js
      |
      |--templates/
      |  |--categories.html
      |  |--documentation.html
      |  |--events.html
      |  |--index.html
      |
      |--unwind/
      |  |--local_settings.py
      |  |--settings.py
      |  |--urls.py
      |  |--views.py
      |  |--wsgi.py
      |
      |--.gitignore
      |--manage.py
      |--README.md
      |--requirements.txt