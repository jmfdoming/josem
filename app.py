import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Configuración de la página de Streamlit
st.title('Visualización de Ticker - Último Año')
st.write('Ingresa un ticker para ver el gráfico del último año de cotizaciones.')

# Input para ingresar el ticker
ticker = st.text_input('Ticker:', 'AAPL')

if ticker:
    # Obtención de datos del último año
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)
    
    data = yf.download(ticker, start=start_date, end=end_date)

    if not data.empty:
        # Crear el gráfico
        st.write(f"Gráfico de {ticker} del último año")
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Close'], label='Precio de Cierre', color='b')
        plt.xlabel('Fecha')
        plt.ylabel('Precio de Cierre (USD)')
        plt.title(f'Evolución del precio de {ticker} en el último año')
        plt.legend()
        plt.grid(True)
        
        # Mostrar gráfico en Streamlit
        st.pyplot(plt)
    else:
        st.write('No se encontraron datos para el ticker ingresado.')
