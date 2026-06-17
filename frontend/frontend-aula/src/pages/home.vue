<template>
  <h1>Esta é a home</h1>
  <p class="exemplo">
    Essa é uma pagina!
  </p>
  <ul v-for="value in ddados">
    <li>{{ value.id }}</li>
    <li>{{ value.nome }}</li>
    <li>{{ value.email }}</li>
  </ul>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue'

onMounted(()=>receberDados())

const mensagem = ref('')
const ddados = ref('')

async function receberDados() {

  try {

    const resposta = await fetch(
      'http://127.0.0.1:5000/user',
      {
        method: 'POST',

        headers: {
          'Content-Type': 'application/json'
        },

        body: JSON.stringify()
      }
    )

    const dados = await resposta.json()

    mensagem.value = dados.mensagem

    console.log(dados)
    ddados.value = dados;

  } catch (erro) {

    console.error(erro)

    mensagem.value =
      'Erro ao enviar cadastro.'
  }
}
</script>