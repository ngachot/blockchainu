import slacker
import requests
import time

from slackclient import SlackClient

## enter your BTC account balance
account_balance = .4

##your slack api token goes in next line
sc = SlackClient('xoxb-3438841528-LjZhzmm2uO1aFyMxIXwiBnFq')

if not sc.rtm_connect():
		print "error connecting to slack"

while True:

##get account balance from Sochain  
## https://chain.so/api/v2/get_address_balance/{NETWORK}/{ADDRESS}[/{MINIMUM CONFIRMATIONS}]
##PARAMETERS
##network: string
##The acronym of the network you're querying. Required.
##address: string
##The address on the network you're querying. Required.
##minimum confirmations: integer
##The minimum confirmations for the balance. Optional. Default is 0.

	response = requests.get('https://chain.so/api/v2/get_address_balance/BTCTest/mvjVouZvsowjLzQ89J5fBDgtbEuTBZKp4p/0')

	if  response.status_code == 200:
		content = response.json()

	else:
		sc.rtm_send_message('general', 'could not connect to sochain')
		break
	
	btctest_balance = content['data']['confirmed_balance']
	checked_balance = float(btctest_balance)

	if checked_balance != account_balance:
		# Sending a message (<channel>,<message>)
		sc.rtm_send_message('general', 'Bitcoin wallet activity detected')
		sc.rtm_send_message('general', 'You now have %f Bitcoins' % checked_balance)
	else:
		pass
	time.sleep(10)