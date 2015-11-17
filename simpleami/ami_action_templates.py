from collections import namedtuple

# Mandatory login options. Action ID is useful for matching responses to action requests.
LoginOptions = namedtuple('LoginOptions', ['username', 'password', 'action_id'])


def login_template(login_options):
    """
    :param:  Mandatory login options
    :return: The action to be send over the AMI connection.
    """
    assert isinstance(login_options, LoginOptions)

    template = """Action: Login\r\n,
                Username: %(username)s\r\n,
                Secret: %(password)s\r\n,
                ActionID: %(action_id)s\r\n,
                Events: off\r\n
                """

    action = template % {
        'username': login_options.username,
        'password': login_options.password,
        'action_id': login_options.action_id
    }
    return action


OriginateOptions = namedtuple('OriginateOptions',
                              ['type',
                               'number',
                               'channel',
                               'caller_id',
                               'context',
                               'priority',
                               'extension',
                               'timeout',
                               'action_id'])


def originate_template(originate_options):
    assert isinstance(originate_options, OriginateOptions)

    template = """Action: Originate\r\n,
                Channel: %(type)s/%(number)s@%(channel)s\r\n,
                CallerID: <%(caller_id)s>\r\n,
                Context: %(context)s\r\n,
                Priority: %(priority)s\r\n,
                Exten: %(extension)s\r\n,
                Async: True\r\n,
                Timeout: %(timeout)s\r\n,
                ActionID: %(action_id)
                """

    action = template % {
        'type': originate_options.type,
        'number': originate_options.number,
        'timeout': originate_options.timeout,
        'callerid': originate_options.callerid,
        'context': originate_options.context,
        'context_local': originate_options.context_local,
        'exten': originate_options.exten,
        'actionid': originate_options.actionid,
    }
    return action
