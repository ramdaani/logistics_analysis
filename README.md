# 📦 Logistics Diagnostic: E-Commerce SLA Performance & Peak Season Analysis

![Dashboard Utama](dashboard.png)

## 📌 Project Overview
Proyek ini bertujuan untuk mendiagnosa performa logistik dan ketepatan waktu pengiriman (**SLA - Service Level Agreement**) pada platform e-commerce Olist. Fokus utama analisis ini adalah memahami bagaimana lonjakan pesanan pada periode **Peak Season** (Simulasi Ramadhan/Lebaran) mempengaruhi keterlambatan paket dan kepuasan pelanggan.

## 📉 Problem Statement
Perusahaan ekspedisi (seperti J&T, SPX, atau Sicepat) sering menghadapi tantangan besar saat volume pesanan naik drastis:
1. **SLA Breach:** Banyak paket yang sampai melebihi estimasi waktu yang dijanjikan.
2. **Bottleneck Operasional:** Penumpukan barang di gudang sortir (*hub*) mengakibatkan keterlambatan berantai.
3. **Customer Churn:** Keterlambatan pengiriman, terutama saat momen penting (seperti Lebaran), berakibat langsung pada penurunan skor ulasan (*review score*) dan hilangnya kepercayaan pelanggan.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Plotly Express
* **Dashboard Framework:** Streamlit
* **Database Logic:** SQL (CTE & Window Functions)

## 📊 Key Features & Analysis

![tren](volume_pesanan_bulanan.png)
![peak season](dampak_peak_season.png)
![keterlambatan vs rating](keterlambatan_vs_rating.png)

* **Peak Season Simulation:** Menganalisis data bulan November (Black Friday) sebagai analogi lonjakan transaksi Ramadhan/Lebaran di Indonesia.
* **Delivery Gap Analysis:** Menghitung selisih hari antara kedatangan aktual vs estimasi (*SLA Breach*).
* **Correlation Study:** Menghubungkan durasi keterlambatan dengan penurunan rating bintang dari pelanggan.
* **Interactive Dashboard:** Visualisasi real-time untuk memantau "Zona Merah" pengiriman.

## 🚀 Insight & Findings
* **Volume vs Delay:** Terdapat korelasi positif di mana kenaikan volume sebesar 30% pada Peak Season mengakibatkan kenaikan angka keterlambatan sebesar 45%.
* **The Rating Impact:** Pelanggan cenderung memberikan rating di bawah 3.0 jika paket terlambat lebih dari 2 hari dari estimasi.
* **Geographical Bottleneck:** Wilayah dengan jarak tempuh menengah seringkali mengalami delay lebih parah karena proses transit yang tidak efisien di gudang pusat.

## 💡 Business Recommendations
1. **Dynamic SLA:** Memberikan estimasi waktu yang lebih fleksibel saat periode High Season untuk menjaga ekspektasi pelanggan.
2. **Staffing Optimization:** Penambahan tenaga kurir *freelance* pada H-14 hingga H-7 sebelum hari puncak.
3. **Priority Handling:** Mendahulukan kategori produk dengan margin tinggi agar mendapatkan jalur pengiriman prioritas.

---

## 🏗️ How to Run
1. Clone repositori ini.
2. Pastikan file dataset Olist ada di dalam folder `data/`.
3. Instal library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
4. python data_cleaning.py
5. streamlit run app.py