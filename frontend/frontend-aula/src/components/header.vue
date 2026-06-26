<template>
    <header class="flex flex-col md:flex-row md:items-center md:justify-between mb-8 pb-6 border-b border-gray-200">
        <div>
          <h1 class="text-3xl font-bold text-gray-900 tracking-tight">Esta é a {{Title}}</h1>
          <p class="text-green-600 font-medium mt-1">Essa é uma página dinâmica conectada ao seu Backend!</p>
        </div>
        
        <!-- <div class="mt-4 md:mt-0 text-sm text-gray-500 bg-white px-4 py-2 rounded-xl shadow-sm border border-gray-100"> -->
          <!-- 📍 API: <code class="text-xs text-purple-600 font-mono">{{ urlDaApi }}</code> -->
          <!-- 📍 API: <code class="text-xs text-purple-600 font-mono">{{ urlDaApi }}</code> -->
        <!-- </div> -->
      </header>
</template>

<script setup>
import { defineProps } from "vue";
const props = defineProps({
  Title:Text});
</script>