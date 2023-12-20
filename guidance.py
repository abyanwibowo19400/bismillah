#!/usr/bin/env python3

#Node_guidance

import numpy as np
import rospy
from simple_pid import PID
from std_msgs.msg import Float32

class Subscriber():
    def __init__(self):
        self.kp = 0
        self.ki = 0
        self.kd = 0
        self.pid = PID(self.kp, self.ki, self.kd)
        self.pwm_roll = 0
        self.pwm_pitch = 0
        self.pwm_yaw = 0

        self.pub_pwm_roll = rospy.Publisher('pwm_roll', Float32, queue_size=10)
        self.pub_pwm_pitch = rospy.Publisher('pwm_pitch', Float32, queue_size=10)
        self.pub_pwm_yaw = rospy.Publisher('pwm_yaw', Float32, queue_size=10)

        rospy.Subscriber('error_roll', Float32, self.callback_error_roll)
        rospy.Subscriber('error_pitch', Float32, self.callback_error_pitch)
        rospy.Subscriber('error_yaw', Float32, self.callback_error_yaw)
        rospy.Subscriber('boot_time', Float32, self.callback_boot_time)

    def calculate_pid(self, error):
        return self.pid(error)

    def callback_error_roll(self, data):
        self.pwm_roll = self.calculate_pid(data.data)

    def callback_error_pitch(self, data):
        self.pwm_pitch = self.calculate_pid(data.data)

    def callback_error_yaw(self, data):
        self.pwm_yaw = self.calculate_pid(data.data)

    def callback_boot_time(self):
        self.pub_pwm_roll.publish(self.pwm_roll)
        self.pub_pwm_pitch.publish(self.pwm_pitch)
        self.pub_pwm_yaw.publish(self.pwm_yaw)

    def spin(self):
        rospy.spin()

def main():
    rospy.init_node('node_guidance', anonymous=True)

    subscriber = Subscriber()

    subscriber.spin()

if __name__ == '__main__':
    main()