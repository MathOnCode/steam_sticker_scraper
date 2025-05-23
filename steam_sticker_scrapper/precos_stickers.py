import os

import requests
import json
from datetime import datetime

from dotenv import load_dotenv
from fpdf import FPDF
import time
import mensageiro as m

load_dotenv()

# CONFIGURAÇÃO
STICKERS = [
    "Sticker | 910 (Glitter) | Copenhagen 2024",
    "Sticker | Aleksib (Glitter) | Copenhagen 2024",
    "Sticker | ANNIHILATION (Glitter) | Paris 2023",
    "Sticker | apEX (Glitter) | Copenhagen 2024",
    "Sticker | arT | Copenhagen 2024",
    "Sticker | arT (Glitter) | Copenhagen 2024",
    "Sticker | bLitz (Glitter) | Copenhagen 2024",
    "Sticker | Brollan (Glitter) | Copenhagen 2024",
    "Sticker | coldzera (Glitter) | Copenhagen 2024",
    "Sticker | coldzera (Holo) | Copenhagen 2024",
    "Sticker | Complexity Gaming (Glitter) | Copenhagen 2024",
    "Sticker | dav1d (Glitter) | Antwerp 2022",
    "Sticker | decenty (Glitter) | Copenhagen 2024",
    "Sticker | decenty (Gold) | Copenhagen 2024",
    "Sticker | decenty (Holo) | Copenhagen 2024",
    "Sticker | device | Stockholm 2021",
    "Sticker | degster (Glitter) | Antwerp 2022",
    "Sticker | degster (Glitter) | Shanghai 2024",
    "Sticker | donk | Copenhagen 2024",
    "Sticker | donk (Glitter) | Copenhagen 2024",
    "Sticker | donk (Glitter) | Shanghai 2024",
    "Sticker | donk (Glitter) | Champions Shanghai 2024",
    "Sticker | donk (Holo) | Champions Shanghai 2024",
    "Sticker | drop (Glitter) | Rio 2022",
    "Sticker | dumau (Glitter) | Copenhagen 2024",
    "Sticker | dumau (Glitter) | Rio 2022",
    "Sticker | EliGE (Glitter) | Copenhagen 2024",
    "Sticker | ENCE (Glitter) | Copenhagen 2024",
    "Sticker | FalleN | Antwerp 2022",
    "Sticker | FalleN | Copenhagen 2024",
    "Sticker | FalleN | Shanghai 2024",
    "Sticker | FalleN (Glitter) | Copenhagen 2024",
    "Sticker | Fame (Glitter) | Copenhagen 2024",
    "Sticker | FL1T (Glitter) | Copenhagen 2024",
    "Sticker | FL1T (Glitter) | Rio 2022",
    "Sticker | FlameZ (Glitter) | Copenhagen 2024",
    "Sticker | FlameZ (Glitter) | Rio 2022",
    "Sticker | forZe eSports (Glitter) | Antwerp 2022",
    "Sticker | frozen (Glitter) | Copenhagen 2024",
    "Sticker | FURIA (Glitter) | Antwerp 2022",
    "Sticker | FURIA (Glitter) | Rio 2022",
    "Sticker | gla1ve (Glitter) | Copenhagen 2024",
    "Sticker | Goofy (Glitter) | Copenhagen 2024",
    "Sticker | Goofy (Holo) | Paris 2023",
    "Sticker | Grim (Glitter) | Copenhagen 2024",
    "Sticker | hallzerk (Glitter) | Copenhagen 2024",
    "Sticker | Heroic (Glitter) | Copenhagen 2024",
    "Sticker | huNter- (Glitter) | Copenhagen 2024",
    "Sticker | huNter- (Glitter) | Paris 2023",
    "Sticker | ICY (Glitter) | Copenhagen 2024",
    "Sticker | insani (Glitter) | Shanghai 2024",
    "Sticker | Jame (Glitter) | Champions Rio 2022",
    "Sticker | Jimpphat (Glitter) | Copenhagen 2024",
    "Sticker | Jimpphat (Holo) | Copenhagen 2024",
    "Sticker | jambo (Glitter) | Shanghai 2024",
    "Sticker | jL (Glitter) | Champions Copenhagen 2024",
    "Sticker | karrigan (Glitter) | Copenhagen 2024",
    "Sticker | KSCERATO (Glitter) | Antwerp 2022",
    "Sticker | KSCERATO (Glitter) | Copenhagen 2024",
    "Sticker | KSCERATO (Glitter) | Paris 2023",
    "Sticker | KSCERATO (Glitter) | Rio 2022",
    "Sticker | Kylar (Glitter) | Copenhagen 2024",
    "Sticker | Legacy (Glitter) | Copenhagen 2024",
    "Sticker | latto (Glitter) | Copenhagen 2024",
    "Sticker | magixx (Glitter) | Antwerp 2022",
    "Sticker | magixx (Glitter) | Copenhagen 2024",
    "Sticker | magixx (Holo) | Champions Shanghai 2024",
    "Sticker | m0NESY | Copenhagen 2024",
    "Sticker | m0NESY | Paris 2023",
    "Sticker | m0NESY (Glitter) | Copenhagen 2024",
    "Sticker | m0NESY (Holo) | Copenhagen 2024",
    "Sticker | mzinho (Glitter) | Copenhagen 2024",
    "Sticker | mzinho (Holo) | Copenhagen 2024",
    "Sticker | nexa (Glitter) | Rio 2022",
    "Sticker | NiKo | Antwerp 2022",
    "Sticker | NiKo | Copenhagen 2024",
    "Sticker | niko (Glitter) | Paris 2023",
    "Sticker | Natus Vincere (Holo) | Copenhagen 2024",
    "Sticker | NQZ (Glitter) | Copenhagen 2024",
    "Sticker | NQZ (Glitter) | Rio 2022",
    "Sticker | NQZ (Gold) | Copenhagen 2024",
    "Sticker | noway (Glitter) | Copenhagen 2024",
    "Sticker | noway (Holo) | Copenhagen 2024",
    "Sticker | n0rb3r7 (Glitter) | Copenhagen 2024",
    "Sticker | Outsiders (Glitter) | Rio 2022",
    "Sticker | Outsiders (Holo) | Rio 2022",
    "Sticker | paiN Gaming (Glitter) | Copenhagen 2024",
    "Sticker | paiN Gaming (Glitter) | Paris 2023",
    "Sticker | Renegades (Glitter) | Antwerp 2022",
    "Sticker | ropz (Glitter) | Rio 2022",
    "Sticker | ropz (Glitter) | Paris 2023",
    "Sticker | salazar (Glitter) | Copenhagen 2024",
    "Sticker | salazar (Holo) | Copenhagen 2024",
    "Sticker | s1mple | Antwerp 2022",
    "Sticker | s1mple | Paris 2023",
    "Sticker | s1mple | Stockholm 2021",
    "Sticker | s1mple (Glitter) | Paris 2023",
    "Sticker | s1mple (Holo) | Stockholm 2021",
    "Sticker | sh1ro (Glitter) | Copenhagen 2024",
    "Sticker | sh1ro (Glitter) | Shanghai 2024",
    "Sticker | sh1ro (Holo) | Champions Shanghai 2024",
    "Sticker | sh1ro (Holo) | Champions Shanghai 2024",
    "Sticker | sh1ro (Holo) | Copenhagen 2024",
    "Sticker | skullz (Glitter) | Shanghai 2024",
    "Sticker | skullz (Holo) | Paris 2023",
    "Sticker | Senzu (Glitter) | Copenhagen 2024",
    "Sticker | Senzu (Holo) | Copenhagen 2024",
    "Sticker | Senzu | Shanghai 2024",
    "Sticker | snow | Shanghai 2024",
    "Sticker | Spinx (Holo) | Copenhagen 2024",
    "Sticker | Starry (Glitter) | Copenhagen 2024",
    "Sticker | StavN (Glitter) | Antwerp 2022",
    "Sticker | StavN (Glitter) | Paris 2023",
    "Sticker | StavN (Glitter) | Rio 2022",
    "Sticker | Techno4K (Glitter) | Copenhagen 2024",
    "Sticker | Techno4K (Glitter) | Paris 2023",
    "Sticker | Techno4K (Holo) | Copenhagen 2024",
    "Sticker | TeSeS (Glitter) | Rio 2022",
    "Sticker | The MongolZ (Glitter) | Copenhagen 2024",
    "Sticker | The MongolZ (Holo) | Copenhagen 2024",
    "Sticker | torzsi (Glitter) | Copenhagen 2024",
    "Sticker | torzsi (Holo) | Copenhagen 2024",
    "Sticker | torzsi (Glitter) | Rio 2022",
    "Sticker | TRAVIS (Glitter) | Copenhagen 2024",
    "Sticker | TRY | Rio 2022",
    "Sticker | TRY (Glitter) | Rio 2022",
    "Sticker | Vexite (Glitter) | Rio 2022",
    "Sticker | vexite (Glitter) | Shanghai 2024",
    "Sticker | Virtus.pro (Glitter) | Copenhagen 2024",
    "Sticker | Wicadia (Glitter) | Copenhagen 2024",
    "Sticker | westmelon (Glitter) | Copenhagen 2024",
    "Sticker | w0nderful (Glitter) | Champions Copenhagen 2024",
    "Sticker | w0nderful (Glitter) | Copenhagen 2024",
    "Sticker | yuurih (Glitter) | Copenhagen 2024",
    "Sticker | YEKINDAR (Glitter) | Antwerp 2022",
    "Sticker | ZywOo | Rio 2022",
    "Sticker | ZywOo (Glitter) | Antwerp 2022",
    "Sticker | ZywOo (Glitter) | Copenhagen 2024",
    "Sticker | ZywOo (Glitter) | Paris 2023",
    "Sticker | ZywOo (Glitter) | Rio 2022",
    "Sticker | ZywOo (Holo) | Copenhagen 2024",
    "Sticker zont1x (Holo) | Champions Shanghai 2024",
    "Sticker | MOUZ (Glitter) | Copenhagen 2024",
    "Sticker | Vitality (Glitter) | Copenhagen 2024",
    "AWP | Atheris (Minimal Wear)",
    "Desert Eagle | Tilted (Minimal Wear)",
    "AK-47 | Legion of Anubis (Minimal Wear)",
    "Charm | Lil' Crass",
    "Charm | Big Kev",
    "Charm | That's Bananas",
    "Charm | Chicken Lil'",
    "Charm | Pinch O' Salt",
    "Charm | Hot Sauce",
    "Charm | Baby's AK",
    "Charm | Pocket AWP",
    "Charm | Lil' Cap Gun",
    "Shadow Case",
    "Gamma Case",
    "Gamma 2 Case",
    "Spectrum 2 Case",
]

