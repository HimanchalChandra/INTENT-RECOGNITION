# INTENT-RECOGNITION
INTENT RECOGNITION USING BREATHING PATTERN TO HELP PARALYZED AND MUTE PEOPLE.
(HEALTHCARE)

In the present era , there are a lot of people who are paralyzed and also face a lot of difficulty in verbal communication. Due to this , they are unable to express themselves and involve in conversations and discussions with the outside world .Afterall , they too have various ideas festering inside their brains which they want to discuss with the world, but unfortunately they can't , due to lack of communication abilities. 
So , through this project , we aim towards helping all those people who aspire to be one of us and who aspire to express their views to the society in the most efficient way possible. In this project ,we will put forward the use of the breathing pattern of the victim , to help him/her , to express his/her intent to someone.

OBJECTIVE

Our main objective behind this project is to develop a portable , efficient , hands free and a stand-alone device , which will be able to assist people facing difficulties in verbal communication due to various diseases. The device would function in three different modes i.e Command Mode , Communication mode and Control Mode.
Command Mode : This mode would encompass all the intents with highest priority such as Emergency , Hunger ,etc.
Communication Mode : This mode will be used solely for communicating with the society , like having a conversation etc.
Control Mode : This mode will be used for controlling the various appliances around the user like Television, Air Conditioner , Fan etc.
So , by developing a model with all the above mentioned features , our sole objective is to make the life of the patient more independent and to boost his/her self confidence.

IMPLEMENTATION

HARDWARE COMPONENTS REQUIRED

1.High Gain Microphone: The high gain microphone will be used for acquiring the breathing data of the user, which will then be relayed to the computing device for further processing.

2.Raspberry Pi Zero: The computing device used for processing the breathing data of the user would be Raspberry pi zero, which would be connected to the microphone with the help of a wire.Here we would be using machine learning to encode the different breathing patterns and map them to different intents. After the intent of the user is identified , our model will create random sentences in such a way that the sentence expresses the intent of the user in the most appropriate manner.

3.Speaker: The speaker will be connected to the computing device via Bluetooth. After the sentence is ready , our model will use text to speech conversion and convey it to the user through a speaker.

WORKING

Whenever the user wants to send a message, the user will give a breath stroke quite stronger than the normal breathing which would then signal the computing device the commencement of the incoming message from the user. The end of the message from the user-end will be signalled to the computing device , when there will be no breathing strokes above the normal breathing strokes (a fixed threshold) for a fixed interval of time, for example, 5 seconds.

Now , when the message from the user in the form of breathing pattern has been received by the computing device, the message will then be processed and then using machine learning algorithms , the model would then be able to map the encoded breathing pattern to the best suitable intent and identify the mode in which the user wants to use the device in.

Now if the mode selected is command or communication mode , the computing device will then frame a sentence which would describe the intent of the user in the most appropriate manner. Then using text to speech conversion, the message will be conveyed to the target audience through a speaker. And if the mode selected is control mode, the computing device would pass the instruction to the iot device which would then be able to control the target appliance. 

In this manner , the patient would be able to be more independent and communicate with the society.


APPLICATIONS

The device can be used by people suffering from diseases like locked-in-syndrome or Pseudocoma ( A condition in which the patient is aware but cannot move or communicate verbally due to complete paralysis of nearly all voluntary muscles in the body except for vertical eye movements and blinking, Paralysis etc.
When merged with IOT , the device can also be used by the user to control appliances around him, call someone when in emergency etc. Thus , making him more independent.

FUTURE PERSPECTIVES

One the model is ready , the entire code and the circuitry will be made available to the open source community. In this way , whoever wants to use it will just have to purchase the hardware and can assemble it themselves. Thus making it cheaper and easy to use . 
Through the speaker the patient will also be able to pass instruction to Alexa and have some source of entertainment too.




