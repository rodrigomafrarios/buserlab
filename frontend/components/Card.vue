<template>
    <v-card class="d-flex flex-column register-card">
        <v-card-title class="headline">
            <v-text-field v-if="showInputTitle" name="card-title" v-model="cardProps.title"></v-text-field>
            <span @click="showInputTitle = true" v-else>{{cardProps.title}}</span>
        </v-card-title>
        <v-tooltip top>
            <template v-slot:activator="{ on }">
                <v-card-text v-on="on" >
                    <v-text-field v-if="showInputText" name="card-text" v-model="cardProps.text"></v-text-field>
                    <span @click="showInputText = true" v-else>{{cardProps.text}}</span>
                </v-card-text>
            </template>
            <span>{{data.text}}</span>
        </v-tooltip>
        <v-spacer />
        <v-card-actions class="card-footer">
            <Button v-if="showInputTitle || showInputText" color='#ff3390' text='Save' @button-click="save" />
            <Button color='#ff3390' text='Remove' @button-click="remove" />
        </v-card-actions>
    </v-card>
</template>
<script>

import Button from '~/components/Button.vue'

export default {
    props:['data'],
    components:{
        Button
    },
    data(){
        return{
            showTooltip:false,
            showInputTitle:false,
            showInputText:false,
            cardProps:{
                title:'',
                text:'',
                created_at:'',
                key: this.$attrs.index
            },
            btnProps:{
                text:'Create',
                route: 'api/register/create/'
            }
        }
    },
    mounted()
    {

      //limit text greater than 100 characters
      this.limitText();

      // set a new card
      if(this.data.isNew){
        this.newCard();
        return false;
      }

      // set a old card
      this.oldCard();

    },
    methods:
    {
      newCard()
      {
        // show inputs to fill title and text
        this.showInputTitle = true;
        this.showInputText  = true;
        this.cardProps.isNew = true;
      },
      oldCard()
      {
        this.btnProps.text  = 'Update',
        this.btnProps.route = 'api/register/update/' + this.data.id

        this.cardProps.id        = this.data.id;
        this.cardProps.title     = this.data.title;
        this.cardProps.text      = this.data.text;
        this.cardProps.created_at  = this.data.created_at;
      },
      limitText()
      {
        if(this.cardProps.text.length > 80){
            this.cardProps.text = this.data.text.substr(0,100) + '...'
        }
      },
      remove()
      {
        // event bus to remove the card itself
        this.$emit('remove-card');
      },
      save(route)
      {
        //in a real case needs to improve the feedback
        if(this.cardProps.title === '' || this.cardProps.text === ''){
          return false;
        }

        // back to span
        this.showInputTitle = false;
        this.showInputText  = false;

        // event bus to save the card
        this.$emit('save-card',{route:this.btnProps.route,card:this.cardProps});
      }
    }
}
</script>
<style scoped>
.register-card{
    margin-top: 15px;
}
.register-card input{
    color: white;
}
.card-footer{
    flex: 1;
    flex-direction: row-reverse;
}
</style>
