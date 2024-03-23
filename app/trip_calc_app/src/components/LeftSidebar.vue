<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import IconHamburger from './icons/IconHamburger.vue'

const isOpen = ref(window.innerWidth > 1023 ? true : false)
const handleOpen = () => (isOpen.value = window.innerWidth > 1023 ? true : false)

onMounted(() => window.addEventListener('resize', handleOpen))
onUnmounted(() => window.removeEventListener('resize', handleOpen))

defineProps<{
  menu: {
    icon: string
    route: string
    label: string
  }[]
}>()
</script>

<template>
  <aside class="sidebar">
    <div class="logo">
      <img src="/logo.png" />
    </div>

    <div class="menu">
      <details :open="isOpen">
        <summary role="button" class="hamburguer" :style="{ display: isOpen ? 'none' : '' }">
          <IconHamburger />
          Menu
        </summary>

        <ul>
          <li v-for="(item, index) in menu" :key="index">
            <img :src="item.icon" />
            <a :href="item.route">
              {{ item.label }}
            </a>
          </li>
        </ul>
      </details>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  background-color: #2a3041;
  display: flex;
}

.logo {
  display: flex;
}

.menu {
  font-family: Arial, Helvetica, sans-serif;

  ul {
    list-style: none;
    margin: 0;
    padding: 0;

    li {
      align-items: center;
      display: flex;
      flex-direction: row;
      gap: 10px;
      max-width: 100%;

      img {
        max-width: 30px;
      }

      a {
        color: #ffffff;
        font-weight: bold;
        text-decoration: none;
      }
    }
  }
}

.hamburguer {
  align-items: center;
  color: white;
  cursor: pointer;
  display: flex;
  font-weight: bold;
  gap: 10px;
  list-style: none;
}

@media (min-width: 1024px) {
  .sidebar {
    align-items: baseline;
    flex-direction: column;
    height: 100vh;
    position: fixed;
    width: 20vmax;
  }

  .logo {
    align-items: center;
    justify-content: center;
    padding: 10% 0;
    width: 100%;

    img {
      max-width: 200px;
      height: 100%;
    }
  }

  .menu {
    width: 100%;

    ul {
      li {
        margin-top: 10%;
        padding: 0 10%;
      }
    }
  }
}

@media (max-width: 1023px) {
  .sidebar {
    flex-direction: column;
    width: 100vw;
  }

  .logo {
    align-items: center;
    justify-content: center;
    margin: 3% 0;

    img {
      height: 50%;
      max-width: 250px;
      width: 100%;
    }
  }

  .menu {
    ul {
      li {
        margin: 3% 5%;
      }
    }
  }

  .hamburguer {
    margin: 3% 5%;
  }
}
</style>
