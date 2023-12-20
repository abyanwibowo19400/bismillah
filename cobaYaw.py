def hitung_putaran_tercepat(posisi_awal, posisi_tujuan, kecepatan_putaran):
    putaran_searah_jarum_jam = (posisi_tujuan - posisi_awal) % 360
    putaran_berlawanan_jarum_jam = (posisi_awal - posisi_tujuan) % 360

    if putaran_searah_jarum_jam < putaran_berlawanan_jarum_jam:
        return putaran_searah_jarum_jam / kecepatan_putaran, "searah jarum jam"
    else:
        return putaran_berlawanan_jarum_jam / kecepatan_putaran, "berlawanan jarum jam"

# Contoh penggunaan
posisi_awal = 0
posisi_tujuan = 300
kecepatan_putaran = 50

waktu, arah = hitung_putaran_tercepat(posisi_awal, posisi_tujuan, kecepatan_putaran)

print(f"Objek membutuhkan {waktu} detik untuk berputar ke sudut {posisi_tujuan} derajat {arah}.")
