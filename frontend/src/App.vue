<script setup>
</script>

<template>
  
  <nav>
    <router-link to="/">Login</router-link>
    <router-link to="/home">Home</router-link>
  </nav>

  <main>
    <router-view />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}
</style>