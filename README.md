# 🤖 Chatbot SQL/NoSQL

Este projeto é um **chatbot interativo** focado em **bancos de dados SQL e NoSQL**, que responde perguntas do usuário de forma resumida e prática, incluindo exemplos de código. Após cada 3 perguntas, o chatbot gera um resumo automático das respostas. 

`Modelo de API utilizada: gemini-2.5-flash.`

---

## 🎯 Objetivo

Permitir que usuários aprendam conceitos de **SQL, NoSQL e ecossistema de SGBDs** de maneira rápida e interativa, com respostas claras e exemplos práticos.

---

## 📹 Vídeo de Demonstração

Você pode assistir à execução do chatbot no vídeo:  
[Link para o vídeo] https://drive.google.com/drive/folders/1we50nXq1ZSK4SJnJ_VWDu_qA4b8qiHvR?usp=sharing

---

## 😎 Chatbot hospedado

Você pode interagir com o chabot nesse link da vercel:  
[Link para o chatbot] https://chatbot-sql.vercel.app

---

## 🏃‍♂️ Como Executar Localmente

### ⚙️ Requisitos
- Navegador moderno (Chrome, Edge, Firefox, etc.)
- **Python 3** (para rodar o servidor Flask)
- **API Key Gemini** da Google (armazenada em `.env`)

1. Clone o repositório:
   ```bash
   git clone https://github.com/Luan-Natan/chatbot-sql.git
   cd chatbot-sql

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt

3. Crie um arquivo .env na raiz com sua API key:
    env
    ```bash
    GEMINI_API_KEY=SUA_CHAVE_AQUI

4. Inicie o servidor Flask:
    ```bash
    cd src
    python app.py

5. Abra o navegador e acesse:
    http://localhost:5000

## 📂 Estrutura do Projeto
    📦 chatbot-sql
    │   .env
    │   .env-example
    │   .gitignore
    │   app.py
    │   README.md
    │   requirements.txt
    │   vercel.json
    │
    └───src
        ├───static
        │       script.js
        │       style.css
        │
        └───templates
                index.html

## 💡 Funcionalidades
1. Chat interativo com efeito de digitação.

2. Respostas formatadas com exemplos em SQL, MongoDB e outros SGBDs.

3. Resumo automático após cada 3 perguntas.

## 👨‍💻 Autor
Desenvolvido por Luan Natan de Sousa 🚀