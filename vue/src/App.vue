<script setup>
import { ref }  from 'vue';
import ButtonComponent from './components/ButtonComponent.vue';

//import classe de servico
import CifradorApi from './service';

// declaracao de v-models
const text_normal = ref('');
const text_cifrado = ref('');
const chave = ref('');

// declaracao de funcoes

async function HandleCifrar() {
  // if(String(chave.value).length !== 3) return alert('Chave deve ter 3 digitos')
  const chaveArray = String(chave.value).split('');
  let responseText = '';
  try{
    const response = await CifradorApi.cifrar({
      data: text_normal.value,
      key: chaveArray
    });
    responseText = response.data.cifra;
  } catch(e) {
    responseText = e.response.data.error;
  }
  text_cifrado.value =responseText;
}

async function HandleDecifrar() {
  // if(String(chave.value).length !== 3) return alert('Chave deve ter 3 digitos')
  const chaveArray = String(chave.value).split('');
  let responseText = '';
  try{
  const response = await CifradorApi.decifrar({
    data: text_cifrado.value,
    key: chaveArray
  });
  responseText = response.data.decifra;
} catch(e) {
  responseText = e.response.data.error;
}
  text_normal.value = responseText;
}

function HandleLimpar() {
  text_normal.value = '';
  text_cifrado.value = '';
  chave.value = '';
}
</script>

<template>
  <main class="mt-40 max-w-6xl mx-auto p-10 bg-gray-300 rounded-lg">
    
    <h1 class="text-xl">Cifrador</h1>

    <section class="w-full flex my-4 gap-4">
      <div class="w-1/2">
        <textarea name="text_normal" id="normal" placeholder="Texto a Ser cifrado" v-model="text_normal" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline " rows="10">
          </textarea>
      </div>
      <div class="w-1/2">
        <textarea name="text_cifrado" id="cifrado" placeholder="Texto Cifrado" v-model="text_cifrado" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline " rows="10">
          </textarea>
      </div>
    </section>
    <footer class="grid grid-cols-12 gap-4">
      <ButtonComponent name="btn" id="btn" label="Cifrar" type="cifrar" class="col-span-3" @click="HandleCifrar"/>
      <input name="btn" id="btn" placeholder="Chave de 3 digitos" class="col-span-6 shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline h-10" v-model="chave" type="number" />
      <ButtonComponent name="btn" id="btn" label="Decifrar" type="decifrar" class="col-span-3" @click="HandleDecifrar"/>
      <ButtonComponent name="btn" id="btn" label="Limpar" type="limpar" class="col-span-12" @click="HandleLimpar"/>
    </footer>
  </main>
</template>
