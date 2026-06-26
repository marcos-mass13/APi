<template>

<div class="w-full md:w-48 h-32 bg-gray-200 rounded-xl overflow-hidden flex items-center justify-center text-gray-400 font-mono text-xs">
      [ Imagem Notícia ]
    </div>
    <div class="flex-1 flex flex-col justify-between">
      <div>
        <span class="text-xs font-bold uppercase tracking-wider text-green-600 bg-green-50 px-2.5 py-1 rounded-md">Notícia</span>
        <h3 class="text-xl font-bold text-gray-900 mt-2 mb-2">{{ item.title }}</h3>
        <p class="text-gray-600 text-sm line-clamp-2">{{ item.content }}</p>
      </div>
      <div class="flex items-center justify-between mt-4 text-xs text-gray-400">
        <span>Por: Autor ID {{ item.usuario_id }}</span>
        <span>{{ formatarData(item.created_at) }}</span>
      </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';
const props = defineProps({item: Object});

// Formatador básico de datas dinâmicas
const formatarData = (stringData) => {
  if (!stringData) return '';
  const data = new Date(stringData);
  return data.toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' });
};
</script>