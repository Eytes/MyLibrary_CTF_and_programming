<template>
  <div class="text-center d-flex align-items-center">
    <input type="checkbox" v-model="item.completed" @change="updateCheck()" />
    <span
      :class="[
        item.completed ? 'text-decoration-line-through text-muted' : '',
        'ms-3',
      ]"
      >{{ item.name }}
    </span>
    <button @click="removeItem()" class="btn-trash">
      <font-awesome-icon icon="trash" />
    </button>
  </div>
</template>

<script>
export default {
  props: ["item"],
  emits: ["itemChanged"],
  methods: {
    updateCheck() {
      axios
        .put(`api/item/${this.item.id}`, {
          item: this.item,
        })
        .then((response) => {
          if (response.status == 200) {
            /**
             * $emit is a Vue function that allows us to trigger an event.
             * In this case, the component 'list-item' of the 'Index' page
             * will listen to the emitted event here.
             */
            this.$emit("itemChanged");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    removeItem() {
      axios
        .delete(`api/item/${this.item.id}`)
        .then((response) => {
          if (response.status == 200) {
            /**
             * $emit is a Vue function that allows us to trigger an event.
             * In this case, the component 'list-item' of the 'Index' page
             * will listen to the emitted event here.
             */
            this.$emit("itemChanged");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.btn-trash {
  border: none;
  color: red;
  outline: none;
}
</style>