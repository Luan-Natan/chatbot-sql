let cycleCount = 0; // ciclo de cores

async function sendMessage() {
  const input = document.getElementById("message");
  const chat = document.getElementById("chat");
  const userMessage = input.value.trim();
  if (!userMessage) return;

  appendMessage(userMessage, "user");
  input.value = "";

  // indicador de digitação
  const typingEl = document.createElement("div");
  typingEl.className = "message typing show";
  typingEl.textContent = "Digitando…";
  chat.appendChild(typingEl);
  chat.scrollTop = chat.scrollHeight;

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage }),
    });
    const data = await res.json();

    typingEl.remove();

    // resposta normal do bot
    appendMessage(data.reply, `bot cycle${cycleCount % 3}`);

    // se tiver resumo (após cada 3ª pergunta)
    if (data.is_summary && data.summary) {
      appendMessage("📌 Resumo das três perguntas:", "summary");
      appendMessage(data.summary, "summary");
      cycleCount++;
    }
  } catch (e) {
    typingEl.remove();
    appendMessage("⚠️ Erro ao contactar o servidor.", "summary");
  }
}

function appendMessage(text, type) {
  const chat = document.getElementById("chat");

  let html = text
    .replace(
      /^### (.*)$/gm,
      '<h3 style="margin:6px 0 2px 0; line-height:1.3; font-weight:600;">$1</h3>'
    )
    .replace(
      /^## (.*)$/gm,
      '<h2 style="margin:8px 0 3px 0; line-height:1.3; font-weight:600;">$1</h2>'
    )
    .replace(/^---$/gm, "<hr>")
    .replace(
      /```(sql|javascript|json|csharp)?([\s\S]*?)```/gi,
      "<pre><code>$2</code></pre>"
    )
    .replace(
      /^(sql|javascript|json|csharp)\n([\s\S]*)/gim,
      "<pre><code>$2</code></pre>"
    )
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/^\* (.+)$/gm, "<ul><li>$1</li></ul>")
    .replace(/^\s*\* (.+)$/gm, "<li>$1</li>")
    .replace(/`(.+?)`/g, "<code>$1</code>")
    .replace(/\n/g, "<br>");

  const div = document.createElement("div");
  div.className = `message ${type}`;
  div.innerHTML = html;
  chat.appendChild(div);
  requestAnimationFrame(() => div.classList.add("show"));
  chat.scrollTop = chat.scrollHeight;
}
