import streamlit as st
import base64
import random

# Configuración de página (Ancho completo)
st.set_page_config(page_title="Sistema Binario ESPAM", page_icon="💻", layout="wide")

# --- CONTROL DE ESTADOS DE SESIÓN (ESTABLECE EL FLUJO DE JUEGO) ---
if "juego_binario" not in st.session_state:
    st.session_state.juego_binario = format(random.randint(1, 100), "08b")
if "puntos" not in st.session_state:
    st.session_state.puntos = 0
if "estado_juego" not in st.session_state:
    st.session_state.estado_juego = "pendiente"  # Estados posibles: pendiente, correcto, incorrecto

# Función para cambiar de ejercicio
def siguiente_ejercicio():
    st.session_state.juego_binario = format(random.randint(1, 100), "08b")
    st.session_state.estado_juego = "pendiente"
    # Limpiamos el texto ingresado reseteando la llave del input mediante rerun si es necesario
    
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

# --- BARRA LATERAL
