import random

class command_mode:
    def __init__(self,data):
        self.data = data
    def get_intent(data):
        intents_ = ["medicine","Thirst","Hunger","health"]
        responses_ = { "medicine":["Time for {} Medicine", "Please give me my medicines", "Can You please help me take my medicines?"],
                     "Thirst" : ["I am thirsty","Please give me a glass of water!","Please help me drinking water."],
                     "Hunger" : ["Time for food"],
                     "health" : ["I am not feeling well.", "Please call the doctor!"] }

        return random.choice(responses_.get(intents_[data]))

class communication_mode:
    def __init__(self,data):
        self.data = data
    def get_intent(data):
        pass

class control_mode:
    def __init__(self,data):
        self.data = data
    def get_intent(data):
        pass

mode = 1;
if(mode == 1):
    myObj = command_mode(data)

elif(mode==2):
    myObj1 =  communication_mode(data)

else:
    myObj2 = control_mode(data)
