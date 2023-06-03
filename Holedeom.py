#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 모터 제어 함수
def angle_to_percent (angle) :
    if angle > 360 or angle < 0 : # 180도 초과, 0도 미만 False
        return False

    start = 4 # 모터 0도
    end = 12.5 # 모터 180도
    ratio = (end - start)/180

    angle_as_percent = angle * ratio

    return start + angle_as_percent


GPIO.setmode(GPIO.BOARD) # 모터 핀 모드 설정 (라즈베리파이 보드 번호)
GPIO.setwarnings(False) # setwarnings False 오류 방지

Servo_pin = 12 # 모터 핀 번호 설정
GPIO.setup(Servo_pin, GPIO.OUT) # 모터 출력 설정
pwm = GPIO.PWM(Servo_pin, 50) # PWM 50Hz로 제어 

start_msg = 0 # 시작 or 인원수
on = True # 회전 대기 on/off
on_msg = True 

# 게임 시작
if(start_msg == 0):
    if(on):
        pwm.start(angle_to_percent(0))
        time.sleep(1)
        # on = False

# 2명일 때 회전
elif(start_msg == 2):
    if(on):
        pwm.start(angle_to_percent(180))
        time.sleep(1)
        # on = False
    if(on):
        pwm.start(angle_to_percent(360))
        time.sleep(1)
        # on = False

# 3명일 때 회전
elif(start_msg == 3):
    if(on):
        pwm.start(angle_to_percent(120))
        time.sleep(1)
        # on = False
    if(on):
        pwm.start(angle_to_percent(240))
        time.sleep(1)
        # on = False
    if(on):
        pwm.start(angle_to_percent(360))
        time.sleep(1)
        # on = False

# 4명일 때 회전
elif(start_msg == 4):
    if(on):
        pwm.start(angle_to_percent(90))
        time.sleep(1)
        # on = False
    if(on):
        pwm.start(angle_to_percent(180))
        time.sleep(1)
        # on = False
    if(on):
        pwm.start(angle_to_percent(270))
        time.sleep(1)
        # on = False
    if(on):
        pwm.start(angle_to_percent(360))
        time.sleep(1)
        # on = False

pwm.stop() # 정지
GPIO.cleanup() # GPIO 설정 초기화
