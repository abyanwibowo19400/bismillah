#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

class AccumulatorNode:
    def __init__(self):
        self.target_roll = 0
        self.target_pitch = 0
        self.target_yaw = 0

        self.error_roll = 0
        self.error_pitch = 0
        self.error_yaw = 0



        # Publisher untuk data error
        self.pub_error_roll = rospy.Publisher('error_roll', Float32, queue_size=10)
        self.pub_error_pitch = rospy.Publisher('error_pitch', Float32, queue_size=10)
        self.pub_error_yaw = rospy.Publisher('error_yaw', Float32, queue_size=10)

        # Subscriber untuk menerima data roll, pitch, dan yaw
        rospy.Subscriber('roll', Float32, self.callback_roll)
        rospy.Subscriber('pitch', Float32, self.callback_pitch)
        rospy.Subscriber('yaw', Float32, self.callback_yaw)
        rospy.Subscriber('boot_time', Float32, self.callback_boot_time)

    def callback_roll(self, data):
        # Callback untuk mendapatkan nilai roll
        roll = data.data
        self.error_roll = roll - self.target_roll

        # Kirim data error_roll
        self.pub_error_roll.publish(self.error_roll)

    def callback_pitch(self, data):
        # Callback untuk mendapatkan nilai pitch
        pitch = data.data
        self.error_pitch = pitch - self.target_pitch

        # Kirim data error_pitch
        self.pub_error_pitch.publish(self.error_pitch)

    def callback_yaw(self, data):
        # Callback untuk mendapatkan nilai yaw
        yaw = data.data
        self.error_yaw = yaw - self.target_yaw

        # Kirim data error_yaw
        self.pub_error_yaw.publish(self.error_yaw)

    def callback_boot_time(self, data):
        # Callback untuk mendapatkan nilai waktu boot
        boot_time = data.data
        rospy.loginfo(f"Boot Time: {boot_time:.2f}")

    def spin(self):
        # Fungsi spin() digunakan untuk menjalankan node ROS
        rospy.spin()

def main():
    # Inisialisasi node ROS
    rospy.init_node('accumulator_node', anonymous=True)

    accumulator_node = AccumulatorNode()
    accumulator_node.spin()

if __name__ == '__main__':
    main()
