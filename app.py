import streamlit as st
import pickle
import numpy as np

# Load model pickle
with open('model_harga_rumah.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Aplikasi Prediksi Harga Rumah di Yogyakarta")
st.write("Masukkan spesifikasi rumah untuk memprediksi estiamasi harga.")

# Input dari user
surface = st.number_input("Luas Tanah (m²)", min_value=10, value=100)
building = st.number_input("Luas Bangunan (m²)", min_value=10, value=80)
bed = st.number_input("Jumlah Kamar Tidur", min_value=1, value=3)
bath = st.number_input("Jumlah Kamar Mandi", min_value=1, value=2)
carport = st.number_input("Kapasitas Carport (Mobil)", min_value=0, value=1)

# Tombol Prediksi
if st.button("Hitung Estimasi Harga"):
    input_data = np.array([[surface, building, bed, bath, carport]])
    prediction = model.predict(input_data)[0]
    
    if prediction >= 1000:
        st.success(f"Estimasi Harga: Rp {prediction/1000:.2f} Miliar")
    else:
        st.success(f"Estimasi Harga: Rp {prediction:.2f} Juta")