import streamlit as st
import pandas as pd
from utils.smile_image import smiles_to_image

# Set page configuration
st.set_page_config(layout="wide")


def main():
    st.title("Streamlit Dashboard")

    # Upload CSV file in the sidebar
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Check if 'molecule_chembl_id' column exists
        if 'molecule_chembl_id' in df.columns:
            # Create a list with 'all' and 'none' options
            molecule_options = ['all', 'none'] + df['molecule_chembl_id'].unique().tolist()

            # Dropdown menu for selecting molecule in the sidebar
            selected_molecule = st.sidebar.selectbox("Select a molecule", molecule_options)

            if selected_molecule == 'all':
                st.write("All molecules selected.")
                # Add logic to handle 'all' option if needed
            elif selected_molecule == 'none':
                st.write("No molecule selected.")
                # Add logic to handle 'none' option if needed
            else:
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