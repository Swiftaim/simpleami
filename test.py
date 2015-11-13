from simpleami import scv_handler


def main():
    HOST = "192.168.40.196"
    PORT = 5038

    login_cmd = """Action: login
Username: %(username)s
Secret: %(password)s
Events: off
"""

    originate_cmd = """Action: Originate
Channel: %(local_user)s
Exten: %(phone_to_dial)s
Priority: 1
Timeout: 10000
Context: default
SetVar: CI_TRUNK_COUNTRY=se
SetVar: language=se_male
SetVar: CI_SYSID=devtest01
"""



if __name__ == '__main__':
    main()