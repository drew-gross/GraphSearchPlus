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

def process_hits():
	done_hits = conn.get_reviewable_hits()
	for done_hit in done_hits:
		assignment = conn.get_assignments(done_hit.HITId)[0]
		if assignment.AssignmentStatus == 'Submitted':
			conn.approve_assignment(assignment.AssignmentId)
			form_response = assignment.answers[0][0]
			scandalous = form_response.fields[0] == 'yes'
			print(scandalous)

def make_hit(url, query):
	html = render_to_string('turkerview.html', Context({'description':query,'img_src':url}));
	question = boto.mturk.question.HTMLQuestion(html, 800)
	return conn.create_hit(question=question, title="Determine if an employer would disqualify a candidate based on an image", reward=0.01)

def login(request):
	if request.user.is_authenticated():
		redirect("/")
	return render(request,'login.html')

def main(request):
	if not request.user.is_authenticated():
		redirect("/login/")

	return render(request,'main.html')

def turkerview(request):
	#make_hit('https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-prn1/t1/1016702_10200553764261376_1292186779_n.jpg', "who is dumb")
	process_hits();
	return HttpResponse("thanks!")