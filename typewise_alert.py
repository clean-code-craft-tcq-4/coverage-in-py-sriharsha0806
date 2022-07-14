from collections import defaultdict 

def infer_breach(value, lowerLimit, upperLimit):
    if value < lowerLimit:
        return 'TOO_LOW'
    elif value > upperLimit:
        return 'TOO_HIGH'
    return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
    coolingTypes = ['PASSIVE_COOLING', 'HI_ACTIVE_COOLING', 'MED_ACTIVE_COOLING']
    upperLimit = [35, 45, 40]
    return infer_breach(temperatureInc, 0, upperLimit[coolingTypes.index(coolingType)]) if coolingType in CoolingTypes elseinfer_breach(temperatureInc, 0, 0)

def def_value():
    return "Not Present"

def check_and_alert(alertTarget, batteryChar, temperatureInce):
    classify_temperateure_breach(batteryChar['CoolingType'], temperatureInc)
    d = defaultdict(def_value)
    d["TO_CONTROLLER"] = send_to_controller(breachType)
    d["TO_EMAIL"] = senf_to_email(breachType)
    return d[alertTarget]

def send_to_controller(breachType):
    header = 0xfeed
    print(f'{header}, {breachType}')

def send_to_email(breachType):
    recepient = "a.b@c.com"
    print(f'To: {recepient}')
    print('Hi, the temperature is', ' '.join(breachType.lower().split('_')))
