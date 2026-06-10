<script setup lang='ts'>
import {BApp} from 'bootstrap-vue-next'
</script>

<template>

<nav class="navbar bg-dark border-bottom border-body navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <!-- <a class="nav-link active" aria-current="page" href="#">Home</a> -->
           <router-link class="nav-link active" aria-current="page"  to="/">Home</router-link>
        </li>
        <li class="nav-item">
          <!-- <a class="nav-link" href="#">Features</a> -->

           <router-link class="nav-link" to="/page">Page</router-link>

        </li>
        <li class="nav-item">
          <!-- <a class="nav-link" href="#">Features</a> -->
           <router-link class="nav-link" to="/sobre">Sobre</router-link>
        </li>
        <li class="nav-item">
          <!-- <a class="nav-link" href="#">Features</a> -->
           <router-link class="nav-link" to="/login">Sobre</router-link>
        </li>
      
      </ul>
    </div>
  </div>
</nav>

</template>


<style>
@import '../estilo.css';
</style>
