# 🛡️ AI Crypto Scam Detector



Aplikasi web berbasis AI untuk mendeteksi penipuan cryptocurrency menggunakan Machine Learning dan Natural Language Processing.

## 📋 Deskripsi

AI Crypto Scam Detector adalah tool yang dirancang untuk membantu pengguna cryptocurrency menghindari penipuan dengan menganalisis teks, pesan, dan URL menggunakan kombinasi rule-based detection dan machine learning model.

### ✨ Fitur Utama

- 🔍 **Analisis Teks Real-time** - Deteksi kata kunci mencurigakan dalam pesan
- 🌐 **Verifikasi Domain** - Cek URL terhadap whitelist exchange resmi
- 🤖 **AI Prediction** - Machine Learning model untuk akurasi tinggi
- 📊 **Confidence Score** - Skor kepercayaan untuk setiap prediksi
- 💡 **Tips Keamanan** - Panduan menghindari scam crypto


## 🛠️ Teknologi

- **Frontend**: Streamlit
- **ML Model**: Scikit-learn (Logistic Regression/Random Forest)
- **NLP**: TF-IDF Vectorization
- **Backend**: Python 3.9+

## 📦 Instalasi

### Prerequisites

- Python 3.9 atau lebih tinggi
- pip atau conda

### Langkah Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/username/crypto-scam-detector.git
   cd crypto-scam-detector
   ```

2. **Buat virtual environment (pilih salah satu)**

   Menggunakan venv:
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

   Atau menggunakan conda:
   ```bash
   conda create -n crypto_scam python=3.9 -y
   conda activate crypto_scam
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**
   ```bash
   streamlit run app2.py
   ```

5. **Buka browser**
   
   Aplikasi akan otomatis terbuka di `http://localhost:8501`

## 📁 Struktur Project

```
crypto-scam-detector/
│
├── app2.py                      # Main application file
├── crypto_scam_model.pkl        # Trained ML model
├── tfidf_vectorizer.pkl         # TF-IDF vectorizer
├── requirements.txt             # Python dependencies
├── README.md                    # Documentation
├── .gitignore                   # Git ignore file
│
├── data/                        # (Optional) Training data
│   └── scam_dataset.csv
│
├── notebooks/                   # (Optional) Jupyter notebooks
│   └── model_training.ipynb
│
└── screenshots/                 # App screenshots
    └── demo.png
```

## 🎯 Cara Penggunaan

1. **Input Teks atau URL**
   - Masukkan pesan, teks, atau URL yang ingin dianalisis
   - Contoh: `"Send 0.1 BTC to double your money"`

2. **Klik Tombol Deteksi**
   - Sistem akan menganalisis input menggunakan AI

3. **Lihat Hasil**
   - ✅ **AMAN** - Tidak ada indikasi penipuan
   - ⚠️ **MENCURIGAKAN** - Berhati-hati, ada red flags
   - 🚨 **SCAM** - Kemungkinan besar penipuan

4. **Baca Rekomendasi**
   - Ikuti saran keamanan yang diberikan

## 🧠 Cara Kerja

### 1. Rule-Based Detection
Sistem memeriksa kata kunci mencurigakan:
- ❌ "double profit", "send crypto", "free BTC"
- ✅ "official", "bappebti", "terdaftar"

### 2. Domain Verification
Membandingkan URL dengan whitelist:
- Binance.com, Indodax.com, Tokocrypto.com, dll.

### 3. Machine Learning Model
- **Model**: Logistic Regression / Random Forest
- **Features**: TF-IDF vectorization
- **Training**: Dataset 10,000+ scam vs legitimate messages
- **Accuracy**: ~95% (tergantung model yang digunakan)

## 📊 Dataset

Model dilatih menggunakan dataset yang berisi:
- Pesan scam dari berbagai platform (Twitter, Telegram, Email)
- Legitimate messages dari exchange resmi
- URL phishing vs URL asli

## ⚙️ Konfigurasi

Edit `app2.py` untuk menyesuaikan:

```python
# Threshold deteksi
THRESHOLD_HIGH = 0.75  # Scam jika >= 75%
THRESHOLD_MED = 0.40   # Mencurigakan jika >= 40%

# Tambah domain whitelist
WHITELIST_DOMAINS = {
    "binance.com", 
    "indodax.com",
    # Tambahkan domain lain
}

# Tambah kata kunci
SCAM_KEYWORDS = [
    "double profit",
    "send crypto",
    # Tambahkan kata lain
]
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Berikut cara berkontribusi:

1. Fork repository
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 To-Do List

- [ ] Tambah support multi-language (Indonesia, English)
- [ ] Integrasi dengan API real-time scam database
- [ ] Mobile app version
- [ ] Browser extension
- [ ] Report scam feature
- [ ] Community voting system

## 🐛 Known Issues

- Model perlu update berkala dengan data scam terbaru
- Beberapa false positive pada pesan marketing legitimate

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author

** Arif**
- GitHub: [@username](https://github.com/username)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Dataset dari berbagai sumber open-source
- Streamlit untuk framework
- Community feedback dan testing

## 📞 Support

Jika ada pertanyaan atau masalah:
- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/username/crypto-scam-detector/issues)
- 💬 Discussion: [GitHub Discussions](https://github.com/username/crypto-scam-detector/discussions)

## ⚠️ Disclaimer

Tool ini dibuat untuk tujuan edukasi dan bantuan deteksi awal. Selalu lakukan verifikasi tambahan dan gunakan akal sehat sebelum melakukan transaksi cryptocurrency.

---

**Stay Safe, Stay Smart! 🛡️**

Made with ❤️ by Bos Arif | Powered by Streamlit & Machine Learning
