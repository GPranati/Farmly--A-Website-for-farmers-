from pymata4 import pymata4
import time
from datetime import datetime
#from time import sleep
#from sinch import SinchClient
import pywhatkit
board = pymata4.Pymata4()


analog_pin = 0
digital_pin = 8
board.set_pin_mode_analog_input(analog_pin)
board.set_pin_mode_digital_input(digital_pin)


'''
sinch_client = SinchClient(
        key_id="YOUR_key_id",
        key_secret="YOUR_key_secret",
        project_id="YOUR_project_id"
    )


def send():

    send_batch_response = sinch_client.sms.batches.send(
        body="Hello from Sinch!",
        to=["YOUR_to_number"],
        from_="YOUR_Sinch_number",
        delivery_report="none"
    )

    print(send_batch_response)
'''

while True:
    value, time_stamp = board.analog_read(analog_pin)
    time.sleep(1)
    if(value<400):
        print("soil is wet")
    elif(value>400 and value<=950):
        print("soil is moderately wet")
    elif(value>950):
        print("soil is dry")
        x = datetime.now()
        current_time = x.strftime("%H:%M:%S")
        print(current_time)
        x = str(current_time)
        pywhatkit.sendwhatmsg('+91995998', 'soil is extremely dry', int(x[:2]), int(x[3:5])+1)
        time.sleep(10)
    else:
        print("connection lost")
        y = datetime.now()
        current_time = y.strftime("%H:%M:%S")
        print(current_time)
        y = str(current_time)
        pywhatkit.sendwhatmsg('+91995998', 'connection lost',int(y[:2]),int(y[3:5])+1)
        time.sleep(10)