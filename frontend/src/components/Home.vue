<template>
  <div>
    <p>CSGO Team History</p>
    <!-- <p>Random number from backend: {{ randomNumber }}</p> -->
    <!-- <button @click="getRandom">New random number</button> -->
    <input class ='input' v-model='teamname' placeholder='チーム名を入力'>
    <button @click='getdf(teamname)'>Get Team History</button>
    <p v-for='data in teamhistory'>
      <nobr v-for='tmp in data'>
        <nobr>{{tmp}}  </nobr>
      </nobr>
    </p>

  </div>

</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      teamname: '',
      randomNumber: 0,
      teamhistory: []
    }
  },
  methods: {
    getRandom () {
      const path = 'http://localhost:5000/api/random'
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    },
    getdf (teamname) {
      teamname = this.teamname.replace(/ /g, '_')
      const path = 'http://localhost:5000/api/df/' + teamname
      axios.get(path)
        .then(response => {
          this.teamhistory = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }

  },
  created () {
    this.getRandom()
  }
}
</script>
