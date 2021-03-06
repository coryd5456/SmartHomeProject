#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# dbws_trafficlight.py
# Voice Controlled Traffic Light
# Modified by DroneBot Workshop
# 2018-02-20
#

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""
import os

from subprocess import call

import logging
import subprocess
import sys
import time
import aiy.cloudspeech


import webbrowser

import aiy.assistant.auth_helpers
import aiy.audio
import aiy.voicehat
from google.assistant.library import Assistant
from google.assistant.library.event import EventType

import RPi.GPIO as GPIO
from selenium import webdriver
import action
 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)



logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

aiy.audio.get_recorder().start()
playshell = None
#os.system('mosquitto_sub -v -t "/test/confirm" ')


def play(text):
    aiy.audio.say('Play DJ song!')
    track = text.replace("play","")

    global playshell
    if (playshell == None):
        playshell = subprocess.Popen(["/usr/local/bin/mpsyt",""],stdin=subprocess.PIPE ,stdout=subprocess.PIPE)

    playshell.stdin.write(bytes('/' + track + '\n1\n', 'utf-8'))
    playshell.stdin.flush()

    gpio.setmode(gpio.BCM)
    gpio.setup(23, gpio.IN)

    while gpio.input(23):
        time.sleep(1)
    pkill = subprocess.Popen(["/usr/bin/pkill","vlc"],stdin=subprocess.PIPE)
    

    
def test():
    say = aiy.audio.say('hello')
    action.play(say, 'play')
    
def security():
    aiy.audio.say('Getting a visual on the room')
    os.system('raspistill -o image.jpg \n')

def open_browser():
    aiy.audio.say('Opening Fire fox')
    browser = webdriver.Firefox()

def Hot_as_fuck():
    aiy.audio.say('Understood sir, it is indeed hot as fuck in here')
    os.system('mosquitto_pub -t "/test/light1" -m "7"\n')

def remote_red_light_on():
    aiy.audio.say('Turning the red light on wirelessly') 
    os.system('mosquitto_pub -t "/test/light1" -m "1"\n')

def remote_green_light_on():
    aiy.audio.say('Turning the green light on wirelessly') 
    os.system('mosquitto_pub -t "/test/light1" -m "2"\n')
    
def remote_blue_light_on():
    aiy.audio.say('Turning the blue light on wirelessly') 
    os.system('mosquitto_pub -t "/test/light1" -m "3"\n')

def mood_light_on():
    aiy.audio.say('Turning rainbow effects on') 
    os.system('mosquitto_pub -t "/test/light1" -m "4"\n')

def remote_light_off():
    aiy.audio.say('Turning off the lights') 
    os.system('mosquitto_pub -t "/test/light1" -m "5"\n')
    
def remote_switch_on():
    aiy.audio.say('Turning the Relay on') 
    os.system('mosquitto_pub -t "/test/light1" -m "7"\n')

def remote_switch_off():
    aiy.audio.say('Turning the Relay off') 
    os.system('mosquitto_pub -t "/test/light1" -m "8"\n')
    
def search_youtube():
    recognizer = aiy.cloudspeech.get_recognizer()
    aiy.audio.say('What would you like me to search for')
    youtube_search_term = recognizer.recognize()
    search_for = 'https://www.youtube.com/results?search_query=' + youtube_search_term
    webbrowser.open(search_for)
        
def set_volume():
    recognizer = aiy.cloudspeech.get_recognizer()
    aiy.audio.say('What would you like the volume at?')
    new_volume= recognizer.recognize()
    volume_str = 'amixer sset \'Master\' '+ new_volume +'%\n'
    os.system(volume_str)
    aiy.audio.say('volume set to' + str(new_volume))

def listen():
    aiy.audio.say('Say something')
    run = recognizer.recognize()
    print('searching', run )
    

def servo_on():
    aiy.audio.say('i am getting you a beer')
    p = GPIO.PWM(12,50)
    p.start(7.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1) 

def say_hi_to_rhys():
    aiy.audio.say('Hello Rise, nice to meet you')
    p = GPIO.PWM(12,50)
    p.start(2.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)

