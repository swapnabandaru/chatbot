from botfn import get_answer

ds= {'hi':['hello','hey','hi! good morning.'],
'hello':['hi','hey there','hello! how are you?'],
'how are you':['I am great','okay.what about you'],
'i am good':['oh thats great to hear','awesome!'],
'what is your name':['chatbot','chatterbot','bot-bot'],
'what is your fathers name':['ross','jim','jo'],
'bye':['okay! bye.','bye. have a good day','bye bye']}

while(1):
	user_input=raw_input("User: ")
	get_answer(user_input,ds)