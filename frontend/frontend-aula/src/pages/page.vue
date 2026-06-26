<template>
  
  <main class="flex-1 p-6 md:p-10 max-w-7xl mx-auto w-full overflow-y-auto">
    
    <Header :url-da-api="urlDaApi"/>

    <div v-if="loading" class="flex justify-center items-center py-20">

      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-green-500"></div>

    </div>

    <div v-else class="flex flex-col gap-6 w-full">

      <!-- <article v-for="noticia in data" :key="noticia.id" class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition flex flex-col sm:flex-row gap-6 w-full"> -->

      <RegisterForm/>

      <!-- </article> -->

    </div>

  </main>
</template>

<script setup lang='ts'>
  import { ref, onMounted } from 'vue';
  import Header from '../components/header.vue';
  import RegisterForm from '../components/RegisterForm.vue';

  const urlDaApi = (typeof import.meta !== 'undefined' && import.meta.env?.VITE_API_URL) 
    ? import.meta.env.VITE_API_URL 
    : 'https://project-je3vo.vercel.app';
    
  const loading = ref(true);

  const buscarPublicacoes = async () => {
    loading.value = false;
  }
  onMounted(() => {
  buscarPublicacoes();
});

// // Dados de teste idênticos ao layout da imagem para a tela não abrir em branco
// const mockarDadosDeTeste = () => {
//   listagemNoticias.value = [
//     { id: 1, title: 'Novidades no Desenvolvimento Vue 4', content: 'Confira as atualizações de performance e as novas diretivas estruturais do ecossistema front-end para este ano.', type: 'noticia', usuario_id: 1, created_at: '2026-06-24T12:00:00Z' },
//     { id: 2, title: 'Dicas de UX para E-commerce', content: 'Aprenda como estruturar a hierarquia visual e os botões de ação para reter mais usuários e converter vendas.', type: 'noticia', usuario_id: 2, created_at: '2026-06-23T15:30:00Z' }
//   ];
  // listagemProdutos.value = [
  //   { id: 3, title: 'Câmera Mirrorless Pro 2', content: 'Sensor full-frame de alta resolução, ideal para gravações profissionais.', price: 277.00, type: 'produto' },
  //   { id: 4, title: 'Fone Bluetooth Premium', content: 'Cancelamento de ruído ativo e bateria de longa duração.', price: 399.00, type: 'produto' }
  // ];
// };
</script>