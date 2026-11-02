from pymupdf import open
from pathlib import Path
import re
from typing import List



def extract_paragraphs(pdf_path:str|Path) -> List[str]:
    """
    Extracts paragraphs from a PDF file.

    Args:
        pdf_path (str|Path): The path to the PDF file.
        
    Returns:
       List[str]: A list
       of paragraphs extracted from the PDF file.
    """
    doc = open(pdf_path)
    paragraphs = []
    
    for page in doc:
        # Extract text blocks from the page
        blocks = page.get_text("blocks")
        blocks = sorted(blocks, key=lambda b: (b[1], b[0]))  # Sort by vertical position, then horizontal position
        
        for block in blocks:
            text = block[4]
            
            # Replace line breaks inside a paragraph with spaces
            text = re.sub(r"\r+", " ", text).strip()
            
            if text:
                paragraphs.append(text)
                
    return paragraphs
