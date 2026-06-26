<template>       

    <main class="flex-1 p-6 md:p-10 max-w-7xl mx-auto w-full overflow-y-auto">
      
      <!-- <header class="flex flex-col md:flex-row md:items-center md:justify-between mb-8 pb-6 border-b border-gray-200">
        <div>
          <h1 class="text-3xl font-bold text-gray-900 tracking-tight">Esta é a home</h1>
          <p class="text-green-600 font-medium mt-1">Essa é uma página dinâmica conectada ao seu Backend!</p>
        </div>
        <div class="mt-4 md:mt-0 text-sm text-gray-500 bg-white px-4 py-2 rounded-xl shadow-sm border border-gray-100">
          📍 API: <code class="text-xs text-purple-600 font-mono">{{ urlDaApi }}</code>
        </div>
      </header> -->  

      <div v-if="loading" class="flex justify-center items-center py-20">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-green-500"></div>
      </div>

      <div v-else class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <div class="lg:col-span-2 space-y-6">
          <div class="flex items-center justify-between mb-2">
            <h2 class="text-2xl font-bold text-gray-900">Últimas Postagens</h2>
            <span class="text-xs font-semibold bg-gray-200 text-gray-700 px-2.5 py-1 rounded-full">{{ listagemNoticias.length }} notícias</span>
          </div>

          <div v-if="listagemNoticias.length === 0" class="bg-white p-6 rounded-2xl border border-gray-100 text-center text-gray-500">
            Nenhuma notícia cadastrada no momento.
          </div>

          <article v-for="noticia in listagemNoticias" :key="noticia.id" class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition flex flex-col md:flex-row gap-6">
            <CardPost v-if="listagemNoticias.length>0" :item="noticia"/>
          </article>
        </div>

        <div class="space-y-6">
          <div class="flex items-center justify-between mb-2">
            <h2 class="text-2xl font-bold text-gray-900">Produtos</h2>
            <span class="text-xs font-semibold bg-gray-200 text-gray-700 px-2.5 py-1 rounded-full">{{ listagemProdutos.length }} itens</span>
          </div>

          <div v-if="listagemProdutos.length === 0" class="bg-white p-6 rounded-2xl border border-gray-100 text-center text-gray-500">
            Nenhum produto cadastrado no momento.
          </div>

          <div v-for="produto in listagemProdutos" :key="produto.id" class="bg-white p-4 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition flex items-center space-x-4">
            
            <CardProd v-if="listagemProdutos.length>0" :produto="produto"/>

          </div>
        </div>

      </div>
    </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import CardProd from '../MyComponents/cardProd.vue';
import CardPost from '../MyComponents/cardPost.vue';
import MyNavBar from '../MyComponents/MyNavBar.vue';

const Page = "Home";

// Estados Reativos
const listagemNoticias = ref([]);
const listagemProdutos = ref([]);
const loading = ref(true);

// Função para buscar as publicações no banco através do seu Backend Python
const buscarPublicacoes = async () => {
  try {
    loading.value = true;
    // IMPORTANTE: Fazendo o fetch na rota correta de listagem do seu backend
    const resposta = await fetch(`http://127.0.0.1:5000/`);
    
    if (resposta.ok) {
      const dados = await resposta.json();
      
      // Filtra o array de publicações vindo do banco baseado no campo 'type' que modelamos
      listagemNoticias.value = dados.noticias;
      listagemProdutos.value = dados.produtos;
    } else {
      console.error("Erro ao buscar dados do servidor:", resposta.status);
      mockarDadosDeTeste(); // Fallback caso a API ainda não esteja respondendo a rota
    }
  } catch (error) {
    console.error("Erro de conexão com a API:", error);
    mockarDadosDeTeste(); // Fallback
  } finally {
    loading.value = false;
  }
};

// // Dados de teste idênticos ao layout da imagem para a tela não abrir em branco
// const mockarDadosDeTeste = () => {
//   listagemNoticias.value = [
//     { id: 1, title: 'Novidades no Desenvolvimento Vue 4', content: 'Confira as atualizações de performance e as novas diretivas estruturais do ecossistema front-end para este ano.', type: 'noticia', usuario_id: 1, created_at: '2026-06-24T12:00:00Z' },
//     { id: 2, title: 'Dicas de UX para E-commerce', content: 'Aprenda como estruturar a hierarquia visual e os botões de ação para reter mais usuários e converter vendas.', type: 'noticia', usuario_id: 2, created_at: '2026-06-23T15:30:00Z' }
//   ];
//   listagemProdutos.value = [
//     { id: 3, title: 'Câmera Mirrorless Pro 2', content: 'Sensor full-frame de alta resolução, ideal para gravações profissionais.', price: 277.00, type: 'produto' },
//     { id: 4, title: 'Fone Bluetooth Premium', content: 'Cancelamento de ruído ativo e bateria de longa duração.', price: 399.00, type: 'produto' }
//   ];
// };

// Formatador básico de datas dinâmicas
const formatarData = (stringData) => {
  if (!stringData) return '';
  const data = new Date(stringData);
  return data.toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' });
};

// Dispara a busca assim que o componente é montado na tela
onMounted(() => {
  buscarPublicacoes();
});
</script>

<style scoped>
/* Ajuste fino para truncamento de linhas longas de descrição */
.line-clamp-1 {
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;  
  overflow: hidden;
}
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;  
  overflow: hidden;
}
</style>