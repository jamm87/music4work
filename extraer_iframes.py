import pandas as pd
import requests
from bs4 import BeautifulSoup

INPUT_CSV = 'M4W-DB 14696bd5b87780dea054ecafa6118cf2.csv'
OUTPUT_CSV = 'con_iframes.csv'
URL_COLUMN = 'url'  # Cambia esto si tu columna se llama distinto

df = pd.read_csv(INPUT_CSV)
iframe_list = []

for url in df[URL_COLUMN]:
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        iframe = soup.find('iframe')
        iframe_list.append(str(iframe) if iframe else '')
    except Exception:
        iframe_list.append('')

df['iframe_html'] = iframe_list
df.to_csv(OUTPUT_CSV, index=False)
print(f"Hecho: {OUTPUT_CSV}")
