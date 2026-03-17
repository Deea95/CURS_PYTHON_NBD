import pdfplumber
import os
import re

pdf_path = r"C:\Users\AndreeaIote\Desktop\CURS_PYTHON_NBD\SUPORT-CURS\curs_python.pdf"
output_folder = r"C:\Users\AndreeaIote\Desktop\CURS_PYTHON_NBD\SUPORT-CURS\toate_exemplele"
os.makedirs(output_folder, exist_ok=True)


def is_python_code(line):
    """Verifică dacă linia pare a fi cod sau text explicativ."""
    l = line.strip()
    if not l: return False

    # Eliminăm headerele de pagină și titlurile de capitol
    if any(x in l for x in ["Paul A. Gagniuc", "Complex Examples", "Synthesis Lectures", "© The Author"]):
        return False
    if re.match(r'^\d+$', l): return False  # Numere de pagină

    # Cuvinte cheie care indică text explicativ (nu cod)
    stop_words = ["The above code", "The point of", "This example", "Specifically", "Note that", "Overall"]
    if any(l.startswith(word) for word in stop_words):
        return False

    # Un rând de cod are de obicei operatori sau structuri Python
    code_indicators = ["=", "def ", "if ", "else:", "return", "print(", "append", "[", "]", "for ", "while "]
    if any(ind in l for ind in code_indicators):
        return True

    # Dacă e un comentariu Python
    if l.startswith("#"):
        return True

    return False


with pdfplumber.open(pdf_path) as pdf:
    ex_dict = {}
    current_ex = None

    print("Extragere fină a codului...")
    for page in pdf.pages:
        text = page.extract_text(layout=True, x_tolerance=3)
        if not text: continue

        for line in text.split('\n'):
            match = re.search(r"Ex\.?\s*\((\d+)\)", line, re.IGNORECASE)
            if match:
                current_ex = int(match.group(1))
                ex_dict[current_ex] = []
                # Păstrăm titlul ca comentariu
                ex_dict[current_ex].append(f"# {line.strip()}")
                continue

            if current_ex:
                # Filtrăm: dacă e cod îl punem, dacă e text lung ne oprim
                if is_python_code(line):
                    # Curățăm caracterele speciale de editură
                    line = line.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'").replace('–',
                                                                                                                '-')
                    ex_dict[current_ex].append(line)
                elif len(line.split()) > 10:  # Dacă e o propoziție lungă fără semne de cod, probabil e finalul
                    current_ex = None

# Salvare
for num, lines in ex_dict.items():
    if len(lines) > 1:  # Doar dacă am găsit mai mult de titlu
        content = "\n".join(lines)
        with open(os.path.join(output_folder, f"ex_{str(num).zfill(3)}.py"), "w", encoding="utf-8") as f:
            f.write(content)

print("Gata! Verifică acum fișierele.")