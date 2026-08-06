<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <div class="input-group">
        <label>E-mail</label>
        <input type="email" v-model="email" required />
      </div>
      <div class="input-group">
        <label>Senha</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Entrar</button>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const email = ref('');
const password = ref('');
const errorMessage = ref('');
const router = useRouter();

const handleLogin = async () => {
  try {
    // Substitua pela chamada da sua API real
    const response = await fakeAuthApi(email.value, password.value);
    
    // Salva o token retornado no localStorage
    localStorage.setItem('userToken', response.token);
    
    // Redireciona para a página protegida
    router.push('/dashboard');
  } catch (error) {
    errorMessage.value = 'E-mail ou senha inválidos.';
  }
};

// Função simulada de API (substitua por fetch ou axios)
const fakeAuthApi = (email, password) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (email === 'usuario@exemplo.com' && password === 'senha123') {
        resolve({ token: 'seu-token-de-autenticacao-jwt-aqui' });
      } else {
        reject(new Error('Falha na autenticação'));
      }
    }, 1000);
  });
};
</script>

<style scoped>
.login-container { max-width: 300px; margin: auto; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
.input-group { margin-bottom: 15px; }
.input-group label { display: block; margin-bottom: 5px; }
.input-group input { width: 100%; padding: 8px; box-sizing: border-box; }
button { width: 100%; padding: 10px; background-color: #42b883; color: white; border: none; cursor: pointer; }
.error { color: red; margin-top: 10px; }
</style>
