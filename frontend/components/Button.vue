<template>
    <div @click="action" class="action-button">
        <v-btn v-if="route" :color="color" nuxt :to="route">
            {{text}}
        </v-btn>
        <v-btn v-else :color="color" nuxt>
            {{text}}
        </v-btn>
    </div>
</template>
<script>
export default {
    props:['color','route','text'],
    methods:{
        action(){
            this.$emit('button-click');
        }
    }
}
</script>
<style scoped>
.action-button{
    margin-left: 10px;
}
</style>