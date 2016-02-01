from urllib.request import Request, urlopen
import urllib.parse
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import pdb
#import logging
#import simplejson
#import itertools


def home(request):
	try:
		errors = []

		data_fetched_from_api = fetchEventbriteCategories()

		if data_fetched_from_api['status'] == "success":

			categories = data_fetched_from_api['data']["categories"]
			

		else:
			errors.append(data_fetched_from_api['errors'])
			raise Exception(errors)

		if not errors:
			context = { 'categories' : categories }
			
		else:
			errors.append('Error fetching API details')
			#response = HttpResponse(json.dumps({'status': 'failure','message': errors}), content_type="application/json")
			raise Exception(errors)

	except:
		errors.append('Error Completing request')
		context = { 'errors' : errors }

	return render(request, "categories.html", context)


def fetchEventbriteCategories():
	
	try:
		errors = []

		request_params = urllib.parse.urlencode({'token': settings.EVENTRBRITE_TOKEN})
		url = settings.EVENTBRITE_BASEURL + 'categories/'
		request = Request(url + '?' + request_params)
		response = urlopen(request)
		content = response.read()
		decoded_content = json.loads(content.decode())

		response = {'status': 'success', 'data' : decoded_content }

	except:
		errors.append('Error fetching categories from Eventbrite API')
		response = {'status': 'failure','errors': errors}

	return response

def fetchEventbriteEvents(category_string):
	try:
		#pdb.set_trace()
		errors = []
		request_params = urllib.parse.urlencode({'token': settings.EVENTRBRITE_TOKEN, 'categories': category_string})
		url = settings.EVENTBRITE_BASEURL + 'events/search/'
		request = Request(url + '?' + request_params)
		response = urlopen(request)
		content = response.read()
		decoded_content = json.loads(content.decode())

		response = {'status': 'success', 'data' : decoded_content }

	except:
		errors.append('Error fetching categories from Eventbrite API')
		response = {'status': 'failure','errors': errors}

	return response



def search(request):
	try:
		errors = []

		category_id_list = request.GET.getlist('category_id')
		category_string = ', '.join(category_id_list)

		data_fetched_from_api = fetchEventbriteEvents(category_string)
		
		if data_fetched_from_api['status'] == "success":

			events = data_fetched_from_api['data']['events']
			page_count = data_fetched_from_api['data']['page_count']
			

		else:
			errors.append(data_fetched_from_api['errors'])
			raise Exception(errors)

		if not errors:
			context = { 'events' : events, 'page_count': page_count }
			
		else:
			errors.append('Error fetching API details')
			raise Exception(errors)



	except:
		errors.append('Error fetching events from Eventbrite API')
		context = { 'errors' : errors }

	return render(request, "events.html", context)
	#https://www.eventbriteapi.com/v3/events/?categories=113,107&token=5U4JRY2Q6QYB4HZMNS3K&price=free