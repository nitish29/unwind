# Unwind
As the name suggests, use unwind to plan out your day!

Unwind uses **Eventbrite's API** to display different event categories to users. As of now, a user can select only upto **3** event categories. Based on the categories selected, a curated list of all the events pertaining to the selected categories are displayed.

**Demo Link:** http://52.34.17.82/

---

## Installation Steps

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

---

## Project Directory Structure
	
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
---

## More about views.py

This application makes use of **4** view **_functions_** to display data to the user.

- home 
	- This function makes a call to fetchEventbriteCategories function in order to fetch a list of all the categories to be presented to the user on the home page. Once all the data is fetched, it is santized into a format that the django templating engine can understand and passed to *categories.html* template. 

- events
	- This function makes a call to the fetchEventbriteEvents function in order to get a list of all the events corresponding to categories selected by the user. The data fetched is santized and passed to *events.html* template.

- fetchEventbriteCategories 
	- This function makes a call to the Eventbrite API's **Categories** endpoint to get a _JSON_ response object of all the categories.
	  The query parameters passed to the endpoint are:
	  	- token: Personal OAuth token issued by Eventbrite.

- fetchEventbriteEvents
	- Function arguments:
		- category_string: A comma separated string of category ids.
		- page: The event page number to be fetched using the API endpoint. 

	- This function makes a call to the Eventbrite API's **Events** endpoint to get a _JSON_ response object of all the events corresponding to requested category ids. A call to specifically this endpoint is made - **_/events/search/_**. The query parameters passed to the endpoint are:
	  	- categories: The value for this parameter is a comma separated category id string. eg: (*categories=1,2,3*)
	  	- token: Personal OAuth token issued by Eventbrite.
	  	- page: The event page number to be fetched using the API endpoint.
	 
---
