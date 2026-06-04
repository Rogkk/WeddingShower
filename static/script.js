const selectPresentes = document.getElementById("presente");
const form = document.getElementById("giftForm");
const mensagem = document.getElementById("mensagem");

async function carregarPresentes() {

    const response = await fetch("/presentes");

    const presentes = await response.json();

    selectPresentes.innerHTML =
        '<option value="">Selecione um presente</option>';

    presentes.forEach(presente => {

        selectPresentes.innerHTML += `
            <option value="${presente.id}">
                ${presente.nome}
            </option>
        `;
    });
}

carregarPresentes();

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const nome = document.getElementById("nome").value;
    const presenteId = selectPresentes.value;

    const response = await fetch("/escolher", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            nome,
            presente_id: presenteId
        })

    });

    const data = await response.json();

    mensagem.innerHTML = data.mensagem;

    if(data.sucesso){

        form.reset();

        carregarPresentes();
    }

});