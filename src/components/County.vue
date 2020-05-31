<template>
    <h1></h1>
</template>

<script>
import getByID from "./../serverTwo.js"
export default {
    name: "County",
    data: () => ({
        info: null
    }),
    created: () => {
        getByID(1001).then(e => console.log(e))
    }
}
</script>