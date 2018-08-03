# simpleami
Simple Asterisk AMI connection class written in Python 3.

The purpose is to provide a simple way to connect to an AMI interface and send commands through it.

The class AMISvcHandler is where the action is. Use AMISvcHandler.connect(username, password) method to connect to the Asterisk AMI.

Use the AMISvcHandler.send_action(action) to send an AMI action to Asterisk.

The file ami_action_templates.py contains two action templates for your convenience for the "Login" and "Originate" actions respectively. More templates will be added as the need arise. Feel free to branch and add your own action templates, but please don't forget to send me a pull request ;)

There is a simple test app called ami_test.py that illustrates how to connect to the AMI and use a template.
