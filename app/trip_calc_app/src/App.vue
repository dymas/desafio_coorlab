<script setup lang="ts">
import LeftSidebar from './components/LeftSidebar.vue'
import NavBar from './components/NavBar.vue'
import TripCalculator from './components/TripCalculator.vue'
</script>

<template>
  <div id="container">
    <LeftSidebar
      :menu="[
        {
          icon: './icons/calculator.svg',
          route: '/',
          label: 'Calculadora de Viagem'
        }
      ]"
    />

    <main class="main">
      <NavBar />
      <TripCalculator />
    </main>
  </div>
</template>

<style scoped>
.main {
  background-color: #eeeeee;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  gap: 5vh;
}

@media (min-width: 1024px) {
  .main {
    margin-left: 20vmax;
    min-height: 100vh;
  }

  #container {
    display: flex;
    flex-direction: row;
  }
}

@media (max-width: 1023px) {
  .main {
    min-height: 82vh;
  }
}
</style>
