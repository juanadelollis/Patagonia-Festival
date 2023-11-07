<template>
    <footer>
            <div class="footer--menu">
                <img src="../assets/images/Patagonia_Fest_Logo_Blanco.png" alt="">
                <div class="footer--menu--list">
                    <ul>
                        <li>Tickets</li>
                        <li>Line Up</li>
                        <li>Mi Cuenta</li>
                    </ul>
                </div>
            </div>
            <p>Grupo #2 Andres, Juana, Milagros</p>
        </footer>
</template>

<script>
export default {

}
</script>

<style>
*{
    padding: 0;
    margin: 0;
}

.footer--menu{
    background-color: #006633;
    display: flex;
    align-items: center;
    font-size: 1.2rem;
    color: white;
}

footer p {
    display: flex;
    justify-content: center;
}

footer img{
    height: 35%;
    width: 60%;
}

footer li{
    list-style-type: none;
    }

footer ul{
    padding: 5px;
}
</style>