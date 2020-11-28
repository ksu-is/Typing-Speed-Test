from pynput import keyboard
import winsound

def on_press(key):
	try: k = key.char # single-char keys
	except: k = key.name # other keys
	if key == keyboard.Key.esc: return False # stop listener
	'''if k in ['1', '2', 'left', 'right']: # keys interested
	# self.keys.append(k) # store it in global-like variable
	print('Key pressed: "' + k +'"')
	return False # remove this if want more keys
	'''
	if k in ['space']: #Space key is pressed
		winsound.PlaySound("space.wav", winsound.SND_ASYNC)
	elif k == 'enter': #New line Enter key is pressed
		winsound.PlaySound("enter_return.wav", winsound.SND_ASYNC)
	elif k == 'backspace': #Back space key is pressed
		winsound.PlaySound("space.wav", winsound.SND_ASYNC)
	elif k in ['shift','shift_r']: #shift key is pressed
		winsound.PlaySound("space.wav", winsound.SND_ASYNC)
	elif k == 'caps_lock': #caps_locka key is pressed
		winsound.PlaySound("space.wav", winsound.SND_ASYNC)
	elif k in ['%','^','&','5','6','7','t','T','y','Y','u','U','i','I','g','G','h','H','j','J','v','V','b','B','n','N']: # any other key
		#keysound.play()
		#winsound.PlaySound('key.wav', winsound.SND_FILENAME)
		winsound.PlaySound("key.wav", winsound.SND_ASYNC)
	elif k in ['`','~','!','@','#','$','1','2','3','4','q','w','e','r','a','s','d','f','z','x','c','Q','W','E','R','A','S','D','F','Z','X','C']:
		winsound.PlaySound("keyleft.wav", winsound.SND_ASYNC) #keys that generally on the left hand side 
	else:
		winsound.PlaySound("keyright.wav", winsound.SND_ASYNC) #keys that generally on the rights
	print ('Key pressed: \''+ k + '\'')

lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is2 123434fasd polling self.keys