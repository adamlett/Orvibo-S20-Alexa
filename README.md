# Orvibo S20 Voice Alexa Integration

Enables voice control of Orvibo S20 smart switches which do not natively support Alexa.
Does so by emulating a Belkin WeMo Switch using the [fauxmo library](https://github.com/makermusings/fauxmo) and calling [python2-orvibo-s20](https://github.com/skarna1/python2-orvibo-s20), a python interface to the Orvibo S20 switch to control them.

## Dependencies
* Python 2


In my case the server is a LEDE router, hence:

### LEDE Dependencies
* python-light
* python-email
* python-openssl
* python-codecs

## Usage
* Map the IP and MAC addresses of the switches to names in the list of switches named "FAUXMOS" in the "fauxmo.py" file. 
* (Consider giving the switches static IPs to avoid having to rediscover if the address given by DHCP is changed)
* Run the "fauxmo.py" file

