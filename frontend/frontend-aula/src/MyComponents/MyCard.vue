<template>

  <div class="card-custom">

    <h2>{{ titulo }}</h2>

    <p>
      {{ texto }}
    </p>

    <button class="btn btn-primary">
      Clique Aqui
    </button>

  </div>

</template>

<script setup>

/* props */
defineProps({
  titulo: String,
  texto: String
})

</script>

<style scoped>

.card-custom{

  background: #1e293b;

  padding: 30px;

  border-radius: 20px;

  color: white;

  text-align: center;

  transition: 0.3s;
}

.card-custom:hover{

  transform: translateY(-10px);
}

h2{
  margin-bottom: 15px;
}

</style>