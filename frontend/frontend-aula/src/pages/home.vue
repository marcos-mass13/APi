<template>
  <h1>Esta é a home</h1>
  <p class="exemplo">
    Essa é uma pagina!
  </p>
 <div v-if="dados.length>0">
   <ul v-for="value in dados">
    <li>{{ value.id }}</li>
    <li>{{ value.nome }}</li>
    <li>{{ value.email }}</li>
  </ul>
 </div>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue'

const urlDaApi = import.meta.env.VITE_API_URL;

onMounted(()=>receberDados())

const mensagem = ref('')
const dados = ref('')

async function receberDados() {

  try {

    const resposta = await fetch(
      urlDaApi+'/',
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify()
      }
    )

    const data = await resposta.json()

    mensagem.value = data.mensagem

    console.log(data)
    dados.value = data;

  } catch (erro) {

    console.error(erro)

    mensagem.value =
      'Erro ao enviar cadastro.'
  }
}
</script>