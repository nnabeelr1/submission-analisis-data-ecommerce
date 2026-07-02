<div align="center">

# 🛒 E-Commerce Analytics Dashboard

**Analisis Data End-to-End Brazilian Olist E-Commerce — Dicoding Submission**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Folium](https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=leaflet&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)

Proyek analisis data end-to-end terhadap **Brazilian E-Commerce Public Dataset by Olist** — mencakup lebih dari **100.000 transaksi**, dilengkapi analisis **RFM**, **Geospatial**, hingga **dashboard interaktif** berbasis Streamlit.

</div>

---

## 📋 Daftar Isi

- [Gambaran Umum](#-gambaran-umum)
- [Alur Analisis](#-alur-analisis)
- [Pertanyaan Bisnis](#-pertanyaan-bisnis)
- [Key Findings](#-key-findings)
- [Teknologi](#-teknologi)
- [Struktur Folder](#-struktur-folder)
- [Detail Analisis](#-detail-analisis)
- [Skema Data](#-skema-data)
- [Instalasi & Setup](#-instalasi--setup)
- [Menjalankan Dashboard](#-menjalankan-dashboard)
- [Live Dashboard](#-live-dashboard)
- [Author](#-author)

---

## 🌟 Gambaran Umum

E-Commerce Analytics Dashboard adalah proyek analisis data end-to-end terhadap **Brazilian E-Commerce Public Dataset by Olist** — salah satu dataset e-commerce terbesar di Brasil yang mencakup lebih dari **100.000 transaksi** dari September 2016 hingga Agustus 2018.

> Proyek ini merupakan submission **Belajar Analisis Data dengan Python** di Dicoding Academy, mengimplementasikan pipeline analisis data lengkap mulai dari *data wrangling*, *exploratory data analysis (EDA)*, *analisis lanjutan (RFM & Geospatial)*, hingga *dashboard interaktif*.

---

## 🔄 Alur Analisis

```
9 Dataset CSV (Olist E-Commerce Public Dataset)
              │
              ▼
      [1] DATA WRANGLING
  • Merge multi-tabel (orders, items, payments,
    reviews, products, customers, sellers)
  • Handling missing values & duplikasi
  • Konversi tipe data & feature engineering
  • Output: main_data.csv (data bersih, 14 kolom)
              │
              ▼
      [2] EXPLORATORY DATA ANALYSIS
  • Tren order & revenue per bulan (2017–2018)
  • Distribusi kategori produk & revenue
  • Pola waktu pengiriman per state Brasil
              │
              ▼
      [3] ANALISIS LANJUTAN
  ┌──────────────────┬──────────────────┬──────────────────┐
  │                  │                  │                  │
RFM Analysis   Geospatial Analysis  Delivery Analysis
Segmentasi     Distribusi pelanggan  Rata-rata waktu
pelanggan      & seller per state    pengiriman per state
(6 segmen)     (Folium HeatMap)      (bar chart ranking)
              │
              ▼
      [4] DASHBOARD INTERAKTIF
  Streamlit app — filter dinamis, visualisasi
  interaktif, deployed di Streamlit Cloud
```

---

## 🔍 Pertanyaan Bisnis

| # | Pertanyaan |
|---|---|
| 1 | Bagaimana tren jumlah order dan total revenue per bulan selama **2017–2018**, dan pada bulan apa terjadi puncak penjualan tertinggi? |
| 2 | Kategori produk mana yang menghasilkan total revenue **tertinggi dan terendah** selama 2016–2018, dan berapa perbandingan rata-rata nilai transaksinya? |
| 3 *(RFM)* | Berapa persentase pelanggan yang termasuk segmen **Champions** dan **At Risk** menggunakan metode RFM, serta strategi retensi apa yang paling tepat untuk masing-masing segmen? |
| 4 *(Geospatial)* | State mana yang memiliki **rata-rata waktu pengiriman tertinggi** selama 2016–2018, dan berapa selisih harinya dibandingkan rata-rata nasional? |

---

## 📊 Key Findings

| Metrik | Nilai |
|--------|-------|
| Total Order (delivered) | **96.478** |
| Total Revenue | **R$ 15.420.000+** |
| Rata-rata Order/Bulan | ~4.097 order |
| Puncak Order | November 2017 — **7.289 order** (Black Friday) |
| Kategori Revenue Tertinggi | `health_beauty` (~R$ 1,26M) |
| Pelanggan Champions | **6.497** (7,0%) |
| Pelanggan At Risk | **22.230** (23,8%) |
| State Pelanggan Terbesar | São Paulo (SP) |
| Rata-rata Delivery Time Nasional | ~12–13 hari |
| Delivery Time Terlama | RR, AP, AM, AC, PA — **20–30+ hari** |

---

## 🛠️ Teknologi

| Bagian | Teknologi |
|---|---|
| Analisis & Manipulasi Data | `pandas` ~3.0, `numpy` ~2.4 |
| Visualisasi Statis | `matplotlib` ~3.10, `seaborn` ~0.13 |
| Peta Interaktif | `folium` ~0.20 |
| Dashboard Interaktif | `streamlit` ~1.56 |
| Notebook | `jupyter` |
| HTTP Requests | `requests` ~2.33 |

---

## 📁 Struktur Folder

```
submission/
│
├── Dashboard/
│   ├── dashboard.py        # Streamlit dashboard app
│   └── main_data.csv       # Data bersih hasil wrangling (14 kolom)
│
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
│
├── notebook.ipynb          # Notebook analisis lengkap (wrangling → EDA → RFM → Geo)
├── requirements.txt        # Daftar dependency Python
├── README.md
└── url.txt                 # URL live dashboard
```

---

## 🔍 Detail Analisis

### 📥 Data Wrangling — `notebook.ipynb`

Menggabungkan 9 tabel dataset Olist menjadi satu `main_data.csv` yang bersih dan siap analisis.

| Langkah | Yang Dilakukan |
|---|---|
| Merge Tabel | Join `orders` ← `order_items`, `payments`, `reviews`, `products`, `customers`, `sellers` |
| Handling Missing Values | Drop baris dengan nilai kritis null (tanggal pengiriman, harga, status order) |
| Hapus Duplikat | Drop baris duplikat berdasarkan `order_id` |
| Feature Engineering | Hitung `delivery_time` (aktual vs estimasi), ekstrak `order_year_month` |
| Konversi Tipe Data | Parse kolom tanggal ke `datetime`, konversi kolom numerik |
| Translate Kategori | Join dengan `product_category_name_translation.csv` → nama kategori bahasa Inggris |

---

### 🧠 RFM Analysis

Segmentasi pelanggan berdasarkan 3 dimensi perilaku pembelian menggunakan **quintile scoring (1–5)**:

| Dimensi | Definisi | Interpretasi Skor |
|---|---|---|
| **Recency (R)** | Seberapa baru pelanggan melakukan transaksi | Skor tinggi = lebih baru (lebih baik) |
| **Frequency (F)** | Seberapa sering pelanggan bertransaksi | Skor tinggi = lebih sering |
| **Monetary (M)** | Total pengeluaran pelanggan | Skor tinggi = lebih besar |

**6 Segmen Hasil:**

| Segmen | Kriteria | Strategi |
|---|---|---|
| **Champions** | R≥4, F≥4, M≥4 | Program loyalty eksklusif, early access produk baru |
| **Loyal Customers** | F≥3, M≥3 | Reward point, upsell ke produk premium |
| **Recent Customers** | R≥4 | Onboarding sequence, cross-sell produk relevan |
| **Potential Loyalists** | R≥3, F≥2 | Nurturing berkala, diskon loyalitas |
| **At Risk** | R≤2, F≥2 | Re-engagement campaign berbasis waktu |
| **Lost** | R=1, F=1 | Win-back campaign atau realokasi anggaran |

> 💡 Champions rata-rata membelanjakan **R$312/transaksi** — **2,3× di atas** rata-rata pelanggan At Risk.

---

### 🗺️ Geospatial Analysis

Analisis distribusi geografis pelanggan dan seller di **27 state Brasil** menggunakan **Folium HeatMap** dan bubble map interaktif.

| Temuan | Detail |
|---|---|
| Konsentrasi tertinggi | São Paulo (SP) — pelanggan & seller terbanyak di Brasil |
| Delivery time tercepat | SP — ~8 hari (kepadatan seller lokal tertinggi) |
| Delivery time terlambat | RR, AP, AM, AC, PA — 20–30+ hari |
| Gap terlebar | Roraima (RR): ~28 hari vs rata-rata nasional ~13 hari **(+15 hari)** |

> ⚠️ Ketimpangan distribusi seller menjadi **faktor utama** perbedaan delivery time antar wilayah — bukan sekadar jarak geografis.

---

## 🗂️ Skema Data

Skema `main_data.csv` setelah wrangling selesai:

| Kolom | Tipe | Deskripsi | Contoh |
|---|---|---|---|
| `order_id` | `str` | ID unik transaksi | `"abc123..."` |
| `customer_id` | `str` | ID pelanggan per order | `"xyz456..."` |
| `customer_unique_id` | `str` | ID unik pelanggan (dedup) | `"def789..."` |
| `order_status` | `str` | Status order | `"delivered"` |
| `order_purchase_timestamp` | `datetime` | Waktu pembelian | `2017-11-17 19:28:06` |
| `order_delivered_customer_date` | `datetime` | Tanggal terima aktual | `2017-11-29 00:00:00` |
| `order_estimated_delivery_date` | `datetime` | Estimasi pengiriman | `2017-12-05 00:00:00` |
| `payment_value` | `float` | Nilai pembayaran (R$) | `169.90` |
| `review_score` | `int` | Skor ulasan pelanggan (1–5) | `5` |
| `product_category_name_english` | `str` | Kategori produk (Inggris) | `"health_beauty"` |
| `customer_state` | `str` | State asal pelanggan | `"SP"` |
| `seller_state` | `str` | State asal seller | `"SP"` |
| `delivery_time` | `float` | Waktu pengiriman aktual (hari) | `12.0` |
| `order_year_month` | `str` | Periode order | `"2017-11"` |

---

## 🚀 Instalasi & Setup

### Prasyarat

Pastikan sudah terinstall:
- Python **3.9+**
- `pip` versi terbaru

### 1. Clone Repository

```bash
git clone https://github.com/nnabeelr1/submission-analisis-data-ecommerce.git
cd submission-analisis-data-ecommerce
```

### 2. Buat & Aktifkan Virtual Environment

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan (Windows)
venv\Scripts\activate

# Aktifkan (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Dashboard

```bash
cd Dashboard
streamlit run dashboard.py
```

Dashboard akan otomatis terbuka di browser pada:

```
http://localhost:8501
```

**Fitur dashboard:**

| Fitur | Deskripsi |
|---|---|
| 📈 Tren Order & Revenue | Grafik interaktif jumlah order & total revenue per bulan |
| 📦 Kategori Produk | Top/bottom kategori berdasarkan revenue & volume order |
| 👥 RFM Segmentation | Scatter plot & tabel distribusi 6 segmen pelanggan |
| 🗺️ Geospatial Map | HeatMap & bubble map distribusi pelanggan & seller per state |
| 🚚 Delivery Time Analysis | Ranking rata-rata waktu pengiriman per state Brasil |

---

## 🌐 Live Dashboard

Dashboard sudah di-deploy dan dapat diakses langsung:

**👉 [https://ecommerce-analysis-fathannabilr.streamlit.app](https://ecommerce-analysis-fathannabilr.streamlit.app)**

---

## 👤 Author

**Fathan Nabil Rahman**
📧 nblrhmn5@students.unnes.ac.id
🆔 Dicoding: `nabeelrr`

---

*Submission Proyek Akhir — Belajar Analisis Data dengan Python, Dicoding Academy*
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