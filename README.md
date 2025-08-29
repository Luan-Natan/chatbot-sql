# 🤖 Chatbot SQL/NoSQL

Este projeto é um **chatbot interativo** focado em **bancos de dados SQL e NoSQL**, que responde perguntas do usuário de forma resumida e prática, incluindo exemplos de código. Após cada 3 perguntas, o chatbot gera um resumo automático das respostas. 

`Modelo de API utilizada: gemini-2.5-flash.`

---

## 🎯 Objetivo

Permitir que usuários aprendam conceitos de **SQL, NoSQL e ecossistema de SGBDs** de maneira rápida e interativa, com respostas claras e exemplos práticos.

---

## 📹 Vídeo de Demonstração

Você pode assistir à execução do chatbot no vídeo:  
[Link para o vídeo](COLE_AQUI_O_LINK_DO_YOUTUBE_OU_DRIVE)

---

## ⚙️ Requisitos

- Navegador moderno (Chrome, Edge, Firefox, etc.)
- **Python 3** (para rodar o servidor Flask)
- **API Key Gemini** da Google (armazenada em `.env`)

---

## 🏃‍♂️ Como Executar Localmente

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
    ├── templates/src
    │   ├── templates/index.html # Página principal
    │   ├── static/style.css     # Estilos do chat
    │   └── static/script.js     # Lógica do chatbot
    ├── app.py           # Servidor Flask
    ├── .env-example     # Alterar para .env para adicionar sua API Key
    ├── .gitignore       # Ignorar arquivos desnecessários
    ├── README.md        # Documentação
    └── requirements.txt # Dependências Python

## 💡 Funcionalidades
1. Chat interativo com efeito de digitação.

2. Respostas formatadas com exemplos em SQL, MongoDB e outros SGBDs.

3. Resumo automático após cada 3 perguntas.

## 👨‍💻 Autor
Desenvolvido por Luan Natan de Sousa 🚀