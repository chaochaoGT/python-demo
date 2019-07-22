from bottle import route, run

@route('/:name')
def index(name='World'):
    return '&lt;div&gt;Hello %s!&lt;/div&gt;' % name

run(host='localhost', port=8080)