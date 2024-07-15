import { createStore } from "vuex";

export default createStore({
  state: {
    data: {
      reTopic: [],
      reTopicM: [],
      bugM: [],
      bug: [],
      exception: [],
      error: [],
      exceptionM: [],
      errorM: [],
      topic: [],
      questionM: [],
      answerM: [],
      viewM: [],
    },
  },
  getters: {},
  mutations: {
    setData(state, payload) {
      console.log("payload", payload.field);
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-ignore
      state.data[payload.field] = payload.value;
    },
  },
  actions: {},
  modules: {},
});
