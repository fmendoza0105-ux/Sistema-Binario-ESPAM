import streamlit as st
import base64
import random

# Configuración de página (Ancho completo)
st.set_page_config(page_title="Sistema Binario ESPAM", page_icon="💻", layout="wide")

# --- CONTROL DE ESTADOS DE SESIÓN (EVITA CAÍDAS DE PÁGINA) ---
if "juego_binario" not in st.session_state:
    st.session_state.juego_binario = format(random.randint(1, 100), "08b")
if "puntos" not in st.session_state:
    st.session_state.puntos = 0
if "estado_juego" not in st.session_state:
    st.session_state.estado_juego = "pendiente"  # Cambia a "correcto" o "incorrecto"

# Función limpia para pasar al siguiente reto sin romper el flujo de renderizado
def siguiente_ejercicio():
    st.session_state.juego_binario = format(random.randint(1, 100), "08b")
    st.session_state.estado_juego = "pendiente"

# Función para codificar la imagen del logo
def get_base64(file):
    try:
        with open(file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

logo = get_base64("logo-espam.png")

# --- ESTILOS CSS REFORZADOS ---
st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e0e0e0; }
    
    .main-header {
        background: linear-gradient(135deg, #02231c, #053f31);
        padding: 25px; border-radius: 12px; color: white; text-align: center;
        margin-bottom: 25px; border-bottom: 5px solid #00bc62;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .main-header h1 { color: #ffffff !important; font-size: 32px !important; margin-bottom: 5px; font-weight: 800; }
    .main-header h3 { color: #a3e635 !important; font-size: 18px !important; margin-top: 0; }

    .info-card {
        background: white; padding: 15px; border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04); border-left: 5px solid #053f31; height: 100%;
    }
    .info-card-title { font-weight: bold; color: #053f31; margin-bottom: 5px; font-size: 15px; }
    
    .custom-container {
        background: white; border-radius: 12px; border: 1px solid #e0e0e0;
        padding: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-top: 10px;
    }
    .custom-title-bar {
        background: #02231c; color: white; padding: 12px 20px;
        font-weight: bold; font-size: 16px; border-radius: 12px 12px 0 0; margin-top: 20px;
    }

    /* Caja "En Palabras" del Prototipo */
    .en-palabras-box {
        background: #f1fcf6; border: 2px dashed #00bc62;
        border-radius: 12px; padding: 20px; text-align: center; height: 100%;
        display: flex; flex-direction: column; justify-content: center;
    }

    /* LEDs Tridimensionales */
    .led-container { display: flex; justify-content: center; gap: 20px; margin: 25px 0; flex-wrap: wrap; width: 100%; }
    .led-box { text-align: center; width: 70px; display: inline-block; }
    .led { width: 60px; height: 60px; border-radius: 50%; margin: 0 auto 8px auto; border: 4px solid #333; }
    .led.on {
        background: radial-gradient(circle at 35% 35%, #60efff, #00bc62 60%, #01542c);
        box-shadow: inset 0 2px 5px rgba(255,255,255,0.7), 0 0 15px rgba(0, 188, 98, 0.7);
    }
    .led.off {
        background: radial-gradient(circle at 35% 35%, #555, #222 70%, #111);
        box-shadow: inset 0 2px 5px rgba(255,255,255,0.2);
    }
    .led-bit { font-size: 18px; font-weight: bold; color: #222; }

    .potencia-table { width: 100%; border-collapse: collapse; margin-top: 15px; background: #fafafa; border-radius: 8px; overflow: hidden; }
    .potencia-table th { background: #053f31; color: white; padding: 10px; font-size: 13px; border: 1px solid #e0e0e0; }
    .potencia-table td { padding: 12px; text-align: center; border: 1px solid #e0e0e0; font-size: 14px; }
    .active-row { background-color: #e8f5e9; font-weight: bold; color: #1b5e20; }

    .ascii-card { background: white; border: 2px solid #e0e0e0; border-radius: 12px; padding: 15px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
    .ascii-char { font-size: 28px; font-weight: bold; color: #053f31; }
    
    .miniled-container { display: flex; justify-content: center; gap: 3px; }
    .miniled { width: 10px; height: 10px; border-radius: 50%; }
    .miniled.on { background: #00bc62; box-shadow: 0 0 4px #00bc62; }
    .miniled.off { background: #bbb; }

    .footer-bar { background-color: #02231c; color: white; text-align: center; padding: 12px; font-size: 13px; border-radius: 8px; margin-top: 35px; }
</style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
logo_html = f'<img src="data:image/png;base64,{logo}" width="200">' if logo else '<h2 style="color:white;margin:0;">ESPAM MFL</h2>'
st.markdown(f"""
<div class='main-header'>
    <div style='display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;'>
        <div style='background: white; padding: 12px 25px; border-radius: 10px;'>{logo_html}</div>
        <div style='flex: 1; text-align: center; padding: 0 20px;'>
            <h1>SISTEMA BINARIO</h1>
            <h3>Escuela Superior Politécnica Agropecuaria de Manabí Manuel Félix López</h3>
            <p><strong>Feria de Ciencias 2026</strong> | Conocimiento que transforma, tecnología que impulsa el agro</p>
        </div>
        <div style='text-align: right; font-size: 13px; opacity: 0.9;'>
            <p><strong>Expositora Oficial:</strong></p>
            <p>Mgtr. Virginia Lucciola Mendoza Z. | <em>Docente</em></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- TARJETAS SUPERIORES ---
t1, t2, t3, t4 = st.columns(4)
with t1: st.markdown('<div class="info-card"><div class="info-card-title">🟢 ¿Qué es?</div><div class="info-card-desc">Usa solo 0 y 1. Es el lenguaje nativo universal de los procesadores del mundo.</div></div>', unsafe_allow_html=True)
with t2: st.markdown('<div class="info-card"><div class="info-card-title">🔌 ¿Por qué se usa?</div><div class="info-card-desc">Los transistores electrónicos solo entienden dos estados: apagado (0) o encendido (1).</div></div>', unsafe_allow_html=True)
with t3: st.markdown('<div class="info-card"><div class="info-card-title">🔢 Equivalencia</div><div class="info-card-desc">Cada posición de un bit de derecha a izquierda duplica su valor (1, 2, 4, 8, 16, 32, 64, 128).</div></div>', unsafe_allow_html=True)
with t4: st.markdown('<div class="info-card"><div class="info-card-title">💡 Datos e IA</div><div class="info-card-desc">Cualquier red, imagen, Inteligencia Artificial o sensor IoT en el agro transmite pulsos binarios.</div></div>', unsafe_allow_html=True)

# --- BARRA LATERAL (CONVERSOR + JUEGO CON EFECTOS CORREGIDOS) ---
with st.sidebar:
    st.markdown("<h2 style='color:#053f31; text-align:center;'>🔄 CONVERSOR</h2>", unsafe_allow_html=True)
    entrada = st.text_input("Número o Texto:", value="42")
    
    st.markdown("---")
    st.markdown("<h3 style='color:#00bc62; text-align:center;'>🎮 TRIVIA INTERACTIVA</h3>", unsafe_allow_html=True)
    st.write("¿Qué número decimal representa este código binario?")
    st.info(f"👉 **`{st.session_state.juego_binario}`**")
    
    respuesta_usuario = st.text_input("Tu respuesta decimal:", key="quiz_input")
    
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        btn_comprobar = st.button("Comprobar 🎯", use_container_width=True)
    with col_b2:
        btn_siguiente = st.button("Siguiente ➡️", use_container_width=True, on_click=siguiente_ejercicio)
        
    # Evaluar la respuesta al pulsar el botón sin recargar abruptamente la app
    if btn_comprobar and respuesta_usuario:
        solucion = int(st.session_state.juego_binario, 2)
        if respuesta_usuario.isdigit() and int(respuesta_usuario) == solucion:
            st.session_state.estado_juego = "correcto"
            st.session_state.puntos += 10
        else:
            st.session_state.estado_juego = "incorrecto"

    # Muestra los efectos según el estado guardado
    if st.session_state.estado_juego == "correcto":
        st.balloons()  # Despliega los globos de manera estable
        st.success("🎉 ¡CORRECTO! ¡Eres un genio binario! (+10 pts). Presiona 'Siguiente ➡️' para otro reto.")
    elif st.session_state.estado_juego == "incorrecto":
        st.snow()  # Efecto de copos de nieve
        st.error("😢 ¡Oh no! Inténtalo de nuevo. El sistema se ha congelado. ¡Mira la tabla central para guiarte!")
            
    st.metric("Score del Stand 🏆", f"{st.session_state.puntos} pts")

# --- LÓGICA CENTRAL ---
if entrada:
    if entrada.isdigit():
        numero = int(entrada)
        num_bits = max(8, numero.bit_length())
        binario = format(numero, f"0{num_bits}b")
        hexa = hex(numero).upper().replace("0X", "#")
        pesos = [2**i for i in range(len(binario)-1, -1, -1)]

        st.markdown('<div class="custom-title-bar">💻 TABLERO BINARIO EN TIEMPO REAL</div>', unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="custom-container">', unsafe_allow_html=True)
            
            col_izq, col_der = st.columns([3, 1.2])
            
            with col_izq:
                m1, m2, m3 = st.columns([1, 2, 1])
                m1.markdown(f"<div style='text-align:center;'><h3>Decimal</h3><h1 style='color:#053f31; font-size:45px; margin:0;'>{numero}</h1></div>", unsafe_allow_html=True)
                m2.markdown(f"<div style='text-align:center;'><h3>Binario</h3><h1 style='color:#00bc62; font-size:45px; font-family:monospace; letter-spacing:4px; margin:0;'>{binario}</h1></div>", unsafe_allow_html=True)
                m3.markdown(f"<div style='text-align:center;'><h3>Hex</h3><h1 style='color:#7b2cbf; font-size:45px; margin:0;'>{hexa}</h1></div>", unsafe_allow_html=True)
                
                # Renderizado de LEDs
                leds_html = "<div class='led-container'>"
                for bit in binario:
                    estado = "on" if bit == "1" else "off"
                    leds_html += f"""<div class='led-box'><div class='led {estado}'></div><div class='led-bit'>{bit}</div></div>"""
                leds_html += "</div>"
                st.markdown(leds_html, unsafe_allow_html=True)
            
            with col_der:
                componentes_texto = [str(pesos[i]) for i in range(len(binario)) if binario[i] == "1"]
                if componentes_texto:
                    frase_matematica = " más ".join(componentes_texto) + f" es igual a {numero}"
                else:
                    frase_matematica = f"Ningún bit activo es igual a {numero}"
                
                st.markdown(f"""
                <div class="en-palabras-box">
                    <b style="color:#00bc62; font-size:14px;">📝 EN PALABRAS:</b>
                    <p style="font-size:16px; margin:10px 0; font-weight:500; color:#333; line-height:1.5;">
                        <i>"{frase_matematica.capitalize()}"</i>
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            # Gráfico de consumo físico
            activos = binario.count("1")
            pct_energia = (activos / len(binario)) * 100
            st.markdown(f"**⚡ Carga de Voltaje en los Transistores del Bus de Datos ({round(pct_energia,1)}%):**")
            st.progress(activos / len(binario))
            
            # Tabla de posición matemática
            st.markdown("### 🔢 Desglose y Posición Matemática de los Bits")
            th_potencias = "".join([f"<th>2<sup>{len(binario)-1-i}</sup></th>" for i in range(len(binario))])
            td_pesos = "".join([f"<td>{p}</td>" for p in pesos])
            td_valores = "".join([f"<td class='{'active-row' if b=='1' else ''}'>{p if b=='1' else 0}</td>" for p, b in zip(pesos, binario)])
            
            tabla_html = f"""
            <table class="potencia-table">
                <tr><th style='background:#02231c;'>Posición (Potencia)</th>{th_potencias}</tr>
                <tr><td style='font-weight:bold; background:#f0f0f0;'>Valor del Peso</td>{td_pesos}</tr>
                <tr><td style='font-weight:bold; background:#f0f0f0;'>Suma Resultante</td>{td_valores}</tr>
            </table>
            """
            st.markdown(tabla_html, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        # TRADUCTOR TEXTO A ASCII
        st.markdown('<div class="custom-title-bar">🔠 TRADUCTOR TEXTO ➔ ASCII ➔ BINARIO</div>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="custom-container">', unsafe_allow_html=True)
            letras = [ch for ch in entrada]
            cols = st.columns(len(letras))
            for i, ch in enumerate(letras):
                ascii_val = ord(ch)
                bin_val = format(ascii_val, "08b")
                minileds = "".join([f"<div class='miniled {'on' if b=='1' else 'off'}'></div>" for b in bin_val])
                with cols[i]:
                    st.markdown(f"""
                    <div class="ascii-card">
                        <div class="ascii-char">{ch}</div>
                        <div class="ascii-meta"><b>ASCII:</b> {ascii_val}<br>
                        <span style="font-family:monospace; font-weight:bold; color:#00bc62;">{bin_val}</span></div>
                        <div class="miniled-container">{minileds}</div>
                    </div>
                    """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.toast("¡Conversión de texto completada con éxito! 🚀")

# --- SECCIÓN INFERIOR: APLICACIONES REALES ---
st.markdown("<br><h3 style='color:#053f31;'>🌍 Aplicaciones del Sistema Binario en el Mundo Real</h3>", unsafe_allow_html=True)
a1, a2, a3, a4, a5 = st.columns(5)
apps = [
    ("💾 Almacenamiento", "Fotos, videos y archivos se guardan como miles de millones de ceros y unos en discos magnéticos o sólidos."),
    ("🌐 Redes e Internet", "Los datos viajan por fibra óptica como pulsos rápidos de luz (1) y total oscuridad (0)."),
    ("🔒 Criptografía", "La seguridad web y contraseñas dependen de mezclar bits usando operadores lógicos."),
    ("🤖 Inteligencia Artificial", "Las redes neuronales procesan billones de operaciones matemáticas que en su base son interruptores binarios."),
    ("🚜 Agricultura IoT", "Sensores miidieron humedad en Calceta, convierten el dato físico a bits y lo envían vía satélite a la nube.")
]
for col, (title, desc) in zip([a1, a2, a3, a4, a5], apps):
    with col:
        st.markdown(f'<div style="background: white; padding: 15px; border-radius: 10px; border-top: 4px solid #00bc62; box-shadow: 0 4px 6px rgba(0,0,0,0.03); height:100%;"><b style="color:#053f31;">{title}</b><p style="font-size:12px; color:#555; margin-top:8px;">{desc}</p></div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<div class="footer-bar">ESPAM MFL | Feria de Ciencias de Ingeniería 2026 — Calceta, Manabí, Ecuador</div>', unsafe_allow_html=True)
