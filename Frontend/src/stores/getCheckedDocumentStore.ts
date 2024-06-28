import { defineStore } from 'pinia'

export const useCheckedDocumentStore = defineStore('getCheckedDocumentStore', {
  state: () => ({
    valueCheckedDocument: null as String[] | null
  }),
  getters: {
    getCheckedDocument(): String[] | null {
      return this.valueCheckedDocument
    }
  },
  actions: {
    setCheckedDocument(checkedDocument: String[] | null) {
      this.valueCheckedDocument = checkedDocument
      console.log('Here is ', this.valueCheckedDocument)
    }
  }
})
