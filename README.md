# Tugas 2 Pemrograman Jaringan - Time Server

Repository ini berisi program server dan client sederhana menggunakan TCP socket. Server dapat melayani lebih dari satu client secara bersamaan dengan multithreading, dan berjalan di port 45000.

## File

- `time_server.py` → kode untuk server
- `time_client.py` → kode untuk client

## Cara Jalankan

1. Jalankan server:

   ```bash
   python time_server.py
   ```

2. Jalankan client di terminal lain:

   ```bash
   python time_client.py
   ```

## Perintah Client

- `TIME` → server akan membalas waktu sekarang dalam format `JAM hh:mm:ss`
- `QUIT` → untuk keluar dan menutup koneksi

## Contoh Output

**Client:**
```
Command (TIME / QUIT): TIME
Server: JAM 13:45:10
```

**Server:**
```
2025-06-07 13:45:10,000 - Time server started on port 45000...
2025-06-07 13:45:12,100 - Handling client ('127.0.0.1', 50500)
```


