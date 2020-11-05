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

Vue.use(Vuetify);
import Card from '~/components/Card.vue'
import Button from '~/components/Button.vue'

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
    mounted(){
        this.fillCards();
    },
    methods:
    {
        fillCards()
        {
            // list cards from database

            this.cards = [
                {
                    id: 1,
                    title:'1ª Frase efeito',
                    text:'Tudo é tudo e nada é nada',
                    datetime: new Date('2020-03-01').getTime()
                },
                {
                    id: 2,
                    title:'2ª Frase efeito',
                    text:'Everybody has a plan until the first punch in the face',
                    datetime: new Date('2020-05-01').getTime()
                },
                {
                    id: 3,
                    title:'3ª Frase efeito',
                    text:'Não se trata de bater duro. Se trata de quanto você aguenta apanhar e seguir em frente',
                    datetime: new Date('2020-05-02').getTime()
                },
                {
                    id: 4,
                    title:'4ª Frase efeito',
                    text:'É preciso escolher um caminho que não tenha fim, mas, ainda assim, caminhar sempre na expectativa de encontrá-lo.',
                    datetime: new Date('2020-07-21').getTime()
                },
                {
                    id: 5,
                    title:'5ª Frase efeito',
                    text:'O futuro é incerto e o fim está sempre perto!',
                    datetime: new Date('2020-09-21').getTime()
                },
                {
                    id: 6,
                    title:'6ª Frase efeito',
                    text:'O importante não é vencer todos os dias, mas lutar sempre.',
                    datetime: new Date('2019-07-21').getTime()
                }
            ]


            // sort cards
            this.sortCards();
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