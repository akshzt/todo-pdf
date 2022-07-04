<template>
  <div class="home">
    
    <v-text-field
    v-model="newTaskTitle"
    @click:append=" addTask"
    @keyup.enter="addTask"
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
     v-for="task in list"
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
              <!-- <v-list-item-title :class="{'text-decoration-line-through' : task.done }"> -->
                {{task.task}}
              <!-- </v-list-item-title> -->
            </v-list-item-content>

               <v-list-item-action>
                <EditTaskVue/>
          <!-- <v-btn icon
          @click.stop="popupFunc">
            <v-icon color="primary">mdi-pencil</v-icon>
          </v-btn> -->
        </v-list-item-action>

            <v-list-item-action>
          <v-btn icon
          @click.stop="deleteTask(task.id)">
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
  import EditTaskVue from '@/components/EditTask.vue'
  import axios from 'axios'
import EditTask from '@/components/EditTask.vue'
  export default {
    name: 'Home',
    components: { EditTaskVue, EditTask },
    data() {
      return {
        // dialog: false,
        list: null,
        newTaskTitle:'',
        tasks: [{
          id:1,
          task: "Eat",
          done: false,

        },
        {
          id:2,
          task: "Sleep",
          done: false,

        },
        {
          id:3,
          task: "Code",
          done: false,

        },
        {
          id:4,
          task: "Repeat",
          done: false,

        },
        ]
      }
    },
    methods: {


      popupFunc(){
        console.log(this.list)
        /*Your logic goes here*/
      
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
        // this.tasks = this.tasks.filter(task => task.id !== id)
        axios.delete(`/todo/${id}`).then(response => (console.log(response)))
        .catch(error=> console.log(error))
        this.$router.go()

      }
    },
    mounted () {
        axios.get(`/todo`).then(response => (
        // console.log(response.data)
        this.list = response.data
        )).catch(error => console.log(error))
    }
  }
</script>
