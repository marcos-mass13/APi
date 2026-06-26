<script setup lang='ts'>
  import MyNavBar from './MyComponents/MyNavBar.vue'
</script>

<template>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
  <div class="min-h-screen bg-gray-50 flex font-sans text-gray-800">
    <MyNavBar/>
    <div class="container">
      <div class="row">
        <div class="col">
          <router-view/>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import './estilo.css';
</style>