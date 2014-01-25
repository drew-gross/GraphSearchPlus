from django_cron import cronScheduler, Job

class GetTurkResults(Job):

	run_every = 300

	def job(self):
		key = os.environ['AWS_ACCESS_KEY_ID']
		secret = os.environ['AWS_SECRET_ACCESS_KEY']
		conn = boto.connect_mturk(key, secret, host='mechanicalturk.sandbox.amazonaws.com')
		done_hits = conn.get_reviewable_hits()
		for done_hit in done_hits:
			assignment = conn.get_assignments(done_hit.HITId)[0]
			if assignment.AssignmentStatus == 'Submitted':
				conn.approve_assignment(assignment.AssignmentId)
				form_response = assignment.answers[0][0]
				scandalous = form_response.fields[0] == 'yes'
				print(scandalous)

cronScheduler.register(GetTurkResults)