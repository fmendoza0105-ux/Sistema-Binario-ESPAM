import streamlit as st
import base64

# Configuración de página (Ancho completo)
st.set_page_config(page_title="Sistema Binario ESPAM", page_icon="💻", layout="wide")

# Función para codificar la imagen del logo
def get_base64(file):
    try:
        with open(file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

logo = get_base64("logo-espam.png")

# --- ESTILOS CSS PARA REPLICAR EL PROTOTIPO ---
st.markdown("""
<style>
    /* Fondo general de la app (Gris claro premium) */
    .stApp {
        background-color: #f4f7f6;
    }
    
    /* Configuración de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    
    /* Encabezado Principal */
    .main-header {
        background: linear-gradient(135deg, #02231c, #053f31);
        padding: 25px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        border-bottom: 5px solid #00bc62;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    .main-header h1 { color: #ffffff !important; font-size: 32px !important; margin-bottom: 5px; font-weight: 800; letter-spacing: 1px; }
    .main-header h3 { color: #a3e635 !important; font-size: 18px !important; margin-top: 0; font-weight: 400; }
    .main-header p { margin: 2px 0; font-size: 14px; opacity: 0.9; }

    /* Tarjetas Informativas Superiores (Grid) */
    .info-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
        border-left: 5px solid #053f31;
        height: 100%;
    }
    .info-card-title {
        font-weight: bold;
        color: #053f31;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 15px;
    }
    .info-card-desc {
        color: #555;
        font-size: 12.5px;
        line-height: 1.4;
    }

    /* Contenedor de Resultados (Tablero) */
    .results-container {
        background: white;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        margin-top: 20px;
        overflow: hidden;
    }
    .results-title-bar {
        background: #02231c;
        color: white;
        padding: 12px 20px;
        font-weight: bold;
        font-size: 16px;
    }
    .results-body {
        padding: 25px;
    }

    /* LEDs Tridimensionales (Copiados exactamente del Prototipo) */
    .led-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 25px 0;
        flex-wrap: wrap;
    }
    .led-box {
        text-align: center;
        width: 65px;
    }
    .led {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        margin: 0 auto 8px auto;
        border: 4px solid #333;
        transition: all 0.3s ease;
    }
    /* LED Encendido: Degradado verde radial con brillo */
    .led.on {
        background: radial-gradient(circle at 35% 35%, #60efff, #00bc62 60%, #01542c);
        box-shadow: inset 0 2px 5px rgba(255,255,255,0.7), 0 0 15px rgba(0, 188, 98, 0.7);
    }
    /* LED Apagado: Gris oscuro metalizado */
    .led.off {
        background: radial-gradient(circle at 35% 35%, #555, #222 70%, #111);
        box-shadow: inset 0 2px 5px rgba(255,255,255,0.2);
    }
    .led-bit {
        font-size: 16px;
        font-weight: bold;
        color: #333;
    }

    /* Tabla de Pesos/Potencias como el prototipo */
    .potencia-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        background: #fafafa;
        border-radius: 8px;
        overflow: hidden;
    }
    .potencia-table th {
        background: #053f31;
        color: white;
        padding: 8px;
        font-size: 13px;
        font-weight: normal;
        border: 1px solid #e0e0e0;
    }
    .potencia-table td {
        padding: 10px;
        text-align: center;
        border: 1px solid #e0e0e0;
        font-size: 14px;
    }
    .active-row { background-color: #e8f5e9; font-weight: bold; color: #1b5e20; }

    /* Tarjetas de Letras ASCII */
    .ascii-card {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .ascii-char { font-size: 28px; font-weight: bold; color: #053f31; margin-bottom: 5px; }
    .ascii-meta { font-size: 12px; color: #666; margin-bottom: 10px; }
    
    /* Minileds para la sección ASCII */
    .miniled-container { display: flex; justify-content: center; gap: 3px; }
    .miniled { width: 10px; height: 10px; border-radius: 50%; }
    .miniled.on { background: #00bc62; box-shadow: 0 0 4px #00bc62; }
    .miniled.off { background: #bbb; }

    /* Estilo del Footer */
    .footer-bar {
        background-color: #02231c;
        color: white;
        text-align: center;
        padding: 12px;
        font-size: 13px;
        border-radius: 8px;
        margin-top: 35px;
    }
</style>
""", unsafe_allow_html=True)

# --- SECCIÓN ENCABEZADO (LOGO + TÍTULOS) ---
logo_html = f'<img src="data:image/png;base64,{logo}" width="200">' if logo else '<h2 style="color:white;margin:0;">ESPAM MFL</h2>'

st.markdown(f"""
<div class='main-header'>
    <div style='display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;'>
        <div style='background: white; padding: 12px 25px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>{logo_html}</div>
        <div style='flex: 1; text-align: center; padding: 0 20px;'>
            <h1>SISTEMA BINARIO</h1>
            <h3>Escuela Superior Politécnica Agropecuaria de Manabí Manuel Félix López</h3>
            <p><strong>Feria de Ciencias 2026</strong> | Conocimiento que transforma, tecnología que impulsa el agro</p>
        </div>
        <div style='text-align: right; font-size: 13px; opacity: 0.9;'>
            <p><strong>Expositora Oficial:</strong></p>
            <p>Mgtr. Virginia Lucciola Mendoza Z.</p>
            <p><em>Docente</em></p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# --- TARJETAS INFORMATIVAS SUPERIORES ---
t1, t2, t3, t4 = st.columns(4)

with t1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🟢 ¿Qué es el Sistema Binario?</div>
        <div class="info-card-desc">Usa solo dos dígitos: 0 y 1. Es el lenguaje nativo e universal con el que operan las computadoras en el mundo.</div>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🔌 ¿Por qué lo usan?</div>
        <div class="info-card-desc">Los transistores electrónicos solo manejan dos estados físicos estables: apagado (0) o encendido (1).</div>
    </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">🔢 Ejemplo rápido</div>
        <div class="info-card-desc">El número decimal <b>42</b> en binario de 8 bits se escribe y representa como: <br><span style="color:#00bc62; font-weight:bold; font-family:monospace;">00101010</span></div>
    </div>
    """, unsafe_allow_html=True)

with t4:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">💡 Aplicaciones</div>
        <div class="info-card-desc">Almacenamiento digital, protocolos de redes, criptografía, Inteligencia Artificial y automatización en Agricultura IoT.</div>
    </div>
    """, unsafe_allow_html=True)


# --- CONFIGURACIÓN DE LA BARRA LATERAL (CONVERSOR) ---
with st.sidebar:
    st.markdown("<h2 style='color:#053f31; text-align:center;'>🔄 CONVERSOR BINARIO</h2>", unsafe_allow_html=True)
    st.write("Ingresa un número entero (ej. 42) o un nombre/palabra (ej. ESPAM) para calcular:")
    
    entrada = st.text_input("Número o Texto:", value="42", placeholder="Ejemplo: 42 o ESPAM")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Explicación breve estática en barra lateral (igual que el prototipo)
    st.markdown("""
    <div style="background:#f9f9f9; padding:15px; border-radius:8px; border:1px solid #e0e0e0; font-size:13px;">
        <b style="color:#053f31;">Tipos de conversión:</b><br><br>
        1️⃣ <b>Decimal ➔ Binario:</b> Convierte números base 10.<br><br>
        2️⃣ <b>Texto ➔ ASCII ➔ Binario:</b> Traduce letras a código numérico y luego a bits.
    </div>
    """, unsafe_allow_html=True)


# --- PROCESAMIENTO LOGÍCO Y TABLERO DE RESULTADOS ---
if entrada:
    # CASO 1: ENTRADA ES UN NÚMERO
    if entrada.isdigit():
        numero = int(entrada)
        # Asegurar representación en 8 bits (o más si el número es mayor a 255)
        num_bits = max(8, numero.bit_length())
        binario = format(numero, f"0{num_bits}b")
        hexa = hex(numero).upper().replace("0X", "#")
        
        # Array de potencias de 2 invertido para los pesos correspondientes
        pesos = [2**i for i in range(len(binario)-1, -1, -1)]

        st.markdown(f"""
        <div class="results-container">
            <div class="results-title-bar">💻 TABLERO BINARIO EN TIEMPO REAL</div>
            <div class="results-body">
        """, unsafe_allow_html=True)
        
        # Columnas de Métrica Superior Interna
        m1, m2, m3 = st.columns([1, 2, 1])
        with m1:
            st.markdown(f"<div style='text-align:center;'><h3>Decimal</h3><h1 style='color:#053f31; font-size:50px;'>{numero}</h1></div>", unsafe_allow_html=True)
        with m2:
            st.markdown(f"<div style='text-align:center;'><h3>Representación Binaria</h3><h1 style='color:#00bc62; font-size:50px; font-family:monospace; letter-spacing:4px;'>{binario}</h1></div>", unsafe_allow_html=True)
        with m3:
            st.markdown(f"<div style='text-align:center;'><h3>Hexadecimal</h3><h1 style='color:#7b2cbf; font-size:50px;'>{hexa}</h1></div>", unsafe_allow_html=True)
        
        # Renderizado de LEDs Dinámicos basados en los bits
        leds_html = "<div class='led-container'>"
        for bit in binario:
            estado = "on" if bit == "1" else "off"
            leds_html += f"""
                <div class='led-box'>
                    <div class='led {estado}'></div>
                    <div class='led-bit'>{bit}</div>
                </div>
            """
        leds_html += "</div>"
        st.markdown(leds_html, unsafe_allow_html=True)
        
        # Explicación matemática interactiva en formato tabla (Estilo el prototipo)
        st.markdown("### 🔢 Desglose y Posición Matemática de los Bits")
        
        # Construir la tabla HTML de potencias y valores activos
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
        
        # Ecuación de la suma de los pesos activos
        componentes_suma = [str(pesos[i]) for i in range(len(binario)) if binario[i] == "1"]
        string_suma = " + ".join(componentes_suma) if componentes_suma else "0"
        
        st.markdown(f"""
        <div style="background: #e8f5e9; border: 1px solid #1b5e20; padding: 15px; border-radius: 8px; text-align: center; margin-top: 15px; font-size: 18px; color: #1b5e20;">
            🧬 <b>Operación:</b> {string_suma} = <b>{numero}</b>
        </div>
        """, unsafe_allow_html=True)
        
        # Métricas de uso de bits abajo del tablero
        st.markdown("<br>", unsafe_allow_html=True)
        activos = binario.count("1")
        apagados = binario.count("0")
        
        s1, s2, s3 = st.columns(3)
        s1.metric("Bits Encendidos (1)", activos)
        s2.metric("Bits Apagados (0)", apagados)
        s3.metric("Eficiencia / Uso de Energía", f"{round((activos/len(binario))*100, 1)} %")

        st.markdown("</div></div>", unsafe_allow_html=True)

    # CASO 2: ENTRADA ES TEXTO (ASCII A BINARIO)
    else:
        st.markdown(f"""
        <div class="results-container">
            <div class="results-title-bar">🔠 TRADUCTOR TEXTO ➔ ASCII ➔ BINARIO</div>
            <div class="results-body">
        """, unsafe_allow_html=True)
        
        # Generar un grid de columnas dinámicas según el número de letras
        letras = [ch for ch in entrada]
        cols = st.columns(len(letras))
        
        for i, ch in enumerate(letras):
            ascii_val = ord(ch)
            bin_val = format(ascii_val, "08b")
            
            # Crear los minileds para cada letra individual
            minileds = "".join([f"<div class='miniled {'on' if b=='1' else 'off'}'></div>" for b in bin_val])
            
            with cols[i]:
                st.markdown(f"""
                <div class="ascii-card">
                    <div class="ascii-char">{ch}</div>
                    <div class="ascii-meta">
                        <b>ASCII:</b> {ascii_val}<br>
                        <span style="font-family:monospace; font-weight:bold; color:#00bc62;">{bin_val}</span>
                    </div>
                    <div class="miniled-container">{minileds}</div>
                </div>
                """, unsafe_allow_html=True)
                
        st.markdown("</div></div>", unsafe_allow_html=True)


# --- SECCIÓN INFERIOR: APLICACIONES REALES (ESTILO GRID MODERNO) ---
st.markdown("<br><h3 style='color:#053f31;'>🌍 Aplicaciones del Sistema Binario en el Mundo Real</h3>", unsafe_allow_html=True)

a1, a2, a3, a4, a5 = st.columns(5)
apps = [
    ("💾 Almacenamiento", "Fotos, videos y documentos se guardan como miles de millones de ceros y unos en discos duros."),
    ("🌐 Redes e Internet", "Los datos viajan por cables de cobre o fibra óptica como pulsos eléctricos o haces de luz (1) y oscuridad (0)."),
    ("🔒 Criptografía", "La seguridad informática y encriptación de contraseñas depende de operaciones lógicas binarias (XOR)."),
    ("🤖 Inteligencia Artificial", "Los modelos de IA procesan matrices masivas de datos que en su nivel más bajo son operaciones binarias."),
    ("🚜 Agricultura IoT", "Sensores en campo miden humedad o temperatura y envían datos binarios a la nube para optimizar el agro.")
]

for col, (title, desc) in zip([a1, a2, a3, a4, a5], apps):
    with col:
        st.markdown(f"""
        <div style="background: white; padding: 15px; border-radius: 10px; border-top: 4px solid #00bc62; box-shadow: 0 4px 6px rgba(0,0,0,0.03); height: 100%;">
            <b style="color:#053f31; font-size:14px;">{title}</b><br>
            <p style="font-size:12px; color:#555; margin-top:8px; line-height:1.4;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)


# --- PIE DE PÁGINA (FOOTER) ---
st.markdown("""
<div class="footer-bar">
    ESPAM MFL | Feria de Ciencias de Ingeniería 2026 — Calceta, Manabí, Ecuador
</div>
""", unsafe_allow_html=True)