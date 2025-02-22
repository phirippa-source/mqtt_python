import json

payload = '{"Temp":24.5, "Humi":66.0}'
payload = json.loads(payload)

print( type(payload) )		# <lass 'dict'>
print( payload['Temp'])		# 24.5
print( payload['Humi'])		# 66.0
