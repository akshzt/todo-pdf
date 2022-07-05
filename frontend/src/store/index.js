
import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        tasks: [],
        newTask: "",
        editTask: "",
    },
    getters: {
        allTasks(state) {
            return state.tasks
        },
        newValue(state) {
            return state.newTask
        }
    },
    actions: {
        getTasks( {commit} ) {
            axios.get('/todo').then(
                response => {console.log(response.data)
                commit("getTasks", response.data)
                }
            ).catch(
                error => console.log(error)
            )
        },
        removeTasks({commit}, id) {
            axios.delete(`/todo/${id}`)
            .then(response=>{console.log("Deleted", response)
                commit("removeTasks", id)})
            .catch(
                error=>{console.log(error)}
            )
        },
        setNewTask({commit}, newValue) {
            commit("setNewTask", newValue)
        },
        addTask({commit}, newTask2) {
            axios.post('/todo', {"task":newTask2})
            .then(response => {
            console.log("added", response)
            commit("addTask", response.data)
            commit("setNewTask", "")}
            )
            .catch(error => {console.log(error)})
        },
        updateTask({commit}, payload) {
            console.log(payload.task, "this is the edit")
            axios.put(`todo/${payload.id}?task=${payload.task}`)
            .then(response=>{
                console.log("updated",response)
                commit("updateTask",payload)
                commit("editTask", "")})
            .catch(error=>console.log(error))
    },
    editTask({commit}, newValue) {
        commit("editTask", newValue)
    },
    updateDone({commit}, payload) {
        axios.put(`todo/${payload.id}/done?done=${payload.done}`)
        .then(response=>{
            console.log('done changed to',response.data.done, response.data)
            commit("updateDone",response.data)
        })
        .catch(error=>console.log(error))

    }
},
    mutations: {
        getTasks (state, todo) {
            state.tasks = todo
        },
        removeTasks(state,id) { 
            state.tasks = state.tasks.filter((todo) => todo.id !== id)},

        setNewTask(state, newValue) {
            state.newTask = newValue
        },
        addTask(state, newVal) {
             state.tasks.unshift(newVal)
        },
        editTask(state, newValue) {
            state.editTask = newValue
        },
        updateTask(state, payload) {
            const index = state.tasks.findIndex(todo => todo.id === payload.id);
            state.tasks.splice(index,1,{'task':payload.task,})
        },
        updateDone(state, payload) {
            const index = state.tasks.findIndex(todo => todo.id === payload.id);
            state.tasks.splice(index,1,payload)
        }
    }
})

export default store;