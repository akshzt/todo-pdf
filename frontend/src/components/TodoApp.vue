<template>
  <div class="todoApp">
    <div class="header">
      <h1>{{ msg }}</h1>
    </div>
    <div class="todoContainer">
      <CompletedTodos />
      <GetTodo />
      <CurrentTodos />
    </div>
  </div>
</template>

<script>
import GetTodo from './GetTodo.vue';
import CurrentTodos from './CurrentTodos.vue';
import CompletedTodos from './CompletedTodos.vue';

export default {
  name: 'TodoApp',
  components: {
    GetTodo,
    CurrentTodos,
    CompletedTodos
  },
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
