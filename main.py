# Nama file: main.py (Versi dengan Fitur Tambahan & Opsi Batal)
# GitHub: Kyugito666

import os
import time
import pyautogui
import threading

NAMA_FILE = 'paths.txt'

def tampilkan_menu():
    """Menampilkan menu pilihan utama ke layar."""
    print("\n" + "="*45)
    print("      PowerShell Auto-Tab Menu (Stabil)")
    print("="*45)
    print("1. Cek & Bersihkan Path Tidak Valid")
    print("2. Buka semua path 'Token' di JENDELA BARU")
    print("3. Buka semua path 'PrivateKey' di JENDELA BARU")
    print("4. Keluar")
    print("="*45)

def tampilkan_sub_menu_otomatisasi():
    """Menampilkan menu pilihan untuk mode otomatisasi dengan opsi kembali."""
    print("\n" + "-"*45)
    print("Pilih Mode Otomatisasi:")
    print("1. Siapkan Command (Auto-Detect .py / npm start)")
    print("2. Buka Direktori Saja (Tanpa Command)")
    print("3. Kembali ke Menu Utama")
    print("-" * 45)
    while True:
        pilihan = input("Masukkan pilihan Anda (1/2/3): ")
        if pilihan in ['1', '2', '3']:
            return pilihan
        else:
            print("Pilihan tidak valid! Masukkan 1, 2, atau 3.")


def cek_dan_bersihkan_path(nama_file=NAMA_FILE):
    """Membaca file, memeriksa setiap path, dan menghapus yang tidak valid."""
    if not os.path.exists(nama_file):
        print(f"❌ Error: File '{nama_file}' tidak ditemukan.")
        return

    print(f"\nMemeriksa path di file '{nama_file}'...")
    time.sleep(1)
    
    path_valid, path_dihapus = [], []
    with open(nama_file, 'r', encoding='utf-8') as f:
        semua_path = f.readlines()

    for path_asli in semua_path:
        path_bersih = path_asli.strip()
        if path_bersih:
            if os.path.isdir(path_bersih):
                path_valid.append(path_asli)
            else:
                path_dihapus.append(path_bersih)

    if not path_dihapus:
        print("✅ Semua path valid, tidak ada yang dihapus.")
        return

    with open(nama_file, 'w', encoding='utf-8') as f:
        f.writelines(path_valid)
    
    print(f"🔥 Ditemukan dan dihapus {len(path_dihapus)} path yang tidak valid:")
    for path in path_dihapus:
        print(f"  - {path}")

def baca_path_untuk_otomatisasi(tipe_path, nama_file=NAMA_FILE):
    """Membaca path dari file untuk kategori tertentu (Token/PrivateKey)."""
    paths = []
    if not os.path.exists(nama_file):
        return []
    with open(nama_file, 'r', encoding='utf-8') as f:
        for line in f:
            path = line.strip()
            if path and tipe_path in path:
                paths.append(path)
    paths.sort()
    return paths

def deteksi_perintah(path):
    """Mendeteksi file di dalam path dan mengembalikan command yang sesuai."""
    try:
        files = os.listdir(path)
        # Prioritas file .py yang umum untuk dijalankan
        py_candidates = ['main.py', 'run.py', 'bot.py']
        for py_file in py_candidates:
            if py_file in files:
                return f"python {py_file}"
        
        # Deteksi jika ada file .py lainnya
        for file in files:
            if file.endswith('.py'):
                return f"python {file}" # Ambil file .py pertama yang ditemukan
        
        # Deteksi proyek Node.js
        if 'package.json' in files:
            return "npm start"
            
    except FileNotFoundError:
        return "" # Path tidak ditemukan saat dieksekusi
    return "" # Tidak ada command yang bisa disiapkan

def jalankan_otomatisasi(paths, siapkan_perintah=False):
    """Fungsi yang menjalankan simulasi keyboard pyautogui."""
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1.75)
    pertama = True
    for path in paths:
        if not pertama:
            pyautogui.hotkey('ctrl', 'shift', 't')
            time.sleep(1.2)
            pyautogui.press('enter')
            time.sleep(0.2)
        
        pyautogui.write(f'cd "{path}"', interval=0.01)
        pyautogui.press('enter')
        pyautogui.write('cls', interval=0.01)
        pyautogui.press('enter')

        if siapkan_perintah:
            command = deteksi_perintah(path)
            if command:
                pyautogui.write(command, interval=0.01)
        
        pertama = False

def hitung_mundur():
    """Memberi waktu bagi pengguna untuk fokus ke PowerShell."""
    print("\nPERSIAPAN!")
    print("Anda punya 5 detik untuk KLIK JENDELA POWERSHELL.")
    for i in range(5, 0, -1):
        print(f"...{i}")
        time.sleep(1)
    print("🚀 Memulai otomatisasi...")

# --- Program Utama ---
if __name__ == "__main__":
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

        if pilihan == '1':
            cek_dan_bersihkan_path()
            input("\nTekan Enter untuk kembali ke menu...")
        
        elif pilihan == '2' or pilihan == '3':
            tipe = "Token" if pilihan == '2' else "PrivateKey"
            paths = baca_path_untuk_otomatisasi(tipe)

            if not paths:
                print(f'⚠️ Tidak ada path "{tipe}" yang valid ditemukan.')
                input("\nTekan Enter untuk kembali ke menu...")
                continue

            pilihan_otomatisasi = tampilkan_sub_menu_otomatisasi()
            
            # Jika user memilih kembali, lanjutkan loop utama
            if pilihan_otomatisasi == '3':
                continue

            siapkan_perintah = (pilihan_otomatisasi == '1')

            hitung_mundur()
            print(f'Otomatisasi untuk "{tipe}" berjalan di background...')
            
            thread = threading.Thread(target=jalankan_otomatisasi, args=(paths, siapkan_perintah))
            thread.daemon = True
            thread.start()
            
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == '4':
            print("Terima kasih! Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid! Silakan masukkan 1, 2, 3, atau 4.")
            time.sleep(2)
