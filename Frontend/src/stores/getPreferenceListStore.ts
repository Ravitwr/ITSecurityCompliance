import { defineStore } from 'pinia'

export const useGetPreferenceListStore = defineStore('getPreferenceListStore', {
  state: () => ({
    IndustryList: [
      { IndustryID: 1, IndustryName: 'Energy' },
      { IndustryID: 2, IndustryName: 'Cross-Industry' },
      { IndustryID: 3, IndustryName: 'Financial Services' }
    ],

    RegionList: [
      { RegionID: 1, RegionName: 'North America' },
      { RegionID: 2, RegionName: 'APAC' },
      { RegionID: 3, RegionName: 'Standard' }
    ]
  })
})
