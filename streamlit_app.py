import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Gestión Agendas Cot")
st.title("Agendas COT")

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/bloqueos.csv")
    return df
df = load_data()

# Show a multiselect widget with the genres using `st.multiselect`.
#medicos = st.multiselect(
   # "Medico",
   # df.Medico.unique(),
    #["Fernandez", "Aguilella"],)

# Filter the dataframe based on the widget input and reshape it.
#df_filtered = df[(df["Medico"].isin(medico))]

# Display the data as a table using `st.dataframe`.
st.dataframe(
    df,
    use_container_width=True,
)
