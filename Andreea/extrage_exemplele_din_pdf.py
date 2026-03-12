import pdfplumber
import os
import re

pdf_path = r"C:\Users\AndreeaIote\Desktop\CURS_PYTHON_NBD\SUPORT-CURS\curs_python.pdf"
output_folder = r"C:\Users\AndreeaIote\Desktop\CURS_PYTHON_NBD\SUPORT-CURS\examples"

os.makedirs(output_folder, exist_ok=True)


def is_actually_code(line):
    """
    Filtru drastic: o linie de cod trebuie să aibă simboluri specifice
    sau să fie foarte scurtă. Dacă e o frază lungă, e text explicativ.
    """
    l = line.strip()
    if not l: return False

    # Cuvinte cheie care „garantează” că e cod
    code_indicators = ['=', 'for ', 'if ', 'print', '+=', 'len(', 'range', 'else:', 'elif']
    if any(ind in l for ind in code_indicators):
        # Dacă are indicatori, dar are și prea multe cuvinte (peste 10), e probabil o explicație
        if len(l.split()) > 10 and "=" not in l[:10]:
            return False
        return True

    # Liniile care conțin doar caractere de desenat sau paranteze
    if any(c in l for c in "▮▯[]()"):
        return True

    return False


def save_example(number, lines):
    if not lines: return
    # Curățăm liniile parazite care s-ar fi putut strecura la final
    final_code = []
    for line in lines:
        if is_actually_code(line):
            final_code.append(line)
        else:
            # Dacă am dat de un bloc mare de text, ne oprim pentru acest exemplu
            if len(line.split()) > 8:
                break

    if final_code:
        filename = os.path.join(output_folder, f"example_{number}.py")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(final_code))


with pdfplumber.open(pdf_path) as pdf:
    current_example = None
    code_lines = []

    for page in pdf.pages:
        # Lăsăm lățimea la 50%, dar filtrăm conținutul rând cu rând
        width = page.width
        height = page.height
        left_area = page.crop((0, 0, width * 0.5, height))

        text = left_area.extract_text(layout=True)
        if not text: continue

        for line in text.split("\n"):
            # Detectăm Ex. (n)
            match = re.search(r"Ex\.\s*\((\d+)\)", line)

            if match:
                if current_example:
                    save_example(current_example, code_lines)
                current_example = match.group(1)
                code_lines = []
                continue

            if current_example:
                # Sărim peste meta-datele Springer (header/footer)
                if any(x in line for x in ["Paul A. Gagniuc", "©", "http", "Page"]):
                    continue

                # Adăugăm linia dacă trece de filtrul de cod
                if is_actually_code(line):
                    code_lines.append(line.rstrip())
                else:
                    # Dacă am dat de text explicativ lung, ignorăm restul de pe pagină
                    if len(line.strip().split()) > 10:
                        continue

    if current_example:
        save_example(current_example, code_lines)

print("Gata! Acum codul extras este curat și complet.")