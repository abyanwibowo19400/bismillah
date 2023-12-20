#!/usr/bin/env python3
#Node Accumulator

import rospy
from std_msgs.msg import Float32

class Subscriber(object):
    def __init__(self):
        self.target_roll = 0
        self.target_pitch = 0
        self.target_yaw = 0

        self.error_roll = 0
        self.error_pitch = 0
        self.error_yaw = 0

        self.pub_error_roll = rospy.Publisher('error_roll', Float32, queue_size=10)
        self.pub_error_pitch = rospy.Publisher('error_pitch', Float32, queue_size=10)
        self.pub_error_yaw = rospy.Publisher('error_yaw', Float32, queue_size=10)

        rospy.Subscriber('roll', Float32, self.callback_roll)
        rospy.Subscriber('pitch', Float32, self.callback_pitch)
        rospy.Subscriber('yaw', Float32, self.callback_yaw)
        rospy.Subscriber('boot_time', Float32, self.callback_boot_time)

    def callback_roll(self, data):
        roll = data.data
        self.error_roll = roll - self.target_roll

    def callback_pitch(self, data):
        pitch = data.data
        self.error_pitch = pitch - self.target_pitch

    def callback_yaw(self, data):
        yaw = data.data
        self.error_yaw = yaw - self.target_yaw

    def callback_boot_time(self):
        self.pub_error_roll.publish(self.error_roll)
        self.pub_error_pitch.publish(self.error_pitch)
        self.pub_error_yaw.publish(self.error_yaw)

    def spin(self):
        rospy.spin()

def main():
    rospy.init_node('node_accumulator', anonymous=True)

    subscriber = Subscriber()

    subscriber.spin()

if __name__ == '__main__':
    main()