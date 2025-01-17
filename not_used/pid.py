import machine
import time
import read_temp

target=18

Pgain=1
Igain=0.5
Dgain=0

history=[0,0,0,0,0,0,0,0,0,0,0,0,0]
temp_value=read_temp.read_temp(temp_sens)

#take a measurement
def getActuator(target,temp_value,history,Pgain,Igain,Dgain)

    error=(temp_value-target)

    history.append(error)

    history.pop(0)

    Pterm=P_gain*error

    Iterm=I_gain*sum(history)

    Dterm=Dgain*(temp_value-previous_measurement)

    previous_measurement=temp_value

    return Pterm+Iterm+Dterm

actuator_val=getActuatorValue(target,temp_value,history,Pgain,Igain,Dgain)
if actuator_val > 0:
    if actuator_val > 10:
        #run the pump a lot
    
    #turn on cooling pump in relation to the actuator value
else:
    #just wait for it to heat up some time