from collections import namedtuple

# Mandatory login options. Action ID is useful for matching responses to action requests.
LoginOptions = namedtuple('LoginOptions', ['username', 'password'])


def login_template(login_options):
    """
    :param:  Mandatory login options
    :return: The action to be send over the AMI connection.
    """
    assert isinstance(login_options, LoginOptions)

    template = """Action: Login
Events: off
Username: %(username)s
Secret: %(password)s
"""

    action = template % {
        'username': login_options.username,
        'password': login_options.password,
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

    template = """Action: Originate
Channel: %(type)s/%(number)s@%(channel)s
CallerID: <%(caller_id)s>
Context: %(context)s
Priority: %(priority)s
Exten: %(extension)s
Async: True
Timeout: %(timeout)s
ActionID: %(action_id)s
"""

    action = template % {
        'type': originate_options.type,
        'number': originate_options.number,
        'channel': originate_options.channel,
        'caller_id': originate_options.caller_id,
        'context': originate_options.context,
        'priority': originate_options.priority,
        'extension': originate_options.extension,
        'timeout': originate_options.timeout,
        'action_id': originate_options.action_id
    }
    return action
