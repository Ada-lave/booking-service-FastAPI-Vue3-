<template>
    <div class="flex items-center justify-center h-screen">
        <div class="w-1/4 rounded">

            <div class="flex space-x-2 justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 21v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21m0 0h4.5V3.545M12.75 21h7.5V10.75M2.25 21h1.5m18 0h-18M2.25 9l4.5-1.636M18.75 3l-1.5.545m0 6.205l3 1m1.5.5l-1.5-.5M6.75 7.364V3h-3v18m3-13.636l10.5-3.819" />
                </svg>
                <p class="text-xl font-bold">
                    Броним
                </p>
            </div>
            <form class="space-y-6">
                <div>
                    <label>Почта</label><br>
                    <input type="email" placeholder="Ваша почта"
                    class="mt-2
                    w-full
                    px-8
                    py-2
                    border
                    rounded">
                </div>

                <div>
                    <label>Пароль</label><br>
                    <input type="password" placeholder="Ваш пароль"
                    class="mt-2
                    w-full
                    px-8
                    py-2
                    border-b border-transparent rounded">
                </div>
                <div>
                    <label>Повторите пароль</label><br>
                    <input type="password" placeholder="Ваш пароль"
                    class="mt-2
                    w-full
                    px-8
                    py-2
                    border
                    border-gray-200
                    rounded">
                </div>
            </form>
            
        </div>
    </div>
    

</template>

<script>

export default {
    mounted(){
        console.log('hii')
    }
}

</script>