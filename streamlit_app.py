import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Gestión Agendas Angiologia y Cirugia Vascular",layout="wide")
st.subheader("Bloqueos ACV")

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data()
def load_data():
    df = pd.read_csv("data/ACV.csv",encoding='utf-8')
    return df
df = load_data()


col1, col2 = st.columns(2)
with col1:
    container = st.container(border=True)
    with container:
        medicos = st.multiselect(
            "Médicos",
            ["Fernandez", "Aguilella", "Revert"]
        )
        st.write("You selected:", medicos)

with col2:
    with st.form("my_form"):
            edited_df = st.data_editor(df, num_rows='dynamic',use_container_width=True,hide_index=True)
            boton_guardar=st.form_submit_button('Save')
            if boton_guardar:
                with open('data/ACV.csv', mode='w') as file :
                    df1 = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                                        'mask': ['red', 'purple'],
                                        weapon': ['sai', 'bo staff']})
                    df1.to_csv('out.csv', index=False)  
                    st.write("Edited dataframe:", edited_df)
                    edited_df.to_csv(file, index=False)
                

