import { BASE_URL } from '@/interfaces/consts'
import type { evidenceRequestType, evidenceResponseType } from '@/interfaces/types'
import axios from 'axios'

export async function getTestCaseResultRepository(
  requestParam: evidenceRequestType[]
): Promise<evidenceResponseType[]> {
  try {
    const endpoint = 'verify_evidence'
    const response = await axios.post(`${BASE_URL}${endpoint}`, requestParam)
    const data = response.data
    if (data.status === 'success') {
      console.log(data.result)
      return data.result
    } else {
      throw new Error(data.errors || 'Failed to fetch test case summary results')
    }
  } catch (error) {
    throw new Error('Connection to server failed')
  }
}

// export async function getTestCaseResultRepository(
//   requestParam: evidenceTableType[] //evidenceRequestType[]
// ): Promise<evidenceResponseType[]> {
//   const mockResult = []
//   for (let i = 0; i < requestParam.length; i++) {
//     mockResult.push({
//       id: requestParam[i].id,
//       result: 'Pass',
//       summary: 'Hey here is the summary'
//     })
//   }
//   return Promise.resolve(mockResult)
// }
