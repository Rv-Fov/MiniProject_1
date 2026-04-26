# Mini Project 1 — Image Restoration
**Mata Kuliah:** Pengolahan Citra dan Video 

* **Nama :** Muhammad Arifin Umasangadji
* **NRP  :** 5024241083

---

## Penjelasan Pipeline Restorasi
Beberapa tools yang digunakan dan langkah-langkahnya untuk mengatasi gambar noisy ini yakni adalah : 

| Langkah | Teknik | Penjelasan |
| :--- | :--- | :--- |
| **1** | **Median Filter ($3 \times 3$)** | Tahap awal untuk menghilangkan Salt-and-pepper noise karena efektif membuang nilai piksel tanpa merusak tepi objek. |
| **2** | **Gaussian Filter ($3 \times 3$)** | Digunakan untuk mereduksi Gaussian noise yang dengan menghaluskan citra agar bintik-bintik hilang. |
| **3** | **Histogram Equalization** | Memperbaiki citra low contrast, proses dilakukan dengan mengonversi RGB ke **Y (Luminance)**, melakukan ekualisasi intensitas, lalu mengalikan faktor skalanya kembali ke RGB asli agar warna kulit tetap natural. |
| **4** | **Sobel Edge Enhancement** | Teknik untuk memperkuat struktur citra. Dengan menghitung gradien $G_x$ dan $G_y$, tepi objek dideteksi lalu ditambahkan kembali ke citra untuk mengompensasi detail yang hilang akibat proses pembersihan noise. |
| **5** | **Unsharp Masking** | Tahap final sharpening, menggunakan selisih antara citra asli dan citra yang dikaburkan (mask) untuk menonjolkan frekuensi tinggi pada detail wajah, mata, dan topi. |

---

## 2. Perbandingan Visual
Berikut merupakan hasil perbandingan antara citra input yang rusak dengan citra hasil restorasi akhir:

| Citra Input (Noisy) | Citra Output (Restored) |
| :---: | :---: |
| ![Input](test_image_lena_noisy.png) | ![Output](lena_restored.png) |

---

## 3. Analisis Singkat
* **Keberhasilan:** - Kombinasi Median dan Gaussian filter berhasil menciptakan latar belakang dan kulit yang bersih dari noise.
    - Penggunaan teknik **Luminance Scaling** pada Histogram Equalization berhasil meningkatkan kontras secara signifikan namun tetap menjaga keaslian warna (tidak menjadi kemerahan).
    - Detail mata dan rambut kembali terlihat tegas berkat teknik penajaman ganda (Sobel + Unsharp Mask).
* **Potensi Peningkatan:** - Waktu komputasi cukup tinggi karena penggunaan *nested loop* manual pada NumPy. Hal ini bisa dioptimalkan dengan teknik *Vectorization*.
    - Pada area dengan transisi warna sangat tajam, terdapat sedikit *ringing effect* yang bisa diminimalisir dengan pengaturan *threshold* pada unsharp mask.

---

## 4. Cara Menjalankan Program
1. Pastikan library Python berikut sudah terinstal:
   ```bash
   pip install numpy opencv-python matplotlib
