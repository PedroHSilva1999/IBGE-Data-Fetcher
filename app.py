import streamlit as st
import pandas as pd
import requests

def get_data(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    except Exception as e:
        print(f"HTTP Error: {e}")
        return []

def get_name_data(name):
    if not name: 
        return {}
        
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    params = {"groupBy":"UF"}
    data = get_data(url, params)
    
    if not data:  
        return {}
        
    return {name["localidade"]: name["res"][0]["populacao"] for name in data}


def get_state_data():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/"

    data = get_data(url, params={"view":"nivelado"})
    
    if not data:  
        return {}
   
    return {str(state["UF-id"]): state["UF-nome"] for state in data}


def consolidate_data(data_name, data_state):
    if not data_name:  
        return pd.DataFrame(columns=["State", "Population"])
        
    result_data = []
    for id_state, population in sorted(data_name.items(), key=lambda x:x[1], reverse=True):
        state_name = data_state.get(id_state, 'N/A')
        result_data.append({"State": state_name, "Population": population})
    print(pd.DataFrame(result_data))
    return pd.DataFrame(result_data)


def main():
    st.title("IBGE Data Fetcher")
    st.header("Data and Population by name for Brazilian States")

    name = st.text_input("Enter a name:")
    
    if st.button("Search"):
        if name:
            name_data = get_name_data(name)
            state_data = get_state_data()
            
            if name_data and state_data:
                df = consolidate_data(name_data, state_data)
                
                col1, col2 = st.columns([0.7, 0.3])
                
                with col1:
                    st.dataframe(df, hide_index=True)
                
                with col2:
                    total = sum(name_data.values()) if name_data else 0
                    st.metric(f"Total occurrences of {name}", total)
            else:
                st.warning("No data found for this name.")
        else:
            st.warning("Please enter a name to search.")

if __name__ == "__main__":
    main()