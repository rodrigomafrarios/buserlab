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
        fillCards()
        {
          // list cards from database
          api.list('api/register/list/').then((response) =>
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
              return new Date(b.created_at).getTime() > new Date(a.created_at).getTime()
          });

        },
        // add new card into array
        addCard()
        {
          this.cards.push({
              title:'',
              text:'',
              isNew:true,
              created_at: new Date().getTime()
          })

          // sort cards
          this.sortCards();
        },
        saveCard(data)
        {
          // is a brand new card?
          if(data.card.isNew){
            this.insert(data);
            return false;
          }

          // just update
          this.update(data);
        },
        insert(data)
        {
          api.create(data.route,data.card).then((response) =>
          {
            // update card array
            if(response.status === 200){
              this.afterSave(data,response.data)
            }
          });
        },
        update(data)
        {
          api.update(data.route,data.card).then((response) =>
          {
            // update card array
            if(response.status === 200){
              this.afterSave(data,response.data)
            }
          });
        },
        afterSave(data,response)
        {
          this.cards[data.card.key].created_at = response.created_at;
          this.cards[data.card.key].title = response.title;
          this.cards[data.card.key].text = response.text;

          // new register already in database, so remove flag
          if(this.cards[data.card.key].isNew){
            this.cards[data.card.key].id = response.id;
            delete this.cards[data.card.key].isNew;
          }

          this.sortCards();
        },
        removeCard(index)
        {
          if(!this.cards[index].id){
            this.cards.splice(index,1);
            return false;
          }

          api.remove('api/register/remove/' + this.cards[index].id).then((response) => {
            if(response.status === 200){
              // remove card from array
              this.cards.splice(index,1);
            }
          })
        }
    }
}
</script>
