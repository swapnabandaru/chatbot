import random

def get_answer(user_input,ds):
	new_user_input=user_input.split()
	count1=0
	question=""
	for k in ds:
		tokens=k.split()
		count2=0	
		for token in tokens:
			if token in new_user_input:
				count2=count2+1
		if count2>count1:
			question=k
			count1=count2
	if not question:
			print "Bot: Sorry. I did not understand you. "
	else:
			print "Bot: %s" % (random.choice(ds[question]))