<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="input-group">
        <label>E-mail</label>
        <input type="email" v-model="formulario.email" required />
      </div>
      <div class="input-group">
        <label>Senha</label>
        <input type="password" v-model="formulario.senha" required />
      </div>
      <button type="submit">Entrar</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script setup>
import { inject, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAlert } from "@/composables/useAlert";

const { open } = useAlert();
const path = inject('path');
const mensagem = ref('');
const errorMessage = ref('');
const router = useRouter();

const formulario = ref({
  email:'',
  senha:''
})

const handleLogin = async ()=>{
  try {

     const payload = {
      email: formulario.value.email,
      senha: formulario.value.senha,
    };

    const resposta = await fetch(
      path+'/usuarios/login',
      {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify(payload)
      }
    )
    const dados = await resposta.json();
    if(dados.erro =="Erro"){
      open("Login","Falha no acesso recusado!","danger")
      return console.error("Acesso recusado");
    }

    if(resposta.ok){
      mensagem.value = dados.mensagem;
      open("Login","Acesso aprovado!","sucess")
      console.info("Acesso aprovado");
      localStorage.setItem('userToken', dados.token);
      return router.push('/');
    }
    else{
      console.error(
        "Erro ao Buscar dados do servidor: ", resposta.status
      );      
      open("Atenção","Erro ao Buscar dados do servidor:","danger")
    }
    
  } catch (error) {
    console.error("Erro de Rede: ",error);
    open("Atenção","Falha ao realizar login","danger")
  }
}

// Botão para logoff ===>>>   <button type="button" @click="handleLogoff">Logoff</button> 
const handleLogoff = ()=>{
localStorage.removeItem('userToken');
router.push('/login');
}

</script>

<style scoped>
.login-container { max-width: 300px; margin: auto; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
.input-group { margin-bottom: 15px; }
.input-group label { display: block; margin-bottom: 5px; }
.input-group input { width: 100%; padding: 8px; box-sizing: border-box; }
button { width: 100%; padding: 10px; background-color: #42b883; color: white; border: none; cursor: pointer; }
.error { color: red; margin-top: 10px; }
</style>
