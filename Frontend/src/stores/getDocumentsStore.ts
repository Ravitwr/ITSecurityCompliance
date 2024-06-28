import { defineStore } from 'pinia'
import type { Document } from '@/interfaces/types'
import * as documentRepository from '@/repository/getDocumentRepository'

export const useDocumentsStore = defineStore('getDocumentsStore', {
  state: () => ({
    Documents: [] as Document[]
  }),
  getters: {
    getDocuments(): Document[] {
      return this.Documents
    }
  },
  actions: {
    async fetchDocuments() {
      try {
        const documents = await documentRepository.getDocuments()
        this.Documents = documents
      } catch (error) {
        console.error('Error fetching documents:', error)
      }
    }
  }
})
