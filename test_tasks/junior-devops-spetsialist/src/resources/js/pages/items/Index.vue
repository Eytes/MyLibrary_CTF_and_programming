<template>
  <div :id="'items'">
    <div :id="key" v-for="(item, key) in items" :key="key">
      <!-- v-on listens to the event specified after the ':' sign. In this case,
      we'll listen to  the 'itemChanged' event and, at the same time, we'll also
      trigger the 'reloadList' event which will be handled in App.vue. In larger
      applications, these events are usually controlled with the state -->
      <list-item :item="item" v-on:itemChanged="$emit('reloadList')" />
    </div>
  </div>
</template>

<script>
import ListItem from "./ListItem.vue";

export default {
  props: ["items"],
  emits: ["reloadList"],
  components: {
    ListItem,
  },
};
</script>