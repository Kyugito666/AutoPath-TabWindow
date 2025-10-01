# PowerShell Auto-Tab Manager (Versi Stabil)

Sebuah skrip Python sederhana namun kuat untuk mengelola dan membuka banyak direktori proyek di PowerShell secara otomatis, rapi, dan efisien.

Dikembangkan oleh **Kyugito666**.

## ✨ Fitur Utama
- **Menu Berbasis Teks**: Interaksi yang cepat dan jelas menggunakan input angka.
- **Pemeriksa Path Otomatis**: Secara cerdas memeriksa semua path di `paths.txt` dan otomatis menghapus direktori yang tidak valid atau tidak ditemukan.
- **Manajemen Cerdas**: Memisahkan direktori "Token" dan "PrivateKey" untuk dibuka di jendela PowerShell yang berbeda.
- **Startup Cepat**: Tanpa *library* UI yang berat, program ini berjalan seketika.
- **Instalasi Mudah**: Semua dependensi dapat diinstal dengan satu skrip sederhana.

---

## 🚀 Instalasi

Pastikan Anda memiliki Python yang terinstal di sistem Anda.

### Cara 1: Menggunakan Skrip (Direkomendasikan untuk Windows)
Cukup klik dua kali file `install.bat`. Skrip ini akan otomatis menginstal *package* yang dibutuhkan.

### Cara 2: Manual via `pip`
Buka terminal atau PowerShell di folder proyek dan jalankan perintah berikut:
```bash
pip install -r requirements.txt
```

---

## 💻 Cara Menjalankan Program

Setelah instalasi selesai, jalankan aplikasi dengan perintah:
```bash
python main.py
```
- Anda akan melihat menu pilihan.
- Masukkan **angka** pilihan Anda (1-4), lalu tekan **Enter**.
- Ikuti instruksi yang muncul di layar.

---

## 📁 Struktur Proyek
```
📁 AutoPath/
├── 📜 main.py         # Skrip utama yang berisi semua logika
├── 📜 paths.txt       # Daftar path direktori Anda
├── 📜 requirements.txt# Daftar package untuk instalasi
└── 🦇 install.bat     # Skrip instalasi untuk Windows
```