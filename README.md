# Tugas 3 Sistem Kendali

Veronika Juninda
21/474552/PA/20495

# Penjelsan Kode

- !pip install tbcontrol --digunakan untuk mengintal package bernama tbcontrol, dimana package tersebut berguna untuk mengolah data terkait dinamika dan kontrol/kendali
- import sympy
- import tbcontrol
- from tbcontrol.symbolic import routh --serangkaian perintah import yang digunakan untuk memanggil library yang dibutuhkan. Sympy untuk library matematika simbolik, tbcontrol untuk kendali dan routh untuk metode yang digunakan dalam pengolahan sistem
- s = sympy.Symbol('s')
- K = sympy.Symbol('K') --deklarasi simbol dalam persamaan matematika agar dapat dideteksi oleh sistem
- 