agora = datetime.now().strftime("%d/%m/%Y %H:%M")

HISTORICO_JSON = "utils/historico_stickers.json"
PDF_SAIDA = "generated_files/precos_stickers.pdf"

# Função para pegar preço atual
def obter_preco(nome_item):
    url = "https://steamcommunity.com/market/priceoverview/"
    params = {
        "country": "BR",
        "currency": 7,
        "appid": 730,
        "market_hash_name": nome_item
    }

    while True:
        r = requests.get(url, params=params)
        if r.status_code == 429:
            print("Muitas requisições. Aguardando 1 minuto para tentar novamente...")
            time.sleep(60)  # espera 60 segundos antes de tentar de novo
            continue
        elif r.status_code != 200:
            return None

        data = r.json()
        preco_str = data.get("lowest_price")
        if not preco_str:
            return None
        # Remove símbolos e formata para float
        preco = float(preco_str.replace("R$ ", "").replace(".", "").replace(",", "."))
        return preco


# Carrega histórico do JSON
def carregar_historico():
    if not os.path.exists(HISTORICO_JSON):
        return {}
    with open(HISTORICO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


# Salva histórico no JSON
def salvar_historico(dados):
    with open(HISTORICO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


# Calcula variação percentual
def calcular_variacao(atual, anterior):
    if anterior is None or anterior == 0:
        return None
    return round(((atual - anterior) / anterior) * 100, 2)


# Gera o PDF com cores
def gerar_pdf(dados):
    # Determina dinamicamente os intervalos com pelo menos uma variação não nula
    colunas_validas = set()
    for item in dados:
        for chave, valor in item.items():
            if chave.startswith("var_") and item[chave] is not None:
                colunas_validas.add(chave)

    colunas_ordenadas = sorted(colunas_validas)

    # Ordena os dados pelo maior valor absoluto de variação
    def max_variacao(item):
        variacoes_validas = [abs(item[k]) for k in colunas_ordenadas if item[k] is not None]
        return max(variacoes_validas, default=0)

    dados_ordenados = sorted(dados, key=max_variacao, reverse=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Relatório de Preços - Steam Stickers", ln=True, align="C")
    pdf.ln(10)

    headers = ["Item", "Preço Atual"] + [k.split("_")[1] for k in colunas_ordenadas]
    col_widths = [80, 30] + [20] * len(colunas_ordenadas)

    pdf.set_font("Arial", "B", 9)
    for i, h in enumerate(headers):
        pdf.cell(col_widths[i], 10, h, border=1, align="C")
    pdf.ln()

    pdf.set_font("Arial", "", 8)
    for item in dados_ordenados:
        # Coluna item (nome do sticker)
        pdf.cell(col_widths[0], 10, item["item"][:70], border=1)

        # Define cor de fundo da célula de preço conforme o valor (tons pastéis)
        preco = item["preco_atual"]
        fill = False

        if preco > 100:
            pdf.set_fill_color(255, 179, 186)  # vermelho pastel
            fill = True
        elif preco > 50:
            pdf.set_fill_color(204, 153, 255)  # roxo pastel
            fill = True
        elif preco > 30:
            pdf.set_fill_color(255, 204, 153)  # laranja pastel
            fill = True
        elif preco > 20:
            pdf.set_fill_color(255, 255, 204)  # amarelo pastel
            fill = True
        elif preco > 10:
            pdf.set_fill_color(204, 255, 204)  # verde pastel
            fill = True
        elif preco > 5:
            pdf.set_fill_color(204, 229, 255)  # azul pastel
            fill = True
        elif preco > 1:
            pdf.set_fill_color(224, 224, 224)  # cinza pastel
            fill = True

        # Célula do preço atual com cor de fundo
        pdf.cell(col_widths[1], 10, f'R$ {preco:.2f}', border=1, align="C", fill=fill)

        # Colunas de variações percentuais
        for key in colunas_ordenadas:
            var = item[key]
            if var is None:
                pdf.set_text_color(0, 0, 0)
                txt = "-"
            elif var > 0:
                pdf.set_text_color(0, 150, 0)
                txt = f"+{var:.2f}%"
            elif var < 0:
                pdf.set_text_color(200, 0, 0)
                txt = f"{var:.2f}%"
            else:
                pdf.set_text_color(0, 0, 0)
                txt = "0.00%"
            pdf.cell(20, 10, txt, border=1, align="C")

        pdf.set_text_color(0, 0, 0)
        pdf.ln()

    pdf.output(PDF_SAIDA)

def main():
    hoje = datetime.today().strftime("%Y-%m-%d")
    historico = carregar_historico()
    resultado = []

    for sticker in STICKERS:
        preco_atual = obter_preco(sticker)
        time.sleep(1.5)
        print(sticker)

        if preco_atual is None:
            continue

        if sticker not in historico:
            historico[sticker] = []

        historico[sticker].append({"data": hoje, "preco": preco_atual})
        historico[sticker] = historico[sticker][-31:]

        preco_1d = preco_7d = preco_30d = None
        for registro in historico[sticker]:
            dias_passados = (datetime.strptime(hoje, "%Y-%m-%d") - datetime.strptime(registro["data"], "%Y-%m-%d")).days
            if dias_passados == 1:
                preco_1d = registro["preco"]
            elif dias_passados == 7:
                preco_7d = registro["preco"]
            elif dias_passados == 30:
                preco_30d = registro["preco"]

        resultado.append({
            "item": sticker,
            "preco_atual": preco_atual,
            "var_1d": calcular_variacao(preco_atual, preco_1d),
            "var_7d": calcular_variacao(preco_atual, preco_7d),
            "var_30d": calcular_variacao(preco_atual, preco_30d),
        })

    salvar_historico(historico)
    gerar_pdf(resultado)
    print("PDF gerado:", PDF_SAIDA)

    m.enviar_email_com_anexo(
        destinatario = os.getenv("EMAIL_RECEPTOR"),
        assunto = f"Relatório de Preços - Steam Stickers ({agora})",
        corpo = "Segue em anexo o relatório atualizado dos preços dos stickers Steam.",
        arquivo_caminho=PDF_SAIDA
    )


if __name__ == "__main__":
    main()
