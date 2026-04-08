# 🛒 E-Commerce Analytics Dashboard
### Brazilian Olist E-Commerce Public Dataset — Dicoding Data Analysis Project

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-green?logo=pandas)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)

---

## 📌 Deskripsi Proyek

Proyek ini merupakan **proyek akhir** kelas **Belajar Analisis Data dengan Python** di Dicoding Academy. Analisis dilakukan terhadap **Brazilian E-Commerce Public Dataset by Olist** — dataset e-commerce terbesar di Brasil yang mencakup lebih dari 100.000 transaksi dari September 2016 hingga Agustus 2018.

Proyek ini mencakup seluruh pipeline analisis data mulai dari **data wrangling**, **exploratory data analysis (EDA)**, **analisis lanjutan (RFM & Geospatial)**, hingga **dashboard interaktif** berbasis Streamlit.

---

## 🔍 Pertanyaan Bisnis

| # | Pertanyaan |
|---|-----------|
| 1 | Bagaimana tren jumlah order dan total revenue per bulan selama 2016–2018, dan pada bulan mana terjadi puncak serta penurunan paling signifikan? |
| 2 | Kategori produk mana yang menghasilkan revenue tertinggi dan terendah, dan bagaimana perbandingan rata-rata nilai transaksinya? |
| 3 | Siapa pelanggan dengan nilai tertinggi berdasarkan segmentasi RFM, dan berapa proporsi segmen Champions vs. pelanggan berisiko churn? |
| 4 | Di negara bagian mana konsentrasi pelanggan dan seller paling tinggi, dan apakah terdapat ketimpangan distribusi geografis yang memengaruhi waktu pengiriman? |

---

## 📊 Key Findings

| Metrik | Nilai |
|--------|-------|
| Total Order (delivered) | 96,478 |
| Total Revenue | R$ 15,420,000+ |
| Rata-rata Order/Bulan | ~4,097 order |
| Puncak Order | November 2017 — 7,289 order (Black Friday) |
| Kategori Revenue Tertinggi | health_beauty |
| Pelanggan Champions | 6,497 (7%) |
| Pelanggan At Risk | 22,230 (23.8%) |
| State Pelanggan Terbesar | São Paulo (SP) |
| Rata-rata Delivery Time | ~12–13 hari |

---

## 🧠 Teknik Analisis

### RFM Analysis
Segmentasi pelanggan berdasarkan 3 dimensi perilaku pembelian menggunakan metode quintile scoring (1–5):
- **Recency** — seberapa baru pelanggan bertransaksi
- **Frequency** — seberapa sering bertransaksi
- **Monetary** — total pengeluaran pelanggan

Menghasilkan 6 segmen: **Champions**, Loyal Customers, Recent Customers, Potential Loyalists, At Risk, dan Lost.

### Geospatial Analysis
Analisis distribusi geografis customer dan seller di 27 state Brasil menggunakan **Folium HeatMap** dan bubble map interaktif — mengidentifikasi ketimpangan yang berdampak pada delivery time.

### Delivery Time Analysis
Mengukur rata-rata waktu pengiriman per state dan membuktikan korelasi antara kepadatan seller dengan kecepatan pengiriman.

---

## 📁 Struktur Direktori

```
submission/
├── Dashboard/
│   ├── dashboard.py        ← Streamlit dashboard app
│   └── main_data.csv       ← Data bersih hasil wrangling (14 kolom)
├── Data/
│   ├── customers_dataset.csv
│   ├── geolocation_dataset.csv
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── orders_dataset.csv
│   ├── product_category_name_translation.csv
│   ├── products_dataset.csv
│   └── sellers_dataset.csv
├── notebook.ipynb          ← Notebook analisis lengkap
├── README.md
├── requirements.txt
└── url.txt
```

---

## 🚀 Menjalankan Dashboard Secara Lokal

### 1. Clone repository
```bash
git clone https://github.com/nnabeelr1/submission-analisis-data-ecommerce.git
cd submission-analisis-data-ecommerce
```

### 2. Buat virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan dashboard
```bash
cd Dashboard
streamlit run dashboard.py
```

Dashboard akan otomatis terbuka di browser pada `http://localhost:8501`

---

## 🌐 Live Dashboard

Dashboard sudah di-deploy dan dapat diakses di:

**👉 [https://ecommerce-analysis-fathannabilr.streamlit.app](https://ecommerce-analysis-fathannabilr.streamlit.app)**

---

## 🛠️ Library yang Digunakan

| Library | Kegunaan |
|---------|----------|
| `pandas` | Data wrangling & manipulasi |
| `numpy` | Komputasi numerik |
| `matplotlib` | Visualisasi statis |
| `seaborn` | Visualisasi statistik |
| `folium` | Geospatial / peta interaktif |
| `streamlit` | Dashboard interaktif |

---

## 👤 Author

**Fathan Nabil Rahman**  
📧 nblrhmn5@students.unnes.ac.id  
🆔 Dicoding: `nabeelrr`

---

*Submission Proyek Akhir — Belajar Analisis Data dengan Python, Dicoding Academy*