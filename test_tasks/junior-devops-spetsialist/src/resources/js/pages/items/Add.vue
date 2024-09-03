<template>
  <!-- '!!' will coerce value to respective boolean -->
  <button class="btn btn-success" :disabled="!item.name" @click="addItem()">
    <font-awesome-icon icon="plus-square" />
  </button>

  <input
    v-model="item.name"
    class="form-control"
    placeholder="Задача"
    aria-label="Задача"
    type="text"
  />
</template>

<script>
export default {
  data: function () {
    return {
      item: {
        name: "",
      },
    };
  },
  emits: ["reloadList"],
  methods: {
    addItem() {
      if (this.item.name == "") {
        return;
      }

      axios
        .post("/api/item", {
          item: this.item,
        })
        .then((response) => {
          if (response.status == 201) {
            this.item.name = "";
            this.$emit("reloadList");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
