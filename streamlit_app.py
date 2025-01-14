import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Gestión Agendas Cot",layout="wide")
st.subheader("Agendas COT")

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/bloqueos.csv")
    return df
df = load_data()


col1, col2, col3 = st.columns(3)
with col1:
    container = st.container(border=True)
    with container:
        medicos = st.multiselect(
            "Médicos",
            ["Fernandez", "Aguilella", "Revert"]
        )
        st.write("You selected:", medicos)

with col2:
    medico = st.selectbox(
    "Médicos",
    ("Aguilella", "Fernandez", "Villar"),
)

    st.write("Tu selección:", medico)

with col3:
    with st.form("my_form"):
        edited_df = st.data_editor(df, num_rows="dynamic",use_container_width=True)
        boton_guardar=st.form_submit_button('Save')
        if boton_guardar:
              df.to_csv('data/bloqueos.csv',index=False)

