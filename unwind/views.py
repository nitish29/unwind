from urllib.request import Request, urlopen
import urllib.parse
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import pdb



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

def fetchEventbriteEvents(category_string,page):
	try:
		#pdb.set_trace()
		errors = []
		request_params = urllib.parse.urlencode({'token': settings.EVENTRBRITE_TOKEN, 'categories': category_string, 'page' : page})
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
		#pdb.set_trace()
		category_id_list = request.GET.getlist('category_id')
		if request.GET['page_no']:
			page_s = request.GET['page_no']
		category_string = ', '.join(category_id_list)
		query=""
		for ids in category_id_list:
			query += 'category_id=' + ids + '&' 
		query = query[:-1]
		data_fetched_from_api = fetchEventbriteEvents(category_string,page_s)
		
		if data_fetched_from_api['status'] == "success":

			events = data_fetched_from_api['data']['events']
			page_count = data_fetched_from_api['data']['pagination']['page_count']
			loop_times = range(1, page_count+1)
			page_no = data_fetched_from_api['data']['pagination']['page_number']
			next_page = int(page_no) + 1
			

		else:
			errors.append(data_fetched_from_api['errors'])
			raise Exception(errors)

		if not errors:
			context = { 'events' : events, 'page_count': page_count, 'loop_times': loop_times, 'page_no': page_no, 'query': query, 'next_page': next_page }
			
		else:
			errors.append('Error fetching API details')
			raise Exception(errors)



	except:
		errors.append('Error fetching events from Eventbrite API')
		context = { 'errors' : errors }

	return render(request, "events.html", context)

