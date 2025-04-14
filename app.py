import streamlit as st

st.title('Cardio Diagnóstico')

# Entradas del usuario
hr = st.number_input('Frecuencia cardíaca (ppm)', min_value=30, max_value=200, value=75)
qrs = st.number_input('Duración del QRS (ms)', min_value=40, max_value=200, value=100)
pr = st.number_input('Intervalo PR (ms)', min_value=80, max_value=320, value=160)
qt = st.number_input('Intervalo QT (ms)', min_value=150, max_value=600, value=400)
rms = st.number_input('RMS de la señal ECG', min_value=0.0, value=0.2)

# Botón para analizar
if st.button('Analizar ECG'):
    st.subheader('Resultados del análisis:')

    if hr < 60:
        st.warning("Frecuencia cardíaca baja: posible bradicardia")
    elif hr > 100:
        st.warning("Frecuencia cardíaca alta: posible taquicardia")
    else:
        st.success("Frecuencia cardíaca en rango normal")

    if qrs > 120:
        st.warning("QRS prolongado: posible bloqueo de rama")
    else:
        st.success("Duración del QRS en rango normal")

    if pr < 120 or pr > 200:
        st.warning("PR fuera de rango: posible anormalidad del nodo AV")
    else:
        st.success("Intervalo PR normal")

    if qt > 450:
        st.warning("QT prolongado: riesgo de arritmia")
    else:
        st.success("Intervalo QT dentro de lo normal")

    if rms < 0.1:
        st.warning("RMS bajo: señal débil o posible hipovolemia")
    else:
        st.success("RMS de la señal ECG aceptable")
