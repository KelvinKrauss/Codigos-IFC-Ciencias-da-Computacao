const botao = document.getElementById("botao");
const paredes = document.querySelectorAll(".parede");

let arrastando = false;
let offsetX = 0;
let offsetY = 0;

botao.addEventListener("mousedown", (e) => {
    arrastando = true;
    offsetX = e.clientX - botao.offsetLeft;
    offsetY = e.clientY - botao.offsetTop;
});

document.addEventListener("mouseup", () => {
    arrastando = false;
});

document.addEventListener("mousemove", (e) => {
    if (arrastando) {
        const x = e.clientX - offsetX;
        const y = e.clientY - offsetY;
        botao.style.left = `${x}px`;
        botao.style.top = `${y}px`;
        verificarColisao();
    }
});

function verificarColisao() {
    const rectBotao = botao.getBoundingClientRect();
    let colidindo = false;

    paredes.forEach(parede => {
        const rectParede = parede.getBoundingClientRect();

        const colide = !(
            rectBotao.right < rectParede.left ||
            rectBotao.left > rectParede.right ||
            rectBotao.bottom < rectParede.top ||
            rectBotao.top > rectParede.bottom
        );

        if (colide) {
            colidindo = true;
        }
    });

    botao.style.backgroundColor = colidindo ? "red" : "blue";
}
