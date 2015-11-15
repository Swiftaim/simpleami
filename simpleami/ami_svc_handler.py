import socket

class AMISvcHandler:
    """AMISvcHandler provides a connection to the Asterisk AMI Manager interface. The class also provides
    methods for passing commands to the AMI as well as simplifying common tasks.
    """
    def __init__(self, host, port):
        self.host_ = host
        self.port_ = port
        self.sock_ = None

    def connect(self, username, password):
        try:
            self.sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock_.connect((self.host_, self.port_))
            return self.do_command(self.build_login_command(username, password))
            
        except Exception as exc:
            print(exc)
            raise

    def do_command(self, command):
        """Sends a multi-line command over the AMI connection."""
        if self.sock_ is None:
            raise "not connected!"
        try:
            for l in command.split('\n'):
                print("> ", l)
                self.sock_.send(str(l+'\r\n').encode())
            return self.wait_for_response()

        except Exception as exc:
            print(exc)
            raise

    def wait_for_response(self):
        if self.sock_ == None:
            raise "not connected!"
        try:
            data = self.sock_.recv(1024)
            for l in data.decode().split('\r\n'):
                print("< {0}".format(l))
            return data

        except Exception as exc:
            print(exc)
            raise

    def build_login_command(self, username, password):
        try:
            login_cmd = ('Action: login\r\n'
                         'Username: %(username)s\r\n'
                         'Secret: %(password)s\r\n'
                         'Events: off\r\n')
            return login_cmd % dict(username=username, password=password)
        except Exception as exc:
            print(exc)
            raise
