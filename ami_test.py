from simpleami import *
from collections import namedtuple


def originate_action():
	options = OriginateOptions(type='Local',
							   number='8888',
							   channel='trunk90-in',
							   timeout='10',
							   caller_id='simpleami',
							   context='auto_test_client',
							   extension='1234',
							   action_id='simpleami-1',
							   priority='1')
	return originate_template(options)


def main():
	try:
		ami = AMISvcHandler('192.168.40.196', 5038)
		print(ami.connect('clearit', 'clearit').decode())
		print(ami.send_action(originate_action()).decode())

	except Exception as exc:
		print(exc)

if __name__ == '__main__':
	main()
