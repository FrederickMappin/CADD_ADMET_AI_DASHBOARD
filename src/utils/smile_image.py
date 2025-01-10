from rdkit import Chem
from rdkit.Chem import Draw

def smiles_to_image(smiles: str):
    """
    Convert a SMILES string to an image of the chemical structure.

    Parameters:
    smiles (str): The SMILES string of the chemical.

    Returns:
    PIL.Image: The image of the chemical structure.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError("Invalid SMILES string")
    img = Draw.MolToImage(mol)
    return img

