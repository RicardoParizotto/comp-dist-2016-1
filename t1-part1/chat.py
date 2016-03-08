from bottle import run, get, post, view, request, redirect

messages = [("Nobody", "Hello!")]

@get('/')
@view('index')
def index():
	return{'nick':'Anonymous', 'messages': messages}

@get('/<nick>')
@view('index')
def index(nick):
	return {'nick': nick, 'messages': messages} 

@post('/send')
def sendMessage():
    m = request.forms.get('message')
    n = request.forms.get('nick')
    messages.append([n, m])
    redirect('/'+n)

run(host='localhost', port=8080)
