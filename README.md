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
- print("Nilai Polynomial")
- p = 7*s**7 + 3*s**6 + 6*s**5 + 4*s**4 + 5*s**3 + 2*s**2 + s + K --deklarasi persamaan polinomial yang disimpan dalam variabel 'p'
- p = sympy.Poly(p, s) --mengubah persamaan P menjadi persamaan polinomial dengan representasi simbolik yang benar 
- p --menampilkan persamaan
- print("Routh Table")
- R = routh(sympy.Poly(p, s)) --membuat Routh Table dari persamaan polinomial yang diberikan, dan disimpan dalam variabel R
- R --menampilkan Routh Table
- print("Nilai K")
- sympy.solve([e > 0 for e in R[:, 0]], K) --menampilkan nilai K yang sesuai agar persamaan stabil

