<script setup>

import { defineProps } from 'vue'

const props = defineProps({
    name: {
        type: String,
        required: true
    },
    id: {
        type: String,
        required: true
    },
    label: {
        type: String,
        required: false
    },
    type:{
        type: String,
        required: false,
        default: 'default',
        validator: (value) => {
            return ['cifrar', 'decifraf', 'limpar'].includes(value)
        }
    },
})
</script>

<template>
    <button :id="id" :type="type" class="text-white font-bold py-2 px-4 rounded" :class="type === 'cifrar' ? 'bg-green-500 hover:bg-green-800' : type == 'decifrar' ? 'bg-red-500 hover:bg-red-800' : 'bg-blue-500 hover:bg-blue-800'">
        {{ label }}
    </button>   
</template>