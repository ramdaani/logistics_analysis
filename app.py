import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Logistic Performance Analysis", layout="wide")

# Load Data yang sudah dibersihkan
@st.cache_data
def load_data():
    df = pd.read_csv('data/cleaned_logistics.csv')
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

df = load_data()

# --- HEADER ---
st.title("📦 Logistics Performance: Peak Season Diagnostic")
st.markdown("""
Dashboard ini mendiagnosa performa pengiriman pada periode **Peak Season (Simulasi Lebaran)** untuk melihat dampaknya terhadap kepuasan pelanggan.
""")

# --- METRIK UTAMA ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Paket dianalisis", f"{len(df):,}")
with col2:
    avg_delay = df[df['delay_days'] > 0]['delay_days'].mean()
    st.metric("Rata-rata Keterlambatan", f"{avg_delay:.1f} Hari", delta="Beresiko Tinggi", delta_color="inverse")
with col3:
    st.metric("Kepuasan Pelanggan (Avg)", f"{df['review_score'].mean():.2f} / 5.0")

st.markdown("---")

# --- GRAFIK 1: TRENS VOLUME ---
st.subheader("📊 Tren Volume Pesanan Bulanan")
df['month_year'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)
monthly_data = df.groupby('month_year').size().reset_index(name='total_orders')

fig_trend = px.line(monthly_data, x='month_year', y='total_orders', 
                    title="Deteksi Lonjakan Pesanan (Peak Season)", markers=True)
st.plotly_chart(fig_trend, use_container_width=True)

# --- GRAFIK 2: PEAK SEASON IMPACT ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("⚠️ Dampak Peak Season pada SLA")
    # Membandingkan persentase keterlambatan
    peak_comp = df.groupby('is_peak_season').agg({'delay_days': lambda x: (x > 0).mean() * 100}).reset_index()
    peak_comp['is_peak_season'] = peak_comp['is_peak_season'].map({True: 'Peak Season', False: 'Normal'})
    
    fig_peak = px.bar(peak_comp, x='is_peak_season', y='delay_days', 
                      labels={'delay_days': '% Paket Terlambat'},
                      color='is_peak_season', color_discrete_map={'Peak Season': 'red', 'Normal': 'blue'})
    st.plotly_chart(fig_peak)

with col_right:
    st.subheader("⭐ Keterlambatan vs Rating")
    # Melihat korelasi delay terhadap skor review
    df['status_kirim'] = df['delay_days'].apply(lambda x: 'Terlambat' if x > 0 else 'Tepat Waktu')
    rating_comp = df.groupby('status_kirim')['review_score'].mean().reset_index()
    
    fig_rating = px.bar(rating_comp, x='status_kirim', y='review_score', color='status_kirim')
    st.plotly_chart(fig_rating)

# --- KESIMPULAN ---
st.info(f"""
**Kesimpulan Analisis:**
1. Terjadi lonjakan volume signifikan pada bulan simulasi **Peak Season**.
2. Paket terlambat memiliki rata-rata rating **{df[df['delay_days']>0]['review_score'].mean():.2f}**, 
   jauh lebih rendah dibanding paket tepat waktu (**{df[df['delay_days']<=0]['review_score'].mean():.2f}**).
3. Rekomendasi: Penambahan kapasitas kurir di wilayah 'Zona Merah' saat H-14 Lebaran.
""")