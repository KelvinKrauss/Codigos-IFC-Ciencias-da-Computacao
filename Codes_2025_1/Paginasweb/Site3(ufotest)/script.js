const ufo1 = document.getElementById("ufo1");
const ufo2 = document.getElementById("ufo2");
const velocidadeSelect = document.getElementById("velocidade");

let larguraArea = window.innerWidth;
let larguraUfo = ufo1.offsetWidth;

let pos1 = 0;
let pos2 = larguraArea - larguraUfo;

let direcao1 = 1; // direita
let direcao2 = -1; // esquerda

let velocidade = Number(velocidadeSelect.value);

velocidadeSelect.addEventListener("change", () => {
    velocidade = Number(velocidadeSelect.value);
});

function animar() {
    larguraArea = window.innerWidth; // Atualiza em resize

    pos1 += direcao1 * velocidade;
    pos2 += direcao2 * velocidade;

    if (pos1 + larguraUfo >= larguraArea) direcao1 = -1;
    if (pos1 <= 0) direcao1 = 1;

    if (pos2 <= 0) direcao2 = 1;
    if (pos2 + larguraUfo >= larguraArea) direcao2 = -1;

    ufo1.style.left = pos1 + "px";
    ufo2.style.left = pos2 + "px";

    requestAnimationFrame(animar);
}

animar();

window.addEventListener("resize", () => {
    larguraArea = window.innerWidth;
});
