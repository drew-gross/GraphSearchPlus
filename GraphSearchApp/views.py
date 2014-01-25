from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.context import Context

# turk related stuff.

import os
import boto

key = os.environ['AWS_ACCESS_KEY_ID']
secret = os.environ['AWS_SECRET_ACCESS_KEY']
conn = boto.connect_mturk(key, secret, host='mechanicalturk.sandbox.amazonaws.com')

def make_hit(url, query):
	html = render_to_string('turkerview.html', Context({'description':query,'img_src':url}));
	question = boto.mturk.question.HTMLQuestion(html, 800)
	return conn.create_hit(question=question, title="Determine if an employer would disqualify a candidate based on an image", reward=0.01)

def login(request):
	return render(request,'login.html')

def main(request):
	if not request.user.is_authenticated():
		return redirect("/login/")

	fb = request.user.get_offline_graph()
	photos = fb.get('me/photos')
	for photo in photos['data']:
		make_hit(photo['source'], "who is dumb")

	return render(request,'main.html')

def turkerview(request):
	process_hits();
	return HttpResponse("thanks!")