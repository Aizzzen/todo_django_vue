<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-form ref="form" lazy-validation class="text-center">
          <v-text-field :counter="64" label="Title" required></v-text-field>

          <v-textarea
            autocomplete="Description"
            label="Description"
          ></v-textarea>

          <v-checkbox label="Is task completed?"></v-checkbox>

          <v-btn color="error" class="mr-4">Clear</v-btn>

          <v-btn color="success" class="mr-4">Add</v-btn>
        </v-form>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <v-list shaped>
          <v-list-item-group color="deep-purple" v-model="selected" multiple>
            <v-list-item v-for="item in todoList" :key="item.id">
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
    selected: [],
    todoList: [],
  }),
  mounted() {
    this.getTodos();
  },
  methods: {
    getTodos() {
      axios
        .get("http://127.0.0.1:8000/api/v1/todo/")
        .then((res) => (this.todoList = res.data));
    },
  },
};
</script>
