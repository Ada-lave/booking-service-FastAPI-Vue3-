
<template>
  <nav class="py-6 px-8 border-b">
    <div class="mx-auto">
  
      <div class="flex items-center  justify-between">
        <div class="flex space-x-2">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 21v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21m0 0h4.5V3.545M12.75 21h7.5V10.75M2.25 21h1.5m18 0h-18M2.25 9l4.5-1.636M18.75 3l-1.5.545m0 6.205l3 1m1.5.5l-1.5-.5M6.75 7.364V3h-3v18m3-13.636l10.5-3.819" />
          </svg>
  
          <RouterLink class="text-xl" v-bind:to="{name: 'main'}">
            Броним
          </RouterLink>
  
        </div>
  
        
          <div class="flex space-x-2">
            <p class="text-xl">
              Мои брони
            </p>
            <p class="text-xl">
              Выйти
            </p>
          </div>
      
  
      </div>
    </div>
  </nav>
  <main>
      <RouterView />
  </main>
</template>

<script>
import { RouterLink } from 'vue-router'
export default{
    
}
</script>
  