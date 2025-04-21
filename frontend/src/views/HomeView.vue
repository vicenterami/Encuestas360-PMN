<template>
  <div class="home-container">
    <header>
      <h1>Encuestas360</h1>
      <p>Hola, Pepe Pepito</p>
    </header>

    <main>
      <section>
        <h2>Nueva Encuesta</h2>
        <button>Comenzar Encuesta</button>
      </section>

      <section>
        <h2>Historial</h2>
        <button>Ver Historial</button>
      </section>

      <section>
        <h2>Soporte</h2>
        <button>Reportar Problema</button>
      </section>
    </main>
  </div>
</template>

<style scoped>
.home-container {
  padding: 1rem;
  max-width: 800px;
  margin: auto;
}

header {
  background-color: #0077cc;
  color: white;
  padding: 1rem;
  border-radius: 10px;
  margin-bottom: 2rem;
}

main section {
  background: white;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 1rem;
}

button {
  margin-top: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: #0077cc;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
