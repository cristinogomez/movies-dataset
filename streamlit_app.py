import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Gestión Agendas Cot",layout="wide")
st.title("Agendas COT")

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/bloqueos.csv")
    return df
df = load_data()

col1, col2, col3 = st.columns(3)
with col1:
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
    # Filter the dataframe based on the widget input and reshape it.
    #df_filtered = df[(df["Medico"].isin(medico))]
    
    # Display the data as a table using `st.dataframe`.
    st.dataframe(
        df,
        use_container_width=True,
    )
