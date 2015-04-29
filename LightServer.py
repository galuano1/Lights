from bottle import route, run, static_file

light = True

@route('/')
def home():
    return static_file('index.html', root='/home/pi/apps/Lights')

@route('/js/<filename>')
def js(filename):
    return static_file(filename, root='/home/pi/apps/Lights/js')
    
@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='/home/pi/apps/Lights/css')
    
@route('/images/<filename>')
def img(filename):
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
lightSwitch()

run(host='0.0.0.0', port=80, debug=True)
