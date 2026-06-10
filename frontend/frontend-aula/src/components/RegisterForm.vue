<template>
   <div class="container">
    <div class="row justify-content-md-center">
      <div class="card col-md-auto">

        <h1>Cadastro</h1>

        <form @submit.prevent="enviarFormulario">

          <div class="campo">
            <label>Nome</label>

            <input
              type="text"
              v-model="form.nome"
              placeholder="Digite seu nome"
              required
            />
          </div>

          <button type="submit">
            Cadastrar
          </button>

        </form>

        <p v-if="mensagem" class="mensagem">
          {{ mensagem }}
        </p>

      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

const mensagem = ref('')

const form = reactive({
  nome: '',
  email: ''
})

async function enviarFormulario() {

  try {

    const resposta = await fetch(
      'http://127.0.0.1:5000/cadastro',
      {
        method: 'POST',

        headers: {
          'Content-Type': 'application/json'
        },

        body: JSON.stringify(form)
      }
    )

    const dados = await resposta.json()

    mensagem.value = dados.mensagem

    console.log(dados)

  } catch (erro) {

    console.error(erro)

    mensagem.value =
      'Erro ao enviar cadastro.'
  }
}
</script>

<style scoped>
.card {
  width: 400px;
  background: white;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 0 20px rgba(0,0,0,0.2);
}

h1 {
  text-align: center;
  margin-bottom: 25px;
  color: #0f172a;
}

.campo {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

label {
  margin-bottom: 8px;
  font-weight: bold;
}

input {
  padding: 12px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 15px;
}

input:focus {
  outline: none;
  border-color: #2563eb;
}

button {
  width: 100%;
  padding: 14px;
  border: none;
  border-radius: 8px;
  background: #2563eb;
  color: white;
  font-size: 16px;
  cursor: pointer;
  transition: 0.3s;
}

button:hover {
  background: #1d4ed8;
}

.mensagem {
  text-align: center;
  margin-top: 20px;
  font-weight: bold;
}
</style>