<template>

  <div class="w-20 h-20 bg-gray-100 rounded-xl flex items-center justify-center text-gray-400 font-mono text-2xs p-2 text-center">
    [ 📦 ]
  </div>
  <div class="flex-1">
    <h3 class="font-bold text-gray-900 text-base">{{ produto.title }}</h3>
    <p class="text-gray-500 text-xs line-clamp-1 mb-2">{{ produto.content }}</p>
    <div class="flex items-center justify-between">
      <span class="text-lg font-extrabold text-gray-900">R$ {{ produto.price?.toFixed(2) }}</span>
      <button class="text-xs bg-gray-900 text-white px-3 py-1.5 rounded-lg hover:bg-gray-800 font-medium transition">
        Comprar
      </button>
    </div>
  </div>

</template>

<script setup>
import { defineProps } from 'vue';
const props = defineProps({produto: Object});
</script>

<style scoped>

</style>