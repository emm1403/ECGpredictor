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

    # Frecuencia cardíaca
    if hr < 60:
        st.warning("Frecuencia cardíaca baja: posible bradicardia")
        st.info("Recomendación: Consulte con un cardiólogo, especialmente si presenta mareos o fatiga.")
    elif hr > 100:
        st.warning("Frecuencia cardíaca alta: posible taquicardia")
        st.info("Recomendación: Se recomienda una evaluación médica para descartar estrés, fiebre o afecciones cardíacas.")
    else:
        st.success("Frecuencia cardíaca en rango normal")
        st.info("Recomendación: Mantenga un estilo de vida saludable con ejercicio regular y buena alimentación.")

    # Duración del QRS
    if qrs > 120:
        st.warning("QRS prolongado: posible bloqueo de rama")
        st.info("Recomendación: Realizar un electrocardiograma completo y consultar a un especialista en cardiología.")
    else:
        st.success("Duración del QRS en rango normal")
        st.info("Recomendación: No se requiere intervención. Continúe con sus chequeos regulares.")

    # Intervalo PR
    if pr < 120 or pr > 200:
        st.warning("PR fuera de rango: posible anormalidad del nodo AV")
        st.info("Recomendación: Monitoreo adicional puede ser necesario; consulte con un profesional de salud.")
    else:
        st.success("Intervalo PR normal")
        st.info("Recomendación: El funcionamiento del nodo AV parece adecuado.")

    # Intervalo QT
    if qt > 450:
        st.warning("QT prolongado: riesgo de arritmia")
        st.info("Recomendación: Evite medicamentos que prolonguen el QT y consulte a un médico para evaluación adicional.")
    else:
        st.success("Intervalo QT dentro de lo normal")
        st.info("Recomendación: No se detectan riesgos de arritmia con este valor de QT.")

    # RMS
    if rms < 0.1:
        st.warning("RMS bajo: señal débil o posible hipovolemia")
        st.info("Recomendación: Asegúrese de que los electrodos estén bien colocados; si el valor persiste, considere una evaluación clínica.")
    else:
        st.success("RMS de la señal ECG aceptable")
        st.info("Recomendación: La señal es clara y útil para el diagnóstico.")
