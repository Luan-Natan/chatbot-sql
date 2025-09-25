from flask import Flask, request, jsonify, render_template
from google import genai
from google.genai.types import GenerateContentConfig
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

context = [
    "Você é um especialista em bancos de dados SQL e NoSQL, incluindo os principais SGBDs do mercado.",
    "Responda de forma resumida, objetiva e didática, com exemplos práticos quando necessário.",
    "Dê atenção a boas práticas de modelagem, índices, consultas otimizadas, e diferenças de desempenho entre SQL e NoSQL.",
    "Você não responderá perguntas que não sejam sobre SQL, NoSQL, SGBDs, modelagem de dados ou o ecossistema de bancos de dados.",
    "Quando possível, faça comparações entre diferentes tecnologias e indique cenários em que cada tipo de banco se aplica.",
    "Se a pergunta envolver código, use exemplos claros."
]

MAX_QUESTIONS = 3

# Histórico do ciclo atual
user_questions = []
bot_answers = []

app = Flask(
    __name__,
    template_folder="src/templates",
    static_folder="src/static"
)

def chat_with_gemini(prompt):
    response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=GenerateContentConfig(
            temperature=0.5,
            max_output_tokens=1500
        )
    )
    return response.text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "", "summary": None, "is_summary": False})

    # Responde a pergunta atual normalmente
    prompt = "\n".join(context + [f"Pergunta: {user_message}"])
    reply = chat_with_gemini(prompt)

    # Adiciona pergunta e resposta ao histórico
    user_questions.append(user_message)
    bot_answers.append(reply)

    summary = None
    is_summary = False

    # Se atingir o limite de 3 perguntas, gera resumo
    if len(user_questions) == MAX_QUESTIONS:
        summary_prompt = "Resumo das três perguntas anteriores:\n\n"
        for i in range(MAX_QUESTIONS):
            summary_prompt += f"Pergunta {i+1}: {user_questions[i]}\nResposta {i+1}: {bot_answers[i]}\n\n"

        summary = chat_with_gemini(summary_prompt)
        is_summary = True

        # Reseta histórico para próximo ciclo
        user_questions.clear()
        bot_answers.clear()

    # Retorna resposta atual + resumo se houver
    return jsonify({
        "reply": reply,
        "summary": summary,
        "is_summary": is_summary
    })

if __name__ == "__main__":
    app.run(debug=True)
