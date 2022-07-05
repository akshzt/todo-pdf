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
      @click="$store.dispatch(`updateDone`,Object.assign(task,{'done':!task.done}))" 
      :class="{'teal darken-4': task.done}" 
      >
        <template v-slot:default>
                  <v-list-item-action>
              <v-checkbox
                :input-value="task.done"
                color="primary"
              ></v-checkbox>
            
            </v-list-item-action>

            <v-list-item-content>
              <v-list-item-title :class="{'text-decoration-line-through' : task.done }">
                {{task.task}}
              </v-list-item-title>
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
    mounted () {
        // axios.get(`/todo`).then(response => (
        // // console.log(response.data)
        // this.list = response.data
        // )).catch(error => console.log(error))
      this.$store.dispatch("getTasks")
    }
  }
</script>
