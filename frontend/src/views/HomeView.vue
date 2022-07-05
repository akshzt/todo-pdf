<template>
  <div class="home">
    
    <v-text-field
    v-model="newTaskTitle"
    
    @click:append="$store.dispatch(`addTask`, $store.getters.newValue)"
    @keyup.enter="$store.dispatch(`addTask`, $store.getters.newValue)"

    class="pa-3"
    outlined
    label="Add task"
    append-icon="mdi-plus"
    hide-details
    clearable
    >

    </v-text-field>
      <v-list class="pt-0"
        flat
    >
 
    <div
     v-for="task in $store.getters.allTasks"
        :key="task.id">
      <v-list-item  
      >
        <template v-slot:default>
                  <v-list-item-action>
              <v-checkbox
                
                color="primary"
              ></v-checkbox>
            
            </v-list-item-action>

            <v-list-item-content>
                {{task.task}}
            </v-list-item-content>

               <v-list-item-action>
                <EditTaskVue :id="task.id"/>
        </v-list-item-action>

            <v-list-item-action>
          <v-btn icon
          @click.stop="$store.dispatch(`removeTasks`,task.id)">
            <v-icon color="primary">mdi-delete</v-icon>
          </v-btn>
        </v-list-item-action>

      

          </template>
        </v-list-item>
        <v-divider></v-divider>
    </div>

     
    </v-list>
      

      </div>
</template>

<script>
  import EditTaskVue from '../components/EditTask.vue'
  import axios from 'axios'
  export default {
    name: 'HomeView',
    components: { EditTaskVue },
    computed: {
      newTaskTitle: {
          get () {
            return this.$store.state.newTask
          },
          set (newValue) {
            this.$store.dispatch('setNewTask', newValue)
          },
      }
    },
    data() {
      return {
        list: null,
      }
    },
    methods: {
      popupFunc(){
        console.log(this.list)
      },
      addTask(){
        let newTask = {
          task: this.newTaskTitle,
        } 

        axios.post(`/todo`,newTask).then(response => (console.log(response)))
        .catch(error=>console.log(error))
        this.newTaskTitle=""
        this.$router.go()
      },
      doneTask(id){
        let task = this.tasks.filter(task=> task.id === id)[0]
        task.done = !task.done
      },
      deleteTask(id){
        axios.delete(`/todo/${id}`).then(response => (console.log(response)))
        .catch(error=> console.log(error))
        this.$router.go()
      }
    },
    mounted () {
      this.$store.dispatch("getTasks")
    }
  }
</script>
