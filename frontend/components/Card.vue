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
                datetime:'',
                key:0
            },
            btnProps:{
                text:'Update',
                route: '/register/update'
            }
        }
    },
    mounted(){
        
        this.cardProps.title     = this.data.title;
        this.cardProps.text      = this.data.text;
        this.cardProps.datetime  = this.data.datetime;

        //limit text greater than 100 characters
        this.limitText();

        // check if new card to set the right button properties
        if(this.data.isNew){
            this.btnProps.text  = 'Create',
            this.btnProps.route = '/register/create'

            // show inputs to fill title and text
            this.showInputTitle = true;
            this.showInputText  = true;
        }
    },
    methods:{
        limitText(){
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
    /* height: 200px; */
}
.register-card input{
    color: white;
}
.card-footer{
    flex: 1;
    flex-direction: row-reverse;
}
</style>