# 🚀 MyInstaFollow: Tool Otomasi Instagram Berbasis Python

Sebuah tool otomasi berbasis Python yang dirancang secara profesional untuk berinteraksi dengan `myinstafollow.com` guna mendapatkan _likes_, _views_, dan _followers_ Instagram. Proyek ini dibangun dengan arsitektur _Object-Oriented_ yang bersih, menjadikannya tangguh, mudah dikembangkan, dan gampang dikonfigurasi.

![MyInstaFollow](https://github.com/user-attachments/assets/c886aed2-2571-45a7-890b-11962c2072e0)

## ✨ Fitur Utama

* **Dukungan Proxy:** Terintegrasi dengan daftar proxy dari file `proxy.txt` untuk merotasi alamat IP pada setiap permintaan, demi keamanan dan keandalan.
* **Dukungan Multi-Layanan:** Mampu menangani layanan _likes_, _views_, dan _followers_ secara bersamaan dalam satu siklus.
* **Otomasi Penuh:** Berjalan dalam _loop_ berkelanjutan untuk mengeksekusi tugas berdasarkan interval waktu yang dapat dikonfigurasi.
* **Arsitektur Profesional:** Dibangun menggunakan prinsip-prinsip _Object-Oriented Programming_ (OOP) untuk kode yang bersih dan mudah dipelihara.
* **Konfigurasi Eksternal:** Semua pengaturan, target, dan parameter layanan dikelola dalam file `JSON` yang sederhana. Tidak perlu mengubah kode sumber.

## 🚀 Panduan Memulai

Ikuti instruksi berikut untuk menyiapkan dan menjalankan proyek di mesin lokal Anda.

#### Prasyarat

* Python 3.7 atau yang lebih baru
* `pip` (manajer paket Python)

#### Instalasi & Pengaturan

1. **Unduh atau Clone Proyek**
    Untuk mendapatkan salinan kode sumber, lakukan _clone_ repositori dengan perintah berikut di terminal Anda:
   
   ```bash
   git clone https://github.com/RozhakLabs/MyInstaFollow.git
   cd MyInstaFollow
   ```

2. **Instal Ketergantungan (Dependencies)**
    Kemudian, jalankan perintah berikut di terminal Anda:
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Konfigurasi Layanan**
    Buka file `config/services.json` dan ubah sesuai kebutuhan Anda:
   
   * Atur `"enabled": true` untuk layanan yang ingin Anda jalankan.
   
   * Isi `post_link`, `reel_link`, atau `username` target Anda.
   
   * Sesuaikan `quantity` dan `interval_hours` (jeda waktu dalam jam) jika perlu.
     
     Contoh:
     
     ```json
     {
       "services": {
           "followers": {
           "enabled": true,
           "username": "rozhak_official",
           ...
           }
       }
     }
     ```

4. **(Opsional) Konfigurasi Proxy**
    Jika Anda ingin menggunakan proxy, buka config/proxy.txt dan tambahkan proxy Anda, satu per baris. Format yang didukung adalah:
   
   * `ip:port`
   * `ip:port:username:password`
   * `http://ip:port`
   * `http://username:password@ip:port`

#### ▶️ Cara Menjalankan

Setelah semua pengaturan selesai, Anda dapat menjalankan _tool_ ini dari direktori utama (`MyInstaFollow/`) menggunakan perintah berikut:

```bash
python -m myinstafollow.main
```

Aplikasi akan mulai berjalan, memuat konfigurasi, dan mulai mengeksekusi layanan yang aktif dalam sebuah _loop_. Semua status proses akan dicetak langsung ke konsol.

Untuk menghentikan tool, tekan `Ctrl + Z`.

## ⚠️ Penafian (Disclaimer)

Tool ini dibuat untuk tujuan edukasi semata. Penggunaan _tool_ otomasi mungkin melanggar ketentuan layanan dari platform yang berinteraksi dengannya. Pengembang tidak bertanggung jawab atas segala konsekuensi dari penggunaan _tool_ ini, seperti penangguhan akun atau penalti lainnya. Gunakan dengan risiko Anda sendiri.

## 📝 License


This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
