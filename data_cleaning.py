import pandas as pd

def clean_data():
    print("Sedang memproses data... Mohon tunggu.")
    
    # 1. Load Data Mentah
    orders = pd.read_csv('data/olist_orders_dataset.csv')
    items = pd.read_csv('data/olist_order_items_dataset.csv')
    customers = pd.read_csv('data/olist_customers_dataset.csv')
    reviews = pd.read_csv('data/olist_order_reviews_dataset.csv')

    # 2. Merging (Menggabungkan tabel menjadi satu alur logistik)
    df = pd.merge(orders, customers, on='customer_id', how='left')
    df = pd.merge(df, items, on='order_id', how='left')
    df = pd.merge(df, reviews, on='order_id', how='left')

    # 3. Merapikan Format Tanggal
    date_cols = ['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date']
    for col in date_cols:
        df[col] = pd.to_datetime(df[col])

    # 4. Feature Engineering (Logika Logistik)
    # Menghitung selisih hari dari estimasi (SLA)
    df['delay_days'] = (df['order_delivered_customer_date'] - df['order_estimated_delivery_date']).dt.days
    
    # Menandai Peak Season (Bulan 11/November sebagai simulasi Lebaran)
    df['is_peak_season'] = df['order_purchase_timestamp'].dt.month == 11

    # 5. Membersihkan data kosong pada kolom penting
    df = df.dropna(subset=['order_delivered_customer_date', 'review_score'])

    # 6. Sampling (Ambil 20rb baris agar laptop tidak lag)
    df_sample = df.sample(n=20000, random_state=42)

    # 7. Simpan ke file baru
    df_sample.to_csv('data/cleaned_logistics.csv', index=False)
    print("✅ Selesai! File 'data/cleaned_logistics.csv' siap digunakan untuk dashboard.")

if __name__ == "__main__":
    clean_data()