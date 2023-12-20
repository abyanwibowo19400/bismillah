#!/usr/bin/env python3

import rospy
from simple_pid import PID
from std_msgs.msg import Float32
import time

class Subscriber:
    def __init__(self):
        self.kp = 0.50
        self.ki = 0.0
        self.kd = 0.0
        self.pid = PID(self.kp, self.ki, self.kd)
        self.setpoint = 90.0
        self.process_variable = 0.0

        # Inisialisasi node ROS
        rospy.init_node('guidance_node', anonymous=True)

        # Publisher untuk hasil kontrol PID
        self.pub_pwm_roll = rospy.Publisher('pwm_roll', Float32, queue_size=10)
        self.pub_pwm_pitch = rospy.Publisher('pwm_pitch', Float32, queue_size=10)
        self.pub_pwm_yaw = rospy.Publisher('pwm_yaw', Float32, queue_size=10)

        # Subscriber untuk menerima data error
        rospy.Subscriber('error_roll', Float32, self.callback_error_roll)
        rospy.Subscriber('error_pitch', Float32, self.callback_error_pitch)
        rospy.Subscriber('error_yaw', Float32, self.callback_error_yaw)
        rospy.Subscriber('boot_time', Float32, self.callback_boot_time)

    def calculate_pid(self, error):
        return self.pid(error)

    def callback_error_roll(self, data):
        # Callback untuk mengupdate nilai error dan menghitung kontrol PID
        error = data.data
        control_signal = self.calculate_pid(error)

        # Tampilkan hasil
        rospy.loginfo(f"Setpoint: {self.setpoint:.2f}, Variabel Proses: {self.process_variable:.2f}, Control Signal: {control_signal:.2f}")

        # Kirim hasil kontrol
        self.pub_pwm_roll.publish(control_signal)

    def callback_error_pitch(self, data):
        # Callback untuk mengupdate nilai error dan menghitung kontrol PID
        error = data.data
        control_signal = self.calculate_pid(error)

        # Tampilkan hasil
        rospy.loginfo(f"Setpoint: {self.setpoint:.2f}, Variabel Proses: {self.process_variable:.2f}, Control Signal: {control_signal:.2f}")

        # Kirim hasil kontrol
        self.pub_pwm_pitch.publish(control_signal)

    def callback_error_yaw(self, data):
        # Callback untuk mengupdate nilai error dan menghitung kontrol PID
        error = data.data
        control_signal = self.calculate_pid(error)

        # Tampilkan hasil
        rospy.loginfo(f"Setpoint: {self.setpoint:.2f}, Variabel Proses: {self.process_variable:.2f}, Control Signal: {control_signal:.2f}")

        # Kirim hasil kontrol
        self.pub_pwm_yaw.publish(control_signal)

    def callback_boot_time(self, data):
        # Callback untuk mendapatkan nilai waktu boot
        boot_time = data.data
        rospy.loginfo(f"Boot Time: {boot_time:.2f}")
    def spin(self):
        rospy.spin()


def main():
    rospy.init_node('node_guidance', anonymous=True)

    Sub = Subscriber()

    Sub.spin()

if __name__ == '__main__':
    main()
