<template>
  <div class="about-page">
    <div class="about-card">

      <div class="header">
        <img
          src="@/assets/teste.png"
          alt="Logo"
          class="logo"
        />

        <div>
          <h1>Front-end</h1>
          <p class="version">
            Versão 0.1.0 Alpha
          </p>
        </div>
      </div>

      <hr>

      <section>
        <h2>Sobre</h2>

        <p>
          Ferramenta de teste para web.
        </p>

        <p>
          O objetivo do projeto é fornecer um material para os alunos terem de apoio, no desenvolvimento do projeto.
        </p>
      </section>

      <section>
        <h2>Recursos</h2>

        <ul>
          <li>✔ Banco de dados</li>
          <li>✔ Cadastros interativos</li>
        </ul>
      </section>

      <section>
        <h2>Tecnologias</h2>

        <div class="tags">
          <span>Vue 3</span>
          <span>Vite</span>
          <span>JavaScript</span>
          <span>Node.js</span>
        </div>
      </section>

      <footer>
        <p>© 2026 Aula Front-end</p>
        <p>Desenvolvido por Marcos</p>
      </footer>

    </div>
  </div>
</template>

<style scoped>

.about-page{
    display:flex;
    justify-content:center;
    align-items:flex-start;
    padding:40px;
    background:#f5f5f5;
    min-height:100vh;
}

.about-card{
    width:900px;
    background:white;
    border-radius:12px;
    padding:35px;
    box-shadow:0 5px 20px rgba(0,0,0,.08);
}

.header{
    display:flex;
    gap:20px;
    align-items:center;
}

.logo{
    width:90px;
    height:90px;
    object-fit:contain;
}

h1{
    margin:0;
}

.version{
    color:#777;
}

section{
    margin-top:30px;
}

section h2{
    margin-bottom:10px;
    color:#2c3e50;
}

ul{
    padding-left:20px;
}

li{
    margin:8px 0;
}

.tags{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
}

.tags span{
    background:#42b883;
    color:white;
    padding:8px 15px;
    border-radius:20px;
    font-size:14px;
}

footer{
    margin-top:40px;
    text-align:center;
    color:#888;
}

hr{
    margin:25px 0;
}

</style>