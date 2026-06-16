
import streamlit as st
import base64

st.set_page_config(page_title="Sistema Binario ESPAM", page_icon="💻", layout="wide")

def get_base64(file):
    try:
        with open(file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

logo = get_base64("logo-espam.png")

st.markdown("""
<style>
.logo-box{
background:white;
padding:20px;
border-radius:20px;
display:inline-block;

box-shadow:
0 0 15px rgba(255,255,255,.8),
0 0 30px rgba(255,255,255,.6);

border:4px solid white;
}

.stApp{
background:linear-gradient(135deg,#081c15,#1b4332,#2d6a4f);
}
.header{
background:rgba(0,0,0,.25);
padding:20px;border-radius:20px;color:white;
border:1px solid #00ff88;
}
.card{
background:white;padding:15px;border-radius:15px;
}
.led{
width:55px;height:55px;border-radius:50%;
display:inline-flex;align-items:center;justify-content:center;
margin:4px;color:white;font-weight:bold;
}
.on{
background:#00ff66;
box-shadow:0 0 10px #00ff66,0 0 25px #00ff66;
}
.off{background:#333;}
</style>
""", unsafe_allow_html=True)

logo_html = f"""
<div class='logo-box'>
<img src="data:image/png;base64,{logo}" width="230">
</div>
""" if logo else ""

st.markdown(f"""
<div class='header'>
<div style='display:flex;align-items:center;justify-content:space-between'>
<div style="width:30%; text-align:center;"> {logo_html} </div>
<div style='width:70%;text-align:center;color:white'>
<h1>SISTEMA BINARIO</h1>
<h3>Escuela Superior Politécnica Agropecuaria de Manabí</h3>
<h3>Manuel Félix López - Feria de Ciencias 2026</h3>
<h4>👩‍🏫 Expositora Oficial Mgtr. Virginia Lucciola Mendoza Zambrano - Docente </h4>
</div>
<div></div>
</div>
</div>
""", unsafe_allow_html=True)

def pasos_binario(n):
    p=[]
    while n>0:
        p.append([n,n//2,n%2])
        n//=2
    return p

with st.sidebar:
    st.title("🔢 Conversor")
    entrada = st.text_input("Número o nombre")
    convertir = st.button("🚀 Convertir", use_container_width=True)

if convertir and entrada:
    if entrada.isdigit():
        numero=int(entrada)
        binario=format(numero,"08b")
        hexa=hex(numero).upper()

        c1,c2,c3=st.columns(3)
        c1.metric("Decimal",numero)
        c2.metric("Binario",binario)
        c3.metric("Hexadecimal",hexa)

        leds="".join([f"<div class='led {'on' if b=='1' else 'off'}'>{b}</div>" for b in binario])
        st.markdown(leds, unsafe_allow_html=True)

        st.subheader("Conversión paso a paso")
        st.table(pasos_binario(numero))

        pesos=[128,64,32,16,8,4,2,1]
        st.table({str(p):[b] for p,b in zip(pesos,binario)})
        activos = binario.count("1")
        apagados = binario.count("0")
        s1,s2,s3 = st.columns(3)
        s1.metric("Bits Activos", activos)
        s2.metric("Bits Apagados", apagados)
        s3.metric("Uso %", round((activos/8)*100,1))
    else:
        st.subheader("ASCII → Binario")
        cols=st.columns(max(1,len(entrada)))
        for i,ch in enumerate(entrada.upper()):
            with cols[i]:
                st.markdown(f"<div class='card'><h2>{ch}</h2>{ord(ch)}<br>{format(ord(ch),'08b')}</div>", unsafe_allow_html=True)

st.subheader("🌎 Aplicaciones Reales")
c1,c2,c3,c4,c5=st.columns(5)
for col,title in zip([c1,c2,c3,c4,c5],
["💾 Almacenamiento","🌐 Redes","🔒 Criptografía","🤖 IA","🚜 Agricultura IoT"]):
    col.markdown(f"<div class='card'><b>{title}</b></div>", unsafe_allow_html=True)
