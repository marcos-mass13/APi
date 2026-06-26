<template>

  <aside class="w-64 bg-white border-r border-gray-200 p-6 flex flex-col justify-between hidden md:flex">
    <div>
      <div class="flex items-center space-x-3 mb-10">
        <svg class="h-8 w-8 text-green-500" viewBox="0 0 256 221" version="1.1" xmlns="http://www.w3.org/2000/svg"><path fill="#41B883" d="M204.8 0H256L128 220.8L0 0h51.2L128 132.4L204.8 0z"/><path fill="#35495E" d="M51.2 0H128l76.8 0l42.6 73.6L128 220.8L3.4 73.6L51.2 0z"/></svg>
        <span class="text-xl font-bold tracking-wide">Painel Vue</span>
      </div>
      
  
    <nav class="space-y-2">
      <a href="#" class="flex items-center space-x-3 bg-green-50 text-green-700 p-3 rounded-xl font-medium transition">
        <span>
          <router-link to="/">
            📊 Dashboard
            </router-link>
          </span>

      </a>
      <a href="#" class="flex items-center space-x-3 text-gray-600 hover:bg-gray-50 p-3 rounded-xl font-medium transition">
        <span>
          <router-link to="/publicacoes">
            📰 Postagens
            </router-link>
        </span>
      </a>
      <a href="#" class="flex items-center space-x-3 text-gray-600 hover:bg-gray-50 p-3 rounded-xl font-medium transition">
        <span>
          <router-link to="/produtos">
            📦 Produtos
            </router-link>
        </span>
      </a>
      <a href="#" class="flex items-center space-x-3 text-gray-600 hover:bg-gray-50 p-3 rounded-xl font-medium transition">
        <span>
          <router-link to="/sobre">
            ⚙️ Configurações
            </router-link>
        </span>
      </a>
      <a href="#" class="flex items-center space-x-3 text-gray-600 hover:bg-gray-50 p-3 rounded-xl font-medium transition">
        <span>
          <router-link to="/sobre">
            ⚙️ Sobre
            </router-link>
        </span>
      </a>
    </nav>
    
    </div>
    
    <div class="border-t border-gray-100 pt-4 flex items-center space-x-3">
      <div class="h-10 w-10 bg-green-600 text-white rounded-full flex items-center justify-center font-bold">M</div>
      <div>
        <p class="font-semibold text-sm">Marcos Aurélio</p>
        <p class="text-xs text-gray-400">marcos@email.com</p>
      </div>
    </div>
  </aside>

</template>


<style>
/* @import '../estilo.css'; */
</style>
