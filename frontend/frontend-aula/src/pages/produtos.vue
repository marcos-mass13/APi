<template>
  
  <main class="flex-1 p-6 md:p-10 max-w-7xl mx-auto w-full overflow-y-auto">
    
    <Header :-title="Title"/>

    <div class="flex justify-end mb-6 w-full">
      <button
      @click="abrirModalCriar" 
      class="bg-green-600 hover:bg-green-700 text-white font-semibold px-5 py-2.5 rounded-xl shadow-sm transition flex items-center space-x-2 whitespace-nowrap"
      >
        <span>➕ Criar Nova Publicação</span>
      </button>
    </div>
    
    <p v-if="mensagem" class="mensagem">
      {{ mensagem }}
    </p>

    <div v-if="loading" class="flex justify-center items-center py-20">

      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-green-500"></div>

    </div>

    <div v-else class="flex flex-col gap-6 w-full">
      
      <article v-for="produto in data" :key="produto.id" class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition flex flex-col sm:flex-row gap-6 w-full">
        
        <CardPost v-if="data.length>0" :item="produto"/>
      
      </article>

    </div>

  </main>
  
<div 
      v-if="modalAberto" 
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50 animate-fade-in"
    >
      <div class="bg-white rounded-2xl shadow-xl max-w-md w-full overflow-hidden transform transition-all p-6">
        <div class="flex items-center justify-between pb-4 border-b border-gray-100">
          <h3 class="text-xl font-bold text-gray-900">
            Novo Produto
          </h3>
          <button @click="fecharModal" class="text-gray-400 hover:text-gray-600 text-xl">&times;</button>
        </div>

        <form @submit.prevent="salvarPublicacao" class="space-y-4 mt-4">

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Título</label>
            <input 
              v-model="formulario.title" 
              type="text" 
              required
              placeholder="Ex: Lançamento do framework"
              class="w-full border border-gray-300 rounded-xl px-3 py-2.5 focus:outline-none focus:ring-2 focus:ring-green-500"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Preço (R$)</label>
            <input 
              v-model.number="formulario.price" 
              type="number" 
              step="0.01"
              required
              placeholder="0.00"
              class="w-full border border-gray-300 rounded-xl px-3 py-2.5 focus:outline-none focus:ring-2 focus:ring-green-500"
            />
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-1">Conteúdo / Descrição</label>
            <textarea 
              v-model="formulario.content" 
              rows="4" 
              required
              placeholder="Escreva os detalhes aqui..."
              class="w-full border border-gray-300 rounded-xl px-3 py-2.5 focus:outline-none focus:ring-2 focus:ring-green-500"
            ></textarea>
          </div>

          <div class="flex items-center space-x-3 pt-4 border-t border-gray-100 justify-end">
            <button 
              type="button" 
              @click="fecharModal" 
              class="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-600 font-medium rounded-xl transition"
            >
              Cancelar
            </button>
            <button 
              type="submit" 
              class="px-5 py-2 bg-green-600 hover:bg-green-700 text-white font-medium rounded-xl shadow-sm transition"
            >
              Publicar
            </button>
          </div>
        </form>
      </div>
    </div>

</template>

<script setup lang='ts'>
  import { ref, onMounted } from 'vue';
  import Header from '../components/header.vue';
  import CardPost from '../MyComponents/cardPost.vue';

  const mensagem = ref('');
  const data= ref({});
  const Title = "Produtos";

  const loading = ref(true);

  const modalAberto = ref(false);

  // Estrutura padrão do formulário limpo
const formulario = ref({
  tipo: 'produto',
  title: '',
  content: '',
  price: ''
});

// Controle do Modal
const abrirModalCriar = () => {
  formulario.value = { tipo: 'produto', title: '', content: '', price: '' };
  modalAberto.value = true;
};

const fecharModal = () => {
  modalAberto.value = false;
};


// Integração com as Rotas do Backend (POST / PUT)
const salvarPublicacao = async () => {
  try {
    const payload = {
      title: formulario.value.title,
      content: formulario.value.content,
      price: formulario.value.price,
      usuario_id: 1 // ID do usuário mocando autenticação básica
    };


    const resposta = await fetch(
      'http://127.0.0.1:5000/produtos',
      {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
      }
    )

    if (resposta.ok) {
      const dados = await resposta.json();
      console.log("DADOS DO PYTHON:", dados);
      mensagem.value = dados.mensagem;

    } else {
      console.error("Erro ao buscar dados do servidor:", resposta.status);
    }

    fecharModal();

  }catch (error) {
    console.error("Erro de rede:", error);
    // Fallback local se a API estiver fora do ar para fins de teste visual:
    mensagem.value = 'Erro ao enviar cadastro.'
  };
}

  const buscarPublicacoes = async () => {
    try {
     const resposta = await fetch(`http://127.0.0.1:5000/produtos`);

    if (resposta.ok) {
      const dados = await resposta.json();
      console.log("DADOS DO PYTHON:", dados);
      mensagem.value = dados.mensagem;
      data.value = dados.produtos;
      if(data.value.length>0) loading.value = false;
    } else {
      console.error("Erro ao buscar dados do servidor:", resposta.status);
    }
    } catch (e) {
    loading.value = false;
  }};
  onMounted(() => {
  buscarPublicacoes();
});

// Dados de teste idênticos ao layout da imagem para a tela não abrir em branco
const mockarDadosDeTeste = () => {
  data.value = [
    { id: 3, title: 'Câmera Mirrorless Pro 2', content: 'Sensor full-frame de alta resolução, ideal para gravações profissionais.', price: 277.00, type: 'produto' },
    { id: 3, title: 'Câmera Mirrorless Pro 2', content: 'Sensor full-frame de alta resolução, ideal para gravações profissionais.', price: 277.00, type: 'produto' },
    { id: 3, title: 'Câmera Mirrorless Pro 2', content: 'Sensor full-frame de alta resolução, ideal para gravações profissionais.', price: 277.00, type: 'produto' },
    { id: 4, title: 'Fone Bluetooth Premium', content: 'Cancelamento de ruído ativo e bateria de longa duração.', price: 399.00, type: 'produto' }
  ];
};

</script>