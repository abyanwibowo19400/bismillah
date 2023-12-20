import matplotlib.pyplot as plt
import control as ctrl
import numpy as np

# Parameter Kp, Ki, dan Kd
Kp = 300
Ki = 50
Kd = 10

# Numerator dan denominator dari fungsi transfer plant
num_plant = [1]
den_plant = [1, 10, 20]

# Fungsi transfer plant
plant = ctrl.TransferFunction(num_plant, den_plant)

# Kontrol PID
pid_controller = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Sistem kontrol tertutup
system = ctrl.feedback(plant * pid_controller)

# Menentukan waktu simulasi
t = np.arange(0, 5, 0.01)

# Tanggapan langkah sistem kontrol tertutup
t, y = ctrl.step_response(system, t)

print(f"Nilai PID : ",y*100)

# Plotting tanggapan langkah
plt.plot(t, y)
plt.title('Closed-Loop Step Response with PID Controller')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.grid(True)
plt.show()
