import pdfplumber
import re
import os

pdf_path = r"C:\Users\AndreeaIote\Desktop\CURS_PYTHON_NBD\SUPORT-CURS\curs_python.pdf"
output_folder = r"C:\Users\AndreeaIote\Desktop\CURS_PYTHON_NBD\SUPORT-CURS\examples"

os.makedirs(output_folder, exist_ok=True)

current_example = None
code_lines = []
indent = 0

def format_line(line):
    global indent

    stripped = line.strip()

    # scădem indentarea pentru else/elif
    if stripped.startswith(("else", "elif", "except", "finally")):
        indent -= 1

    formatted = "    " * indent + stripped

    # creștem indentarea după :
    if stripped.endswith(":"):
        indent += 1

    return formatted


with pdfplumber.open(pdf_path) as pdf:

    for page in pdf.pages:

        width = page.width
        height = page.height

        # extragem doar partea stângă (codul)
        left = page.crop((0, 0, width/2, height))

        text = left.extract_text()
        if not text:
            continue

        lines = text.split("\n")

        for line in lines:

            match = re.search(r"Ex\.\s*\((\d+)\)", line)

            if match:
                if current_example and code_lines:
                    filename = os.path.join(output_folder, f"example_{current_example}.py")
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write("\n".join(code_lines))

                current_example = match.group(1)
                code_lines = []
                indent = 0
                continue

            line = line.strip()

            if re.match(r"^(#|for |while |if |elif |else|def |class |print|\w+\s*=)", line):
                code_lines.append(format_line(line))


# salvare ultim exemplu
if current_example and code_lines:
    filename = os.path.join(output_folder, f"example_{current_example}.py")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(code_lines))

print("Exemplele au fost extrase cu indentare.")