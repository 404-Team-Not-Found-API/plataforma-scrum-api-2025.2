// ====== MENU LATERAL ======
const menuBtn = document.getElementById("menuToggle");
const menuLateral = document.getElementById("menuLateral");

menuBtn.addEventListener("click", () => {
  menuLateral.classList.toggle("ativo");
  menuBtn.classList.toggle("ativo");
});

document.querySelectorAll(".menu-lateral a").forEach(link => {
  link.addEventListener("click", () => {
    menuLateral.classList.remove("ativo");
    menuBtn.classList.remove("ativo");
  });
});

// ===== MODAL =====
const modal = document.getElementById("meuModal");
const modalTitulo = document.getElementById("modalTitulo");
const modalTexto = document.getElementById("modalTexto");

function abrirModal(titulo, texto) {
  modalTitulo.textContent = titulo;
  modalTexto.innerHTML = texto;
  modal.style.display = "flex";
}

function fecharModal() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target === modal) fecharModal();
};

// ====== QUIZ ======
document.getElementById("verificar").addEventListener("click", () => {
  const radios = document.querySelectorAll("input[type=radio]");
  let corretas = 0;
  const total = 3;

  radios.forEach(radio => {
    const label = radio.parentElement;

    // Resetar antes de verificar
    label.style.color = "#1a202c";
    label.style.fontWeight = "normal";

    if (radio.checked) {
      if (radio.value === "correto") {
        label.style.color = "#2f855a"; // verde
        label.style.fontWeight = "600";
        corretas++;
      } else {
        label.style.color = "#e53e3e"; // vermelho
        label.style.fontWeight = "600";
      }
    }
  });

  // Exibir o resultado
  const resultado = document.getElementById("resultadoQuiz");
  if (corretas === total) {
    resultado.textContent = `Parabéns! Você acertou todas as ${total} perguntas! 🎯`;
    resultado.style.color = "#2f855a";
  } else {
    resultado.textContent = `Você acertou ${corretas} de ${total} perguntas.`;
    resultado.style.color = "#e53e3e";
  }
});
