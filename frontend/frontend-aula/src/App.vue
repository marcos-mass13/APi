<script setup lang='ts'>
  import MyNavBar from './MyComponents/MyNavBar.vue'
</script>

<template>
  <MyNavBar/>
  <div class="container">
    <div class="row">
      <div class="col">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<style>
@import './estilo.css';
</style>