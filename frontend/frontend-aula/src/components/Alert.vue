<template>
    <div
        v-if="alertState.show"
        class="position-fixed bottom-0 end-0 p-3"
        style="z-index: 9999;"
    >
        <div
            :class="[
                'alert',
                alertClass,
                'alert-dismissible',
                'fade',
                'show'
            ]"
            role="alert"
        >
            <strong>{{ alertState.title }}</strong>

            <br>

            {{ alertState.message }}

            <button
                type="button"
                class="btn-close"
                @click="close"
            ></button>

        </div>
    </div>
</template>

<script setup>
import { computed } from "vue";
import { useAlert } from "../composables/useAlert";

const { alertState, close } = useAlert();

const alertClass = computed(() => {

    switch (alertState.type) {

        case "success":
            return "alert-success";

        case "danger":
            return "alert-danger";

        case "warning":
            return "alert-warning";

        case "info":
            return "alert-info";

        default:
            return "alert-primary";
    }

});
</script>