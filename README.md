
# Hacktiv8 Chatbot — Offline (Ollama)

Chatbot **offline/lokal** menggunakan **Ollama** sebagai backend model LLM. UI memakai **Gradio**.

---
## Prasyarat
- **Python 3.10+**
- **Ollama** terpasang di mesin lokal Anda
  - Download & instal dari https://ollama.com (sekali saja). Setelah itu bisa **offline**.
  - Jalankan daemon: `ollama serve` (biasanya otomatis saat menjalankan perintah `ollama`).

---
## Siapkan Model Lokal (sekali unduh, lalu bisa offline)
Pilih salah satu model ringan (contoh):
- `llama3.2:3b`
- `mistral:7b-instruct`
- `qwen2.5:3b`

Unduh model pilihan (butuh internet **sekali** saat pertama kali):
```bash
ollama pull llama3.2:3b
```
Cek daftar model lokal:
```bash
ollama list
```

---
## Menjalankan Aplikasi
1) Buat virtualenv & install deps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2) Salin `.env.example` → `.env`, sesuaikan `OLLAMA_MODEL` jika perlu.
3) Pastikan Ollama aktif (`ollama serve`) dan model sudah terunduh.
4) Jalankan aplikasi:
   ```bash
   python app.py
   ```
   Buka **http://127.0.0.1:7860**, lalu **screenshot UI** untuk upload ke form.

---
## Struktur Proyek
```text
hacktiv8-chatbot-offline/
├─ app.py
├─ requirements.txt
├─ .env.example
└─ README.md
```

---
## Jawaban Formulir (boleh copy-paste)
- **Model AI apa yang Anda gunakan untuk membangun chatbot Anda?**  
  Model lokal via **Ollama**, contoh: **Llama 3.2 3B** (`llama3.2:3b`).

- **Bagaimana peran AI dalam chatbot yang Anda buat?**  
  Model AI yang berjalan secara lokal memproses input bahasa alami pengguna, mempertimbangkan riwayat percakapan (konteks), lalu menghasilkan respons. Arah gaya jawaban diatur lewat *system prompt* agar sopan, singkat, dan jelas.

- **URL repositori GitHub**  
  Setelah push, masukkan URL repo Anda (mis.: `https://github.com/<username>/hacktiv8-chatbot-offline`).

- **Upload UI (User Interface)**  
  Jalankan `python app.py`, buka `http://127.0.0.1:7860`, ambil **screenshot** halaman chat.

- **Apakah Anda setuju untuk mengizinkan tim Hacktiv8 menggunakan proyek akhir Anda untuk tujuan publikasi?**  
  Pilih **Ya** atau **Tidak** sesuai preferensi.

---
## Kustomisasi (opsional)
- **Ganti model**: ubah `OLLAMA_MODEL` di `.env`.
- **Gaya jawaban**: sunting `SYSTEM_PROMPT` di `app.py`.
- **Parameter inferensi**: ubah `options` (mis. `temperature`, `num_ctx`, dll.) di payload `/api/chat`.
