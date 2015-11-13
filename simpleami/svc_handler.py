class SvcHandler:
    """SvcHandler serves as a base class for connection-oriented communication classes that require a connection
    to a host and a port.
    """
    def __init__(self, host, port):
        self.host_ = host
        self.port_ = port
