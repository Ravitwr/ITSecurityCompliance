import { defineStore } from 'pinia'
import type { Industry, Region } from '@/interfaces/types'

export const usePreferenceValueStore = defineStore('getPreferenceValueStore', {
  state: () => ({
    valueSelectedIndustry: null as Industry | null,
    valueSelectedRegion: null as Region | null
  }),
  getters: {
    getSelectedIndustry(): Industry | null {
      console.log('ye kya hai bc', this.valueSelectedIndustry)
      return this.valueSelectedIndustry
    },

    getSelectedRegion(): Region | null {
      return this.valueSelectedRegion
    }
  },
  actions: {
    setSelectedIndustry(industry: Industry | null) {
      this.valueSelectedIndustry = industry
      console.log('Here is ', this.valueSelectedIndustry)
    },
    setSelectedRegion(region: Region | null) {
      this.valueSelectedRegion = region
      console.log('Here is ', this.valueSelectedRegion)
    }
  }
})
