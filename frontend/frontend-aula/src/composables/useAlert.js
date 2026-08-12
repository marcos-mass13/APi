import { reactive } from "vue";

export const alertState = reactive({
  show: false,
  title: "",
  message: "",
  type: "info",
});

export function useAlert() {

  function open(title, message, type = "info") {
    alertState.show = true;
    alertState.title = title;
    alertState.message = message;
    alertState.type = type;
  }

  function close() {
    alertState.show = false;
  }

  return {
    alertState,
    open,
    close
  };
  console.log("open");
  
}