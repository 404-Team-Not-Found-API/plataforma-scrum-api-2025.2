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

