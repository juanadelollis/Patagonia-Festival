<template>
  <div class="Counter">
    <button @click="decrement" :disabled="counter.value === 0" class="button-counter">-</button>
    <p id="counter-text">{{ counterComputed }}</p>
    <button @click="increment" class="button-counter">+</button>
  </div>
</template>

<script>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';

export default {
  name: 'CounterComponent',
  props: {
    counterName: {
      type: String,
      default: 'Counter',
    },
  },
  setup(props, { emit }) {
    const counter = ref(0);

    const counterComputed = computed(() => {
      return `${counter.value}`;
    });

    const increment = () => {
      counter.value++;
      emitCounterChangeEvent();
    };

    const decrement = () => {
      if (counter.value > 0) {
        counter.value--;
        emitCounterChangeEvent();
      }
    };

    // Emitir el evento cuando el componente se monta y desmonta
    onMounted(() => {
      emitCounterChangeEvent();
    });

    onBeforeUnmount(() => {
      emitCounterChangeEvent();
    });

    function emitCounterChangeEvent() {
      emit('counter-change', { name: props.counterName, value: counter.value });
    }

    return {
      counter,
      increment,
      decrement,
      counterComputed,
    };
  },
};
</script>
  
  <style>
  .Counter{
    display:flex;
    flex-direction: row;
    width: 210px;
    height: 70px;
  }

  .button-counter{
    width: 70px;
    height: 60px;
    font-size: 40px;
    font-weight: 700;
    margin:0px;
    padding: 0px;
    align-items: center;
    border: solid black 2px;
  }

  #counter-text{
    background-color: lightgray ;
    margin: 0px;
    padding: 0px;
    height:60px;
    border: solid black 2px;
    font-size: 40px;
    display: flex;
    justify-content: center;
    align-content: center;
  }
</style>
  