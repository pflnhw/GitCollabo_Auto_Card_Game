#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 모터 제어 함수
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 : # 180도 초과, 0도 미만 False
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

# 서보모터 0도 회전
pwm.start(angle_to_percent(0))
time.sleep(1)

# 서보모터 90도 회전
pwm.ChangeDutyCycle(angle_to_percent(90))
time.sleep(1)

# 서보모터 180도 회전
pwm.ChangeDutyCycle(angle_to_percent(180))
time.sleep(1)


pwm.stop() # 정지
GPIO.cleanup() # GPIO 설정 초기화