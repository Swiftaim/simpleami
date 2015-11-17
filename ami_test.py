from simpleami import AMISvcHandler


def main():
	try:
		ami = AMISvcHandler('192.168.40.196', 5038)
		print(ami.connect('clearit', 'clearit').decode())
	except Exception as exc:
		print(exc)

if __name__ == '__main__':
	main()
