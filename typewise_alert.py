def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
    l = [35, 40, 45]
    coolingTypes = ['PASSIVE_COOLING', 'MED_ACTIVE_COOLING', 'HI_ACTIVE_COOLING']
    lowerlimit = 0
    index = coolingTypes.index(coolingType)
    upperlimit = l[index]
    return infer_breach(temperatureInC, lowerlimit, upperlimit)
    

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    msg = send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    msg = send_to_email(breachType)
  return breachType, msg


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
    return f"To: {recepient}, Hi, the temperature is too low"
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
    return f"To: {recepient}, Hi, the temperature is too high"
