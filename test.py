from simpleami.ami_svc_handler import AMISvcHandler

def main():
	HOST = "192.168.40.196"
	PORT = 5038

	ami = AMISvcHandler(HOST, PORT)
	print(ami.connect(username='clearit', password='clearit').decode())

if __name__ == '__main__':
    main()