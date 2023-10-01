import stem.process
from stem.control import Controller

def start_tor():
    tor_process = stem.process.launch_tor_with_config(
        config = {
            'SocksPort': '9000',
            'ExitNodes': '{us}',
            'ControlPort': '9055',
            'DataDirectory': '/tmp/tor'
        },
        init_msg_handler = print,
        take_ownership = True
    )
    return tor_process

def stop_tor(tor_process):
    tor_process.kill()

tor_process = start_tor()

with Controller.from_port(port = 9055) as controller:
    controller.authenticate()
    print('Tor is running version %s' % controller.get_version())
    print('Tor has %s active circuits' % len(controller.get_circuits()))

stop_tor(tor_process)
