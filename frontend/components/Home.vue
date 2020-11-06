<template>
<v-container fluid>
    <v-row justify="center" align="center">
        <Button color='#ff3390' @button-click="addCard" text='New Register'/>
    </v-row>
    <!-- TODO: Obter cadastros persistidos -->

    <v-row dense justify="center" align="center">
        <v-col cols="12" sm="4" md="8">
            <Card v-for="(item,index) in cards"
            v-bind:index="index"
            v-bind:key="item.id"
            :data="item"
            @remove-card="removeCard(index)"
            @save-card="saveCard"/>
        </v-col>
    </v-row>
</v-container>
</template>
<script>

import Vue from 'vue';
import Vuetify from 'vuetify';
import Card from '~/components/Card.vue'
import Button from '~/components/Button.vue'
import api from '~/plugins/api'
import axios from 'axios'

Vue.use(Vuetify);

export default {
    components: {
        Card,
        Button
    },
    data() {
        return{
            cards:[]
        }
    },
    created(){
        this.fillCards();
    },
    methods:
    {
        async fillCards()
        {
            // list cards from database
            api.list('api/register/list').then((response) =>
            {
              if(response.status === 200){
                this.cards = response.data;

                // sort cards
                this.sortCards();
              }
            });
        },
        sortCards()
        {
            this.cards.sort((a,b) => {
                return b.datetime > a.datetime
            });

        },
        addCard()
        {
            // add new card into array
            this.cards.push({
                title:'',
                text:'',
                isNew:true,
                datetime: new Date().getTime()
            })


            // sort cards
            this.sortCards();
        },
        // TODO: Create API
        // TODO: Update API
        saveCard(data)
        {
            console.log(data);

            axios.post(data.route,data.card, (response) => {
                console.log(response);
            });


            // if insert get the new id
        },
        // TODO: Delete API
        removeCard(card)
        {
            // remove card from array
            this.cards.splice(card.index,1);

            // remove from database
        }
    }
}
</script>
