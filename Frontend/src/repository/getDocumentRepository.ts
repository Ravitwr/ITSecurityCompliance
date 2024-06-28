import axios from 'axios'
import type { Document, getDocumentApiResponse, Industry, Region } from '@/interfaces/types'
import { usePreferenceValueStore } from '@/stores/getPreferenceValueStore'
import { BASE_URL } from '@/interfaces/consts'
// const documentsMockAPI = {
//   status: 'Success',
//   errors: null,
//   result: {
//     Documents: [
//       {
//         DocumentID: 1,
//         DocumentName: 'Compliance Report 2022'
//       },
//       {
//         DocumentID: 2,
//         DocumentName: 'Compliance Report 2023'
//       }
//     ]
//   }
// }
// Real function
export async function getDocuments(): Promise<Document[]> {
  try {
    // Define endpoint
    const endpoint = 'documents/filtered'

    // Get request parameters from store's getter functions
    const preferences = usePreferenceValueStore()
    const industryObj: Industry | null = preferences.getSelectedIndustry
    const regionObj: Region | null = preferences.getSelectedRegion

    // Construct request parameters object
    const requestParam = {
      industry: industryObj || null,
      region: regionObj || null
    }
    const response = await axios.get<getDocumentApiResponse>(`${BASE_URL}/${endpoint}`, {
      params: requestParam
    })
    const data = response.data
    // Assuming response is an array of Documents
    return data.result.Documents // Make sure to navigate to the correct property that contains the array of documents
  } catch (error) {
    console.error('An error occurred while fetching documents:', error)
    // Handle error appropriately, possibly re-throw or return an empty array or special error value
    throw error
  }
}

// Mock Function
// export function getDocuments(): Promise<Document[]> {
//   const documents = documentsMockAPI.result.Documents
//   return Promise.resolve(documents)
// }
