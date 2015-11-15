from simpleami.ami_svc_handler import AMISvcHandler


def main():
    host = "192.168.40.196"
    port = 5038

    ami = AMISvcHandler(host=host, port=port)
    print(ami.connect(username='clearit', password='clearit').decode())

if __name__ == '__main__':
    main()
