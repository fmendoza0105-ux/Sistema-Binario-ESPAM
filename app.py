import streamlit as st
import base64

st.set_page_config(
    page_title="Sistema Binario ESPAM",
    page_icon="💻",
    layout="wide"
)

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo = get_base64("logo-espam.png")

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.header{
    background:linear-gradient(90deg,#012d22,#014737,#01664d);
    border-radius:25px;
    padding:20px;
    color:white;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 2px 10px rgba(0,0,0,.1);
}

.led{
    width:60px;
    height:60px;
    border-radius:50%;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    margin:5px;
    color:white;
    font-weight:bold;
    font-size:20px;
}

.on{
    background:#00d63b;
    box-shadow:0 0 20px #00ff66;
}

.off{
    background:#333;
}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="header">

<div style="display:flex;align-items:center;">

<div style="width:25%;">
<img src="data:image/png;base64,{logo}" width="250">
</div>

<div style="width:75%;text-align:center;">

<h1>SISTEMA BINARIO</h1>

<h2>Escuela Superior Politécnica Agropecuaria de Manabí</h2>

<h3>Manuel Félix López</h3>

<h3>Feria de Ciencias 2026</h3>

</div>

</div>

</div>
""", unsafe_allow_html=True)

st.write("")

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='card'>
    <h3>¿Qué es?</h3>
    Sistema de numeración que usa únicamente 0 y 1.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
    <h3>¿Por qué lo usan?</h3>
    Los transistores tienen dos estados:
    apagado y encendido.
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
    <h3>Aplicaciones</h3>
    IA, Redes, IoT, Criptografía y almacenamiento.
    </div>
    """, unsafe_allow_html=True)

st.write("")

entrada = st.text_input(
    "Ingrese un número o nombre"
)

if st.button("CONVERTIR"):

    if entrada.isdigit():

        numero = int(entrada)

        binario = format(numero,'08b')

        st.subheader("Conversión Decimal → Binario")

        st.write(f"Decimal: {numero}")
        st.write(f"Binario: {binario}")

        leds=""

        for bit in binario:

            if bit=="1":
                leds += "<div class='led on'>1</div>"
            else:
                leds += "<div class='led off led'>0</div>"

        st.markdown(
            leds,
            unsafe_allow_html=True
        )

        pesos=[128,64,32,16,8,4,2,1]

        tabla={}

        for p,b in zip(pesos,binario):
            tabla[str(p)] = [b]

        st.table(tabla)

        suma=[]

        for p,b in zip(pesos,binario):
            if b=="1":
                suma.append(str(p))

        st.success(
            f"{' + '.join(suma)} = {numero}"
        )

    else:

        st.subheader(
            "Texto ASCII → Binario"
        )

        cols = st.columns(len(entrada))

        for i, letra in enumerate(
            entrada.upper()
        ):

            ascii_num=ord(letra)

            binario=format(
                ascii_num,
                "08b"
            )

            with cols[i]:

                st.markdown(f"""
                <div class='card'>

                <h2>{letra}</h2>

                ASCII: {ascii_num}

                <br><br>

                {binario}

                </div>
                """,
                unsafe_allow_html=True)

st.write("")

st.subheader("Aplicaciones Reales")

col1,col2,col3,col4,col5 = st.columns(5)

col1.success("💾 Almacenamiento")
col2.info("🌐 Redes")
col3.warning("🔒 Criptografía")
col4.success("🤖 IA")
col5.info("🚜 Agricultura IoT")
