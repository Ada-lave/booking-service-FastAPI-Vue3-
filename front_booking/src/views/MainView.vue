<template>
    <div>
        <div class="flex justify-center">
            <div class="p-6">
                
                <form method="post" v-on:submit.prevent="">
                    <div class="p-6 flex space-x-2 items-center ml-24">
                    <div>
                        
                        <input type="text"
                        class="
                        w-[325px]
                        h-10
                        rounded-full
                        border-2
                        border-yellow-500
                        pl-4">
                    </div>
                    <p>С</p>
                    <div>

                        <input type="text"
                        class="
                        w-[80px]
                        h-10
                        rounded-full
                        border-2
                        border-yellow-500">
                    </div>
                    <p>По</p>
                    <div>
                        
                        <input type="text"
                        class="
                        w-[80px]
                        h-10
                        rounded-full
                        border-2
                        border-yellow-500">
                    </div>
                    <button type="submit"
                    class="
                    py-2
                    px-8
                    rounded-full
                    bg-yellow-500">Найти</button>
                    </div>
                </form>
                <div>
                    
                        <div class="h-auto w-[900px] shadow flex my-4">
                           <div class="space-y-2 w-4/5 p-2 word-wrap break-words">
                            <p>
                                Name
                            </p>
                            <p class="flex">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" />
                                <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" />
                                </svg>
                                Location
                            </p>
                            <p>
                                Services
                            </p>
                            <p>
                                Rooms avalible
                            </p>
                           </div>
                           <div class="p-2 space-y-4 flex flex-col justify-center mx-auto">
                                <div class="text-center">
                                    <div class="flex space-x-2 items-center justify-center">
                                        <p>от</p>
                                        <p class="text-3xl font-bold">25 500₽</p>
                                    </div>
                                    
                                    
                                    <p>за n ночей</p>
                                </div>
                                <div class="mx-auto">
                                    <button type="submit"
                                    class="
                                    py-2
                                    px-8
                                    rounded-full
                                    bg-yellow-500">Найти</button>
                                </div>
                           </div>
                        </div>
                    
                </div>
            </div>
        </div>
    </div>
</template>