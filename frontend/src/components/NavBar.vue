<template>
  <div class="navbar-div">
      <a href="#"><img src="../assets/images/Patagonia_Fest_Logo_Blanco.png" alt="logo" /></a>
      <nav class="nav-bar" id="nav">
                <ul class="ul-nav">
                  <li>
                    <a href="#">Line Up</a>
                  </li>
                  <li>
                    <a href="#">Informacion</a>
                  </li>
                  <li>
                    <a href="#">Tickets</a>
                  </li> 
                  <li>
                    <a href="#">Mi Cuenta</a>
                  </li>
                </ul>
      </nav>
      <svg v-show="showMenuButton" v-on:click="toggleNav" id="menu" class="menu-icon" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M0.714286 5.15625H19.2857C19.6802 5.15625 20 4.87645 20 4.53125V2.96875C20 2.62355 19.6802 2.34375 19.2857 2.34375H0.714286C0.319777 2.34375 0 2.62355 0 2.96875V4.53125C0 4.87645 0.319777 5.15625 0.714286 5.15625ZM0.714286 11.4062H19.2857C19.6802 11.4062 20 11.1264 20 10.7812V9.21875C20 8.87355 19.6802 8.59375 19.2857 8.59375H0.714286C0.319777 8.59375 0 8.87355 0 9.21875V10.7812C0 11.1264 0.319777 11.4062 0.714286 11.4062ZM0.714286 17.6562H19.2857C19.6802 17.6562 20 17.3764 20 17.0312V15.4688C20 15.1236 19.6802 14.8438 19.2857 14.8438H0.714286C0.319777 14.8438 0 15.1236 0 15.4688V17.0312C0 17.3764 0.319777 17.6562 0.714286 17.6562Z"
          fill="white"/>
      </svg>
  </div>
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
.navbar-div{
  background-color: #006633;
  display: flex;
  flex-direction: row;
}

.navbar-div a{
  width: 20%;
}

.navbar-div img{
  width: 100%;
}
.nav-bar{
  width: 80%;
}
.ul-nav{
    display: flex;
    flex-direction: row;
    font-size: 1.3rem;
    list-style: none;
}

.ul-nav li{
    padding: 5% 0;
    padding-left: 8%;
    color: white;
    text-decoration: none;
}

.a{
  text-decoration: none;
  color: white;
}
</style>