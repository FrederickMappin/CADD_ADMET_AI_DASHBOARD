import streamlit as st
import pandas as pd
from utils.smile_image import smiles_to_image

def main():
    st.title("Streamlit Dashboard")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Check if 'molecule_chembl_id' column exists
        if 'molecule_chembl_id' in df.columns:
            # Dropdown menu for selecting molecule
            selected_molecule = st.selectbox("Select a molecule", df['molecule_chembl_id'])
            
            # Get the SMILES string for the selected molecule
            smiles = df[df['molecule_chembl_id'] == selected_molecule]['smiles'].values[0]
            
            # Call the function to get the image
            try:
                img = smiles_to_image(smiles)
                # Display the image
                st.image(img, caption=f"Chemical Structure of {selected_molecule}")
            except ValueError as e:
                st.error(f"Error: {e}")
        else:
            st.error("The uploaded CSV file does not contain 'molecule_chembl_id' column.")
    else:
        st.info("Please upload a CSV file.")

if __name__ == "__main__":
    main()