def say_hi_to_steffen():
    aiy.audio.say('Hello Steffen, nice to meet you')
    p = GPIO.PWM(12,50)
    p.start(2.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    aiy.audio.say('If you would like a beer, I will get you one next time')
    
def demo_lab_3():
    aiy.audio.say('okay, first we will start by turning on the light emitting diodes')
    GPIO.output(26,True)
    time.sleep(1)
    GPIO.output(6,True)
    time.sleep(1)
    GPIO.output(13,True)
    time.sleep(1)
    aiy.audio.say('Now I will demonstate the operation of a servo motor')
    p = GPIO.PWM(12,50)
    p.start(7.5)
    time.sleep(1)
    aiy.audio.say('First left')
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    aiy.audio.say('Second right')
    p.ChangeDutyCycle(12.5)
    time.sleep(1)
    aiy.audio.say('Now to turn all light emitting diodes off')
    GPIO.output(26,False)
    GPIO.output(6,False)
    GPIO.output(13,False)
    aiy.audio.say('That was a fun demo, lets do something even more fun next time')

def red_led_on():
    aiy.audio.say('Red light on')
    GPIO.output(26,True)

def red_led_off():
    aiy.audio.say('Red light off')
    GPIO.output(26,False)

def yellow_led_on():
    aiy.audio.say('Yellow light on')
    GPIO.output(6,True)

def yellow_led_off():
    aiy.audio.say('Yellow light off')
    GPIO.output(6,False)

def green_led_on():
    aiy.audio.say('Green light on')
    GPIO.output(13,True)

def green_led_off():
    aiy.audio.say('Green light off')
    GPIO.output(13,False)
    
def all_led_on():
    aiy.audio.say('Turning all lights on')
    GPIO.output(26,True)
    GPIO.output(6,True)
    GPIO.output(13,True)

def all_led_off():
    aiy.audio.say('Turning all lights off')
    GPIO.output(26,False)
    GPIO.output(6,False)
    GPIO.output(13,False)
    
def search_google():
    recognizer = aiy.cloudspeech.get_recognizer()
    aiy.audio.say('What would you like me to search for')
    run = recognizer.recognize()
    search_for = 'https://www.google.co.in/#q=' + run
    webbrowser.open(search_for)
    


def play_music():
    webbrowser.open('https://www.youtube.com/watch?v=RB8QPkIaNhQ&t=20s')
    aiy.audio.say('Playing your jam')

def play_relaxing_music():
    webbrowser.open('https://www.youtube.com/watch?v=7tuJM2OuIY0&t=685s')
    aiy.audio.say('Here is what I have found. Hope it helps you relax.')

def quit():
    aiy.audio.say('Exiting program')
    subprocess.call(exit(), shell=True)
    

def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    aiy.audio.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)


def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))


def process_event(assistant, event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')
           

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        first = text.split(" ")[0]
        
        if text == 'power off':
            assistant.stop_conversation()
            power_off_pi()
        elif text == 'reboot':
            assistant.stop_conversation()
            reboot_pi()
        elif text == 'check security':
            assistant.stop_conversation()
            security()
        elif text == 'change the volume':
            assistant.stop_conversation()
            set_volume()
        elif text == 'ip address':
            assistant.stop_conversation()
            say_ip()
        elif text == 'red light on':
            assistant.stop_conversation()
            red_led_on()
        elif text == 'red light off':
            assistant.stop_conversation()
            red_led_off()
        elif text == 'yellow light on':
            assistant.stop_conversation()
            yellow_led_on()
        elif text == 'yellow light off':
            assistant.stop_conversation()
            yellow_led_off()
        elif text == 'green light on':
            assistant.stop_conversation()
            green_led_on()
        elif text == 'green light off':
            assistant.stop_conversation()
            green_led_off()
        elif text == 'all lights on':
            assistant.stop_conversation()
            all_led_on()
        elif text == 'all lights off':
            assistant.stop_conversation()
            all_led_off()
        elif text == 'servo on':
            assistant.stop_conversation()
            servo_on()
        elif text == 'say hi to rise':
            assistant.stop_conversation()
            say_hi_to_rhys()
        elif text == 'say hi to steffen':
            assistant.stop_conversation()
            say_hi_to_steffen()
        elif text == 'demo lab 3':
            assistant.stop_conversation()
            demo_lab_3()
        elif text == 'quit':
            assistant.stop_conversation()
            quit()
        elif text == 'search':
            assistant.stop_conversation()
            search_google()
        elif text == 'play music':
            assistant.stop_conversation()
            play_music()
        elif text == 'play something relaxing':
            assistant.stop_conversation()
            play_relaxing_music()
        elif text == 'search videos':
            assistant.stop_conversation()
            search_youtube()
        elif text == 'remote red light on':
            assistant.stop_conversation()
            remote_red_light_on()
        elif text == 'remote green light on':
            assistant.stop_conversation()
            remote_green_light_on()
        elif text == 'remote blue light on':
            assistant.stop_conversation()
            remote_blue_light_on()
        elif text == 'remote light off':
            assistant.stop_conversation()
            remote_light_off()
        elif text == 'turn mood light on':
            assistant.stop_conversation()
            mood_light_on()
        elif text == 'turn switch on':
            assistant.stop_conversation()
            remote_switch_on()
        elif text == 'turn switch off':
            assistant.stop_conversation()
            remote_switch_off()
        elif text == 'turn on the fan':
            assistant.stop_conversation()
            Hot_as_fuck()
        elif text =='testing time':
            assistant.stop_conversation()
            test()
        elif first == 'play':
            assistant.stop_conversation()
            play(text)

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)



if __name__ == '__main__':
    main()