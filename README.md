# PowerShell Auto-Tab Manager (Versi Stabil)

Sebuah skrip Python sederhana namun kuat untuk mengelola dan membuka banyak direktori proyek di PowerShell secara otomatis, rapi, dan efisien.

Dikembangkan oleh **Kyugito666**.

## ✨ Fitur Utama
* **Menu Berbasis Teks**: Interaksi yang cepat dan jelas menggunakan input angka.
* **Pemeriksa Path Otomatis**: Secara cerdas memeriksa semua path di `paths.txt` dan otomatis menghapus direktori yang tidak valid.
* **Manajemen Cerdas**: Memisahkan direktori "Token" dan "PrivateKey" untuk dibuka di jendela PowerShell yang berbeda.
* **Startup Cepat**: Tanpa *library* UI yang berat, program ini berjalan seketika.
* **Instalasi Mudah**: Dilengkapi skrip instalasi otomatis untuk Windows dan Linux/macOS.

---

## 🚀 Instalasi & Persiapan

Pastikan Anda memiliki **Git** dan **Python 3** yang terinstal di sistem Anda.

### Langkah 1: Clone & Masuk ke Direktori
Buka terminal Anda dan jalankan perintah-perintah berikut satu per satu:

```bash
git clone https://github.com/Kyugito666/AutoPath-TabWindow.git
cd AutoPath-TabWindow
```

### Langkah 2: Instalasi Dependensi
Setelah berada di dalam folder proyek, instal *package* yang dibutuhkan dengan cara yang sesuai untuk sistem operasi Anda:

* **Windows**: Klik dua kali file `install.bat`.
* **Linux / macOS**: Jalankan skrip `install.sh` dengan perintah berikut di terminal:
    ```bash
    # Jadikan skrip bisa dieksekusi (hanya perlu dilakukan sekali)
    chmod +x install.sh
    ```
    ```bash
    # Jalankan skrip
    ./install.sh
    ```
* **(Alternatif Manual)**: Jika Anda lebih suka cara manual, jalankan 
  ```bash
    pip install -r requirements.txt
  ```
### Langkah 3: Siapkan `paths.txt`
Isi file `paths.txt` dengan daftar lengkap *path* direktori yang ingin Anda kelola. Pastikan setiap *path* mengandung kata kunci `Token` atau `PrivateKey`.

---

## 💻 Cara Menjalankan Program

Setelah instalasi selesai, jalankan aplikasi dari dalam folder proyek dengan perintah:
```bash
# Untuk Windows
python main.py
```
```bash
# Untuk Linux / macOS
python3 main.py
```
* Anda akan melihat menu pilihan.
* Masukkan **angka** pilihan Anda (1-4), lalu tekan **Enter**.

---

## 📁 Struktur Proyek
```
📁 AutoPath-TabWindow/
├── 📜 main.py
├── 📜 paths.txt
├── 📜 requirements.txt
├── 🦇 install.bat
└── 🐧 install.sh
```
