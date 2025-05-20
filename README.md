# 🖼️ Steam-Sticker-Scrapper

Script para gerar automaticamente um **relatório em PDF** com os preços atuais de stickers de CS2 no Steam Market, incluindo **variações de 1, 7 e 30 dias**, e enviar por **e-mail com anexo**.

## 📁 Estrutura esperada

O projeto depende de dois arquivos principais:

- `main.py`: responsável por buscar os preços, calcular variações e gerar o PDF.
- `mensageiro.py`: módulo auxiliar que realiza o envio do PDF por e-mail.

## 📦 Requisitos

Instale as dependências com:

```bash
pip install fpdf requests
```

## ⚙️ Configuração de Ambiente

Defina as seguintes variáveis de ambiente (via `.env` ou diretamente no sistema):

| Variável         | Descrição                            |
|------------------|----------------------------------------|
| `EMAIL_USER`     | E-mail do remetente                   |
| `EMAIL_PASSWORD` | Senha ou app password                 |
| `EMAIL_HOST`     | Host SMTP (ex: smtp.gmail.com)        |
| `EMAIL_PORT`     | Porta SMTP (ex: 587)                  |
| `EMAIL_RECEPTOR` | E-mail do destinatário do relatório   |

Exemplo:

```bash
export EMAIL_USER=seu@email.com
export EMAIL_PASSWORD=sua_senha
export EMAIL_HOST=smtp.gmail.com
export EMAIL_PORT=587
export EMAIL_RECEPTOR=destinatario@email.com
```

## 📊 O que o script faz?

- Consulta os preços dos stickers definidos na lista `STICKERS`.
- Compara os valores atuais com os de 1, 7 e 30 dias atrás.
- Gera um PDF com destaques visuais:
  - 🟩 Verde para aumento de preço
  - 🟥 Vermelho para queda de preço
- Envia o PDF automaticamente por e-mail.

## 📂 Saídas

- `generated_files/precos_stickers.pdf`: PDF com os preços e variações.
- `utils/historico_stickers.json`: Armazena os históricos para cálculo de variações.

## ⏱️ Observações

- Limita requisições à Steam com `time.sleep(2)` entre chamadas.
- Em caso de erro `429 (rate limit)`, aguarda 10 minutos antes de tentar novamente.
- Mantém histórico de **31 dias por item**.

## ▶️ Como executar

```bash
python main.py
```

## 📧 Exemplo de envio

O e-mail enviado terá:

- **Assunto**: `Relatório de Preços - Steam Stickers (dd/mm/yyyy hh:mm)`
- **Corpo**: Texto simples informando o envio.
- **Anexo**: PDF com os dados de preço.

## 🧼 Git e versionamento

Adicione ao seu `.gitignore`:

```
.idea/
utils/historico_stickers.json
generated_files/
```
