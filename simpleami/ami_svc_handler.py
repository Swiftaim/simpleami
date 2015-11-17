import socket
from .ami_action_templates import *


class AMISvcHandler:
    """AMISvcHandler provides a connection to the Asterisk AMI Manager interface.
    The class also provides methods for passing commands to the AMI as well as
    simplifying common tasks.
    For more info on Asterisk AMI:
      http://www.voip-info.org/wiki/view/Asterisk+manager+API
    """

    def __init__(self, host, port):
        """Provide the AMI host and port."""
        self.host_ = host
        self.port_ = port
        self.sock_ = None

    def connect(self, username, password):
        """Connect by providing AMI username and password (secret).
        :rtype : AMI response raw data
        """
        try:
            self.sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock_.connect((self.host_, self.port_))
            options = LoginOptions(username=username, password=password)
            return self.send_action(login_template(options))

        except Exception as exc:
            raise exc

    def send_action(self, action):
        """Sends a multi-line command over the AMI connection.
        Only one outstanding AMI action is allowed.
        :rtype : AMI response raw data
        """
        if self.sock_ is None:
            raise "not connected!"
        try:
            for instruction in action.split('\n'):
                self.sock_.send(str(instruction + '\r\n').encode())
            return self.wait_for_response()

        except Exception as exc:
            raise exc

    def wait_for_response(self):
        """
        Waits for the mandatory AMI response.
        :rtype : AMI response raw data
        """
        if self.sock_ == None:
            raise "not connected!"
        try:
            return self.sock_.recv(1024)

        except Exception as exc:
            raise exc
