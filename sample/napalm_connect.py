from napalm import get_network_driver

driver = get_network_driver('ios')

option_args = {'secret': 'cisco'}  # enable password
ios = driver('192.168.217.5', 'wyx', 'wyx', optional_args=option_args)
ios.open()


ios.close()