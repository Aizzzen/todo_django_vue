<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-form ref="form" lazy-validation class="text-center">
          <v-text-field
            v-model="newTodo.title"
            :counter="64"
            :rules="newTodo.titleRules"
            label="Title"
            required
          ></v-text-field>

          <v-textarea
            v-model="newTodo.description"
            autocomplete="Description"
            label="Description"
          ></v-textarea>

          <v-checkbox
            v-model="newTodo.is_complete"
            label="Is task completed?"
          ></v-checkbox>

          <v-btn color="error" class="mr-4" @click="reset">Clear</v-btn>

          <v-btn
            color="success"
            class="mr-4"
            :disabled="!newTodo.title"
            @click="add"
            >Add</v-btn
          >
        </v-form>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" v-if="todoList.length">
        <h3>List:</h3>
        <v-list>
          <v-list-item-group color="deep-purple" v-model="selected" multiple>
            <v-list-item
              v-for="item in todoList"
              :key="item.id"
              @click="updateStatus(item)"
            >
              <v-list-item-icon>
                {{ item.id }}
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  <strong>{{ item.title }}</strong>
                </v-list-item-title>
                <v-list-item-subtitle>
                  {{ item.description }}
                </v-list-item-subtitle>
              </v-list-item-content>
              <v-list-item-action>
                <v-checkbox
                  :input-value="item.is_complete"
                  color="deep-purple"
                ></v-checkbox>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "TodoComponent",
  data: () => ({
    newTodo: {
      title: "",
      description: "",
      titleRules: [
        (v) => !!v || "Title is required",
        (v) => (v && v.length <= 64) || "Title must ne less than 64 characters",
      ],
      is_complete: false,
      user: 1,
    },
    selected: [],
    todoList: [],
  }),
  mounted() {
    this.getTodos();
  },
  methods: {
    getTodos() {
      axios
        .get("http://localhost:8000/api/v1/todo/?ordering=is_complete")
        .then((res) => {
          this.todoList = res.data;
          res.data.forEach((el, i) => {
            if (!el.is_complete) this.selected.push(i);
          });
        });
    },
    reset() {
      this.$refs.form.rest();
    },
    add() {
      let data = this.newTodo;
      axios.post("http://localhost:8000/api/v1/todo/", data).then((res) => {
        console.log(res);
        this.getTodos();
      });
    },
    updateStatus(item) {
      item.is_complete = !item.is_complete;
      let data = { is_complete: item.is_complete };
      axios
        .patch(`http://localhost:8000/api/v1/todo/${item.id}/`, data)
        .then((res) => {
          console.log(res);
          this.getTodos();
        });
    },
  },
};
</script>
