import streamlit as st
import joblib
import re
import pandas as pd

# ==============================
# KONFIGURASI UTAMA
# ==============================
st.set_page_config(
    page_title="Crypto Scam Detector", 
    page_icon="🛡️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS untuk styling
st.markdown("""
<style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Main container */
    .main-container {
        background: rgba(255, 255, 255, 0.98);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Header styling */
    .header-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        animation: fadeIn 1s ease-in;
    }
    
    .subtitle {
        text-align: center;
        color: #f1f5f9;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 500;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        color: white !important;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border-radius: 12px;
        border: none;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(14, 165, 233, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(14, 165, 233, 0.6);
        background: linear-gradient(135deg, #0284c7 0%, #1d4ed8 100%);
    }
    
    /* Text area styling */
    .stTextArea>div>div>textarea {
        border-radius: 12px;
        border: 2px solid #cbd5e1;
        font-size: 1rem;
        transition: border-color 0.3s ease;
        background-color: #ffffff !important;
        color: #0f172a !important;
    }
    
    .stTextArea>div>div>textarea:focus {
        border-color: #0ea5e9;
        box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.1);
    }
    
    /* Alert boxes dengan kontras lebih baik */
    .stSuccess {
        background-color: #d1fae5 !important;
        color: #065f46 !important;
        border-radius: 12px;
        padding: 1rem;
        font-weight: 600;
        border-left: 4px solid #10b981;
    }
    
    .stError {
        background-color: #fee2e2 !important;
        color: #991b1b !important;
        border-radius: 12px;
        padding: 1rem;
        font-weight: 600;
        border-left: 4px solid #ef4444;
    }
    
    .stWarning {
        background-color: #fef3c7 !important;
        color: #92400e !important;
        border-radius: 12px;
        padding: 1rem;
        font-weight: 600;
        border-left: 4px solid #f59e0b;
    }
    
    .stInfo {
        background-color: #dbeafe !important;
        color: #1e40af !important;
        border-radius: 12px;
        padding: 1rem;
        font-weight: 500;
        border-left: 4px solid #3b82f6;
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 4px solid #0ea5e9;
    }
    
    .feature-title {
        font-weight: 700;
        color: #0369a1;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
    }
    
    .feature-text {
        color: #334155;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    
    /* Stats box */
    .stats-box {
        background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 16px rgba(14, 165, 233, 0.3);
    }
    
    .stats-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
        font-size: 0.9rem;
        opacity: 0.95;
        font-weight: 500;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        color: #cbd5e1;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    .footer strong {
        color: #f1f5f9;
    }
    
    /* Icon styling */
    .icon-large {
        font-size: 4rem;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #f1f5f9 !important;
        border-radius: 8px !important;
        color: #0f172a !important;
        font-weight: 600 !important;
    }
    
    /* Tips list styling */
    .tips-container {
        background: #f8fafc;
        padding: 1.5rem;
        border-radius: 12px;
        color: #1e293b;
        line-height: 1.8;
    }
    
    .tips-container strong {
        color: #0369a1;
    }
    
    /* Label text color fix */
    .stTextArea label, .stMarkdown h3 {
        color: #f8fafc !important;
        font-weight: 600 !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    }
    
    /* Section headers */
    h3 {
        color: #f8fafc !important;
    }
    
    /* Emoji headers */
    .stMarkdown h3::before {
        filter: brightness(1.2);
    }
</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================
st.markdown('<h1 class="header-title">🛡️ AI Crypto Scam Detector</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Lindungi diri Anda dari penipuan cryptocurrency dengan teknologi AI</p>', unsafe_allow_html=True)

# ==============================
# LOAD MODEL DAN VECTORIZER
# ==============================
try:
    model = joblib.load("crypto_scam_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    model_loaded = True
except:
    model_loaded = False
    st.warning("⚠️ Model belum dimuat. Mode demo dengan rule-based detection.")

# ==============================
# PARAMETER DAN DATA TAMBAHAN
# ==============================
WHITELIST_DOMAINS = {
    "binance.com", "indodax.com", "triv.co.id", "pintu.co.id",
    "tokocrypto.com", "luno.com", "bybit.com",
    "coinbase.com", "kraken.com", "gemini.com",
    "huobi.com", "okx.com", "bitfinex.com", "bitstamp.net",
    "rekeningku.com", "bitcoin.org", "ethereum.org", "ripple.com", "xrpl.org"
}

OFFICIAL_EXCHANGES = ["binance", "indodax", "tokocrypto", "pintu", "coinbase", "kraken", "bybit"]

SAFE_KEYWORDS = ["bappebti", "ojk", "terdaftar", "diawasi", "resmi", "official", "verified"]
SCAM_KEYWORDS = [
    "congratulations", "won", "win", "claim", "bonus", "reward",
    "send crypto", "airdrop", "double profit", "free", "get rich",
    "gift", "giveaway", "click here", "login", "verify account", "suspended", "die"
]

THRESHOLD_HIGH = 0.75
THRESHOLD_MED = 0.40

# ==============================
# INFO SECTION
# ==============================
with st.expander("ℹ️ Cara Kerja Detector Ini"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🔍 Analisis Teks</div>
            <p class="feature-text">
                Menganalisis kata kunci dan pola yang sering digunakan dalam penipuan
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🌐 Cek Domain</div>
            <p class="feature-text">
                Memverifikasi URL terhadap database exchange resmi
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🤖 AI Prediction</div>
            <p class="feature-text">
                Machine Learning model untuk deteksi akurat
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================
# INPUT SECTION
# ==============================
st.markdown("### 📝 Masukkan Teks atau URL untuk Dianalisis")
text_input = st.text_area(
    "",
    height=120,
    placeholder="Contoh: https://binance.com atau 'Congratulations! You won 5 BTC. Click here to claim your reward!'",
    help="Paste pesan, teks, atau URL yang ingin Anda periksa",
    key="text_input_main"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    detect_button = st.button("🔎 Deteksi Sekarang", use_container_width=True)

# ==============================
# DETECTION LOGIC
# ==============================
if detect_button:
    if not text_input.strip():
        st.warning("⚠️ Mohon masukkan teks atau URL terlebih dahulu!")
    else:
        with st.spinner("🔄 Menganalisis..."):
            text = text_input.lower()
            
            # Cek domain
            domain_match = re.findall(r"(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", text)
            domain = domain_match[0] if domain_match else ""
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<h3 style="color: #f8fafc;">📊 Hasil Analisis</h3>', unsafe_allow_html=True)
            
            # Cek whitelist domain resmi
            if domain in WHITELIST_DOMAINS:
                st.markdown('<div class="icon-large">✅</div>', unsafe_allow_html=True)
                st.success(f"**AMAN** - Situs resmi terdeteksi: {domain}")
                st.info(f"Domain ini terdaftar dalam whitelist exchange cryptocurrency resmi.")
                
            # Cek nama exchange + kata "official"
            elif any(exchange in text for exchange in OFFICIAL_EXCHANGES) and "official" in text:
                detected_exchange = [ex for ex in OFFICIAL_EXCHANGES if ex in text][0]
                st.markdown('<div class="icon-large">✅</div>', unsafe_allow_html=True)
                st.success(f"**AMAN** - Menyebut exchange resmi: {detected_exchange.upper()}")
                
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.markdown("""
                    <div class="stats-box" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);">
                        <div class="stats-number">95%</div>
                        <div class="stats-label">Safety Score</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                st.info(f"💡 **Tips**: Pastikan URL benar-benar {detected_exchange}.com, bukan yang mirip-mirip (typosquatting)")
                
            # Cek kata legalitas (aman)
            elif any(k in text for k in SAFE_KEYWORDS):
                st.markdown('<div class="icon-large">✅</div>', unsafe_allow_html=True)
                st.success("**AMAN** - Teks mengandung kata kunci legalitas")
                detected_keywords = [k for k in SAFE_KEYWORDS if k in text]
                st.info(f"Kata kunci terdeteksi: {', '.join(detected_keywords)}")
                
            # Cek kata scam umum
            elif any(k in text for k in SCAM_KEYWORDS):
                st.markdown('<div class="icon-large">🚨</div>', unsafe_allow_html=True)
                st.error("**SCAM TERDETEKSI** - Mengandung kata kunci penipuan!")
                detected_scam = [k for k in SCAM_KEYWORDS if k in text]
                st.warning(f"Kata kunci mencurigakan: {', '.join(detected_scam[:5])}")
                
            else:
                # Pembersihan teks
                text_clean = re.sub(r"http\S+|www.\S+", " ", text)
                text_clean = re.sub(r"[^a-z0-9\s]", " ", text_clean)
                text_clean = re.sub(r"\s+", " ", text_clean).strip()
                
                if model_loaded:
                    # Prediksi dari model
                    X = vectorizer.transform([text_clean])
                    proba = model.predict_proba(X)[0][1]
                    
                    # Interpretasi hasil
                    if proba >= THRESHOLD_HIGH:
                        st.markdown('<div class="icon-large">🚨</div>', unsafe_allow_html=True)
                        st.error(f"**SANGAT BERBAHAYA** - Kemungkinan SCAM tinggi!")
                        
                        col1, col2, col3 = st.columns(3)
                        with col2:
                            st.markdown(f"""
                            <div class="stats-box" style="background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);">
                                <div class="stats-number">{proba:.0%}</div>
                                <div class="stats-label">Scam Probability</div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        st.warning("⚠️ **Rekomendasi**: Jangan berikan informasi pribadi atau kirim crypto!")
                        
                    elif proba >= THRESHOLD_MED:
                        st.markdown('<div class="icon-large">⚠️</div>', unsafe_allow_html=True)
                        st.warning(f"**MENCURIGAKAN** - Berhati-hatilah!")
                        
                        col1, col2, col3 = st.columns(3)
                        with col2:
                            st.markdown(f"""
                            <div class="stats-box" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);">
                                <div class="stats-number">{proba:.0%}</div>
                                <div class="stats-label">Risk Level</div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        st.info("💡 Verifikasi lebih lanjut sebelum melakukan tindakan apapun")
                        
                    else:
                        st.markdown('<div class="icon-large">✅</div>', unsafe_allow_html=True)
                        st.success(f"**KEMUNGKINAN AMAN** - Tidak terdeteksi tanda-tanda penipuan jelas")
                        
                        col1, col2, col3 = st.columns(3)
                        with col2:
                            st.markdown(f"""
                            <div class="stats-box" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);">
                                <div class="stats-number">{(1-proba):.0%}</div>
                                <div class="stats-label">Safety Score</div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        if proba > 0.25:
                            st.info("💡 **Catatan**: Score di bawah 80% berarti masih ada sedikit indikasi mencurigakan. Tetap waspada dan verifikasi URL dengan teliti.")
                else:
                    st.info("Model AI tidak tersedia. Hasil berdasarkan rule-based detection.")

# ==============================
# TIPS SECTION
# ==============================
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("💡 Tips Menghindari Scam Crypto"):
    st.markdown("""
    <div class="tips-container">
        🔒 <strong>Verifikasi URL</strong> - Selalu cek URL dengan teliti, perhatikan ejaan domain<br>
        📧 <strong>Jangan Klik Sembarangan</strong> - Hindari link dari email/pesan yang tidak dikenal<br>
        🎁 <strong>Too Good to Be True</strong> - Tidak ada yang gratis, waspada dengan tawaran fantastis<br>
        🔐 <strong>Jaga Private Key</strong> - Jangan pernah membagikan private key atau seed phrase<br>
        ✅ <strong>Gunakan Platform Resmi</strong> - Hanya gunakan exchange yang terdaftar dan terverifikasi<br>
        👥 <strong>Cek Legalitas</strong> - Pastikan platform terdaftar di BAPPEBTI atau regulator lokal
    </div>
    """, unsafe_allow_html=True)

# ==============================
# FOOTER
# ==============================
st.markdown("""
<div class="footer">
    <strong>Dibuat oleh Bos Arif</strong> — AI & Machine Learning 🇮🇩<br>
    <small>Powered by Streamlit | Stay Safe, Stay Smart 🛡️</small>
</div>
""", unsafe_allow_html=True)