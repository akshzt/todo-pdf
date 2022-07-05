<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          icon
          dark
          v-bind="attrs"
          v-on="on"
        >
<v-icon color="primary">mdi-pencil</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Edit Task</span>
        </v-card-title>
        <v-card-text>
          <v-container>
          
                <v-text-field
                  label="Task"
                  v-model="editTask"
                  @keyup.enter="updateTask(id,editTask)"
                ></v-text-field>    
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="updateTask(id,editTask)"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default{
   props: {
    id: Number,
  },
   computed: {
      editTask: {
          get () {
            return this.$store.state.editTask
          },
          set (newValue) {
            this.$store.dispatch('editTask', newValue)
          },
      }
    },
   data: () => ({
    dialog: false,
    newTask: "",
      }),
    methods: {
      updateTask(id, editTask) {
        this.$store.dispatch(`updateTask`,{'id':id,'task':editTask})
        this.dialog=false
      },
    } 
}
</script>