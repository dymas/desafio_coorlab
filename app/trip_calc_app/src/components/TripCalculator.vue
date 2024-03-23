<script setup lang="ts">
import { ref, onBeforeMount } from 'vue'
import IconTruck from './icons/IconTruck.vue'
import IconPrice from './icons/IconPrice.vue'
import IconWarning from './icons/IconWarning.vue'
import IconClock from './icons/IconClock.vue'
import IconMoney from './icons/IconMoney.vue'

type Cities = string[]
type Results = {
  name: string
  type: string
  description: string
  duration: string
  price: string
}[]

const origin = 'http://localhost:3000'
const cities = ref<Cities>()
const destiny = ref('')
const chosen_date = ref('')
const dialog = ref<HTMLDialogElement>()
const result = ref<Results>()

function validate(event: Event) {
  event.preventDefault()
  if (!destiny.value || !chosen_date.value) {
    dialog.value?.showModal()
  } else {
    getResults(destiny.value)
  }
}

function clear() {
  result.value = undefined
}

async function getCities() {
  const endpoint = new URL('/', origin)

  try {
    const data = await fetch(endpoint)
    return (await data.json()) as Cities
  } catch (err) {
    return ['Não retornado.' + err]
  }
}

async function getResults(city: string) {
  const endpoint = new URL(`/city/${city}`, origin)

  try {
    const data = await fetch(endpoint)
    result.value = (await data.json()) as Results
  } catch (err) {
    console.log(err)
  }
}

onBeforeMount(async () => cities.value = await getCities())
</script>

<template>
  <section class="card">
    <dialog ref="dialog" class="modal">
      <div class="dialog-content">
        <IconWarning />
        <h2>Insira os valores para realizar a cotação.</h2>
        <button class="button" @click="dialog?.close()">Fechar</button>
      </div>
    </dialog>
    <div class="header bg-blue">
      <IconTruck />
      <h2>Calculadora de Viagem</h2>
    </div>

    <div class="content">
      <div class="calculator">
        <div class="header">
          <IconPrice />
          <h3>Calcule o valor da viagem</h3>
        </div>

        <form class="calc-area">
          <div class="field">
            <label class="label" for="destiny">Destino</label>
            <select class="dropdown" v-model="destiny" required>
              <option disabled selected value="">Selecione o destino</option>
              <option v-for="(city, index) in cities" :key="index" :value="city">{{ city }}</option>
            </select>
          </div>

          <div class="field">
            <label class="label" for="date">Data</label>
            <input class="dropdown" type="date" v-model="chosen_date" required />
          </div>

          <button class="button" type="submit" @click="validate">Buscar</button>
        </form>
      </div>

      <div v-if="result === undefined" class="results">
        <p>Nenhum dado selecionado.</p>
      </div>

      <div v-if="result !== undefined" class="results">
        <p>Estas são as melhores alternativas de viagem para a data selecionada:</p>

        <div v-for="(item, index) in result" :key="index" class="seat-option">
          <div class="seat">
            <div v-if="item.type === 'confort'" class="icon">
              <IconMoney />
            </div>

            <div v-if="item.type === 'economic'" class="icon">
              <IconClock />
            </div>

            <div class="seat-description">
              <h3>{{ item.name }}</h3>
              <p>{{ item.description }}</p>
              <p>Tempo estimado: {{ item.duration }}</p>
            </div>
          </div>

          <div class="price">
            <h3>Preço</h3>
            <p>{{ item.price }}</p>
          </div>
        </div>

        <button @click="clear" class="button">Limpar</button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.modal::backdrop {
  background-color: rgba(0, 0, 0, 0.2);
}

.modal {
  border: none;
  border-radius: 20px;
  font-family: Arial, Helvetica, sans-serif;
  width: 45vh;
}

.dialog-content {
  margin: 10% auto;
  text-align: center;
  width: 70%;

  h2 {
    color: #444444;
  }
}

.card {
  background-color: #ffffff;
  border-radius: 10px 10px 0 0;
  box-shadow: 2px 2px 7px 1px rgba(0, 0, 0, 0.2);
}

.calculator {
  background-color: #eeeeee;
  border-radius: 10px;
}

.header {
  align-items: center;
  display: flex;
  gap: 15px;
  padding: 10px 20px;
  font-family: Arial, Helvetica, sans-serif;

  img {
    width: 40px;
  }
}

.calc-area {
  display: flex;
  flex-direction: column;
  padding: 25px;
}

.dropdown {
  background-color: #fff;
  border: 1px solid #cecece;
  border-radius: 5px;
  font-family: Arial, Helvetica, sans-serif;
  padding: 15px;
}

.label {
  color: #444444;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 13px;
  font-weight: bolder;
  margin-bottom: 10px;
}

.field {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.bg-blue {
  background-color: #2a3041;
  border-radius: 10px 10px 0 0;
  color: #ffffff;
}

.button {
  align-self: center;
  background-color: #03a8b4;
  border: none;
  border-radius: 5px;
  color: #2a3041;
  cursor: pointer;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bolder;
  margin-top: 20px;
  padding: 10px 60px;
  width: fit-content;
}

.button:active {
  background-color: #00656c;
}

.button:hover {
  background-color: #47bfc8;
}

.results {
  color: #444;
  font-family: Arial, Helvetica, sans-serif;
  padding: 90px 25px;

  p:first-child {
    font-size: 20px;
  }
}

.seat,
.price {
  height: 120px;
}

.seat {
  display: flex;
}

.price {
  align-content: space-evenly;
  display: grid;
  background-color: #eeeeee;
  border-radius: 5px;
  padding-left: 20px;
}

.seat-description {
  align-content: space-evenly;
  display: grid;
  background-color: #eeeeee;
  border-radius: 0 5px 5px 0;
  padding-left: 25px;
  width: 100%;

  h3,
  p {
    margin: 0;
  }
}

.seat-option {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-top: 20px;
  width: 100%;
}

.icon {
  background-color: #03a8b4;
  border-radius: 5px 0 0 5px;
  display: grid;
  padding: 0 20px;
  place-content: center;
  height: 100%;
}

@media (min-width: 1024px) {
  .seat {
    width: 65%;
  }

  .price {
    width: 25%;
  }

  .card {
    margin: 0 5%;
  }

  .calculator {
    margin: 25px;
    padding: 90px 25px;
    width: 35%;
  }

  .results {
    width: 100%;
  }

  .content {
    display: flex;
  }
}

@media (max-width: 1023px) {
  .seat-option {
    flex-direction: column;
  }
}
</style>
