<template>
 <VideoHero/>


</template>

<script>
import VideoHero from './VideoHero.vue'
export default {
    data() {
        return {
            articles: [],
        };
    },
    methods: {
        getArticles() {
            fetch('http://localhost:5000/articles', {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(resp => resp.json())
                .then(data => {
                let articulos = data.articles;
                console.log(articulos);
                articulos.forEach(articulo => { this.articles.push(articulo); });
                //this.articles.push(...data)
            })
                .catch(error => {
                console.log(error);
            });
        }
    },
    //este se llama una vez creado el objeto, ver lifecicle hooks
    created() {
        this.getArticles();
    },
    components: { VideoHero }
}
</script>

<style>

</style>