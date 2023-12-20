#Untuk menentukan PID yang akan dipakai

from simple_pid import PID
import time

# Inisialisasi PID Controller
pid = PID(Kp=0.50, Ki=0.0, Kd=0)

# Setpoint yang diinginkan
setpoint = 90.0

# Nilai awal variabel proses
process_variable = 0

# Waktu sampel (dalam detik)
dt = 1.0

# Loop kontrol
for _ in range(100):
    # Menghitung sinyal kontrol PID
    control_signal = pid(process_variable - setpoint)

    # Simulasikan perubahan variabel proses
    process_variable += control_signal * dt

    # Tampilkan hasil
    print(f"Setpoint: {setpoint:.2f}, Variabel Proses: {process_variable:.2f}, Control Signal: {control_signal:.2f}")

    # Tunggu selama waktu sampel
    time.sleep(1)