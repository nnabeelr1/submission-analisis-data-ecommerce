# 🛒 E-Commerce Analytics Dashboard
### Brazilian Olist E-Commerce Public Dataset — Dicoding Data Analysis Project

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-green?logo=pandas)
![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)

---

## 📌 Deskripsi Proyek

Proyek ini merupakan **proyek akhir** dari kelas **Belajar Analisis Data dengan Python** di Dicoding Academy. Analisis dilakukan terhadap **Brazilian E-Commerce Public Dataset by Olist** — salah satu dataset e-commerce terbesar di Brasil yang mencakup lebih dari **100.000 transaksi** sejak September 2016 hingga Agustus 2018.

Proyek ini mencakup seluruh pipeline analisis data, mulai dari **data wrangling**, **exploratory data analysis (EDA)**, **analisis lanjutan (RFM & Geospatial)**, hingga **dashboard interaktif** berbasis Streamlit.

---

## 🔍 Pertanyaan Bisnis

| # | Pertanyaan |
|---|------------|
| 1 | Bagaimana tren jumlah order dan total revenue per bulan selama **2017–2018**, dan pada bulan apa terjadi puncak penjualan tertinggi? |
| 2 | Kategori produk mana yang menghasilkan total revenue tertinggi dan terendah selama 2016–2018, dan berapa perbandingan rata-rata nilai transaksinya? |
| 3 *(RFM)* | Berdasarkan data transaksi 2016–2018, berapa persentase pelanggan yang termasuk segmen **Champions** dan **At Risk** menggunakan metode RFM, serta strategi retensi apa yang paling tepat untuk masing-masing segmen? |
| 4 *(Geospatial)* | State mana yang memiliki **rata-rata waktu pengiriman tertinggi** selama 2016–2018, dan berapa selisih harinya dibandingkan rata-rata nasional? |

---

## 📊 Key Findings

| Metrik | Nilai |
|--------|-------|
| Total Order (delivered) | 96.478 |
| Total Revenue | R$ 15.420.000+ |
| Rata-rata Order/Bulan | ~4.097 order |
| Puncak Order | November 2017 — 7.289 order (Black Friday) |
| Kategori Revenue Tertinggi | `health_beauty` (~R$ 1,26M) |
| Pelanggan Champions | 6.497 (7,0%) |
| Pelanggan At Risk | 22.230 (23,8%) |
| State Pelanggan Terbesar | São Paulo (SP) |
| Rata-rata Delivery Time Nasional | ~12–13 hari |
| Delivery Time Terlama | RR, AP, AM, AC, PA — 20–30+ hari |

---

## 🧠 Teknik Analisis

### RFM Analysis
Segmentasi pelanggan berdasarkan 3 dimensi perilaku pembelian menggunakan metode **quintile scoring (1–5)**:

- **Recency (R)** — seberapa baru pelanggan melakukan transaksi (semakin kecil = semakin baik)
- **Frequency (F)** — seberapa sering pelanggan bertransaksi dalam periode data
- **Monetary (M)** — total pengeluaran pelanggan

Menghasilkan 6 segmen pelanggan: **Champions**, Loyal Customers, Recent Customers, Potential Loyalists, At Risk, dan Lost. Segmen Champions (avg. R$312/transaksi) diprioritaskan dengan program loyalty eksklusif, sementara segmen At Risk ditangani melalui kampanye re-engagement berbasis waktu.

### Geospatial Analysis
Analisis distribusi geografis pelanggan dan seller di 27 state Brasil menggunakan **Folium HeatMap** dan bubble map interaktif — mengidentifikasi ketimpangan distribusi seller yang berdampak langsung pada waktu pengiriman. State wilayah Utara (RR, AP, AM, AC, PA) mencatat selisih pengiriman **10–18 hari** di atas rata-rata nasional.

### Delivery Time Analysis
Mengukur rata-rata waktu pengiriman per state dan membuktikan korelasi antara kepadatan seller lokal dengan kecepatan pengiriman. State São Paulo (SP) menjadi yang tercepat karena konsentrasi seller tertinggi berada di sana.

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

Dashboard sudah di-deploy dan dapat diakses langsung di:

**👉 [https://ecommerce-analysis-fathannabilr.streamlit.app](https://ecommerce-analysis-fathannabilr.streamlit.app)**

---

## 🛠️ Library yang Digunakan

| Library | Kegunaan |
|---------|----------|
| `pandas` | Data wrangling & manipulasi |
| `numpy` | Komputasi numerik |
| `matplotlib` | Visualisasi statis |
| `seaborn` | Visualisasi statistik |
| `folium` | Peta interaktif & analisis geospatial |
| `streamlit` | Dashboard interaktif |

---

## 👤 Author

**Fathan Nabil Rahman**
📧 nblrhmn5@students.unnes.ac.id
🆔 Dicoding: `nabeelrr`

---

*Submission Proyek Akhir — Belajar Analisis Data dengan Python, Dicoding Academy*