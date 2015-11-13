import socket
from time import sleep
from simpleami.scv_handler import SvcHandler


class AMISvcHandler(SvcHandler):
    """AMISvcHandler provides a connection to the Asterisk AMI Manager interface. The class also provides
    methods for passing commands to the AMI as well as simplifying common tasks.
    """
    def __init__(self, host, port):
        super().__init__(self, host, port)

    def connect(self, username, password):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(HOST, PORT)
            return self.do_command(self.build_login_command(username, password))
        except Exception as exc:
            print(exc)
            raise

    def do_command(self, sock, command):
        """Sends a multi-line command over the AMI connection."""
        try:
            for l in command.split('\n'):
                print("> ", l)
                sock.send(str(l+'\r\n').encode())
            return self.wait_for_response(sock)
        except Exception as exc:
            print(exc)
            raise

    def make_call(self, phone_to_dial, username, password, local_user):
        try:
            print("click_to_call")

            data = s.recv(1024)

            do_command(s, pattern)
            self.wait_for_response(s)
            sleep(1)

            pattern = originate_cmd % dict(local_user=local_user, phone_to_dial=phone_to_dial)
            do_command(s, pattern)

            while True:
                data = s.recv(1024)
                for l in data.decode().split('\r\n'):
                    print("< {0}".format(l))
                sleep(1)

            s.close()
        except Exception as exc:
            print(exc)
            raise

    def wait_for_response(self, sock):
        data = sock.recv(1024)
        for l in data.decode().split('\r\n'):
            print("< {0}".format(l))
        return data

    def build_login_command(self, username, password):
        try:
            login_cmd = """Action: login
Username: %(username)s
Secret: %(password)s
Events: off
"""
            return login_cmd % dict(username=username, password=password)
        except Exception as exc:
            print(exc)
            raise
