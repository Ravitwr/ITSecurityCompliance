import type { ChatRequestParam, responseTableType } from '@/interfaces/types'
import axios from 'axios'
import { BASE_URL } from '@/interfaces/consts'

export async function getTestCaseResults(
  requestParam: ChatRequestParam
): Promise<responseTableType[]> {
  const endpoint = 'test_cases_query'
  try {
    const response = await axios.post(`${BASE_URL}${endpoint}`, requestParam)
    const data = response.data
    console.log(response.data)
    if (data.status === 'success') {
      return data.result.response
    } else {
      throw new Error(data.errors || 'Failed to fetch test case summary results')
    }
  } catch (error) {
    throw new Error('Connection to server failed')
  }
}

// export async function getTestCaseResults(
//   requestParam: ChatRequestParam
// ): Promise<responseTableType> {
//   console.log(requestParam)
//   if (requestParam.query == 'Hello') {
//     return Promise.resolve({
//       id: 1,
//       control_family: 'Access Control',
//       domain: '1',
//       sub_domain: '2',
//       control_description: 'rfwf',
//       test_procedure: `1. Inquiresystems`,
//       accepted_evidence: 'vfssffssf'
//     })
//   } else {
//     return Promise.resolve({
//       id: 2,
//       control_family: 'Access Control 2',
//       domain: 'something',
//       sub_domain: 'else',
//       control_description: 'How to do',
//       test_procedure: `1. Inquiresystems`,
//       accepted_evidence: 'vfssffssf'
//     })
//   }
// }
