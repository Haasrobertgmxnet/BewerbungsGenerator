
## Read csv data
import pandas as pd

def merge_pdfs(pdf_paths, output_path):
    from pypdf import PdfReader, PdfWriter
    writer = PdfWriter()

    for path in pdf_paths:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f_out:
        writer.write(f_out)




csv_path = '../../Schulen.csv'
df = pd.read_csv(csv_path, sep=';')
# print(df)
print(df.head())

## read LaTeX template
tex_file = '../../../Template/ACV.tex'
with open(tex_file, 'r', encoding='utf-8') as f:
    text = f.read()  # <--- liest die ganze Datei als einen String


import subprocess
import re
import smtplib
from email.message import EmailMessage
from pathlib import Path
smtp_server = "mail.gmx.net"
smtp_port = 587
sender_email = "****" # your email
sender_pass = "****" # your password
empf_email = sender_email

for line in df.iterrows():
    data = line[1]
    ident = data.iloc[0]
    name = data.iloc[1]
    street = data.iloc[2]
    zipcode = str(data.iloc[3])
    city = data.iloc[4]
    email = data.iloc[5]

    new_content = name + '\\\\\\\r' + street + '\\\\\\\r' + str(zipcode) + ' ' + city
    pattern = r"%%% Adressat 1 Begin(.*?)%%% Adressat 1 End"
    ersetzt = f"%%% Adressat 1 Begin\n{new_content}\n%%% Adressat 1 End"
    text = re.sub(pattern, ersetzt, text, flags=re.DOTALL)

    pattern = r"%%% Adressat 2 Begin(.*?)%%% Adressat 2 End"
    ersetzt = f"%%% Adressat 2 Begin\n{name}\n%%% Adressat 2 End"
    text = re.sub(pattern, ersetzt, text, flags=re.DOTALL)

    new_tex_path = ident + ".tex"
    with open(new_tex_path, "w", encoding="utf-8") as f:
        f.write(text)

    result = subprocess.run(
    ["pdflatex", "-interaction=nonstopmode", new_tex_path],
    capture_output=True,
    text=True)

    pdf_doc1 = ident + ".pdf"
    pdf_doc2 = "Zeugnisse.pdf"

    merge_pdfs([pdf_doc1, pdf_doc2], pdf_doc1)

    gs_path = r"C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe"

    ofile = 'Bewerbung ' + city + '.pdf'
    subprocess.run([
        r"C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",  # alternativ: /screen, /default, /prepress
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={ofile}",
        pdf_doc1
    ])

    pdf_path = Path(ofile)
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Cc"] = sender_email
    msg["Subject"] = "Bewerbung als Lehrkraft für MINT-Fächer"
    msg_text = (
    "Sehr geehrte Damen und Herren der Schulleitung,\n\n"
    "mit großem Interesse bewerbe ich mich als Lehrkraft an Ihrer Schule.\n"
    "Im Anhang finden Sie meine vollständigen Bewerbungsunterlagen.\n\n"
    "Für Rückfragen stehe ich Ihnen jederzeit gerne zur Verfügung.\n\n"
    "Ich freue mich sehr über die Gelegenheit, mich persönlich bei Ihnen vorzustellen.\n\n"
    "Mit freundlichen Grüßen\n"
    "Robert Haas\n\n"
    "Telefon: +49 176 8018 1926\n"
)
    msg.set_content(msg_text, charset="utf-8")


    # PDF-Datei anhängen
    pdf_bytes = pdf_path.read_bytes()
    msg.add_attachment(pdf_bytes, maintype="application", subtype="pdf", filename=pdf_path.name)

    # E-Mail senden
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()  # TLS-Verschlüsselung
        smtp.login(sender_email, sender_pass)
        smtp.send_message(msg)

    print("E-Mail wurde gesendet.")

