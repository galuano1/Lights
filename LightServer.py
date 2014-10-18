from bottle import route, run, static_file

light = True

@route('/')
def home():
    return static_file('index.html', root='/home/pi/apps/Lights')

@route('/js/<filename>')
def home(filename):
    return static_file(filename, root='/home/pi/apps/Lights/js')
    
@route('/css/<filename>')
def home(filename):
    return static_file(filename, root='/home/pi/apps/Lights/css')
    
@route('/images/<filename>')
def home(filename):
    return static_file(filename, root='/home/pi/apps/Lights/images')
    
@route('/do')
def lightSwitch():
	global light
	if (light):
		execfile('off.py')
		light = False
	else:
		execfile('on.py')
		light = True

	return {'status': light}
	
@route('/status')
def status():
	return {'status': light}

@route('/reset')
def reset():
	execfile('off.py')
	light = False
	return {'status': light}
	
reset()

run(host='0.0.0.0', port=80, debug=True)
