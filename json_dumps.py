import json

payload = {'Temp':24.5, 'Humi':66.0}
# payload = {"Temp":24.5, "Humi":66.0}

print( type(payload) )        # <class 'dict'>
print( payload['Temp'] )      # 24.5
print( payload['Humi'] )     # 66.0

print()

payload = json.dumps(payload)
print( type(payload) )        # <class 'str'>
print( payload )              # {"Temp": 24.5, "Humi": 66.0}
