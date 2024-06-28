export interface Chat {
  message: string
  by: string
}

export interface Industry {
  IndustryID: number
  IndustryName: string
}

export interface Region {
  RegionID: number
  RegionName: string
}

export interface Document {
  DocumentID: number
  DocumentName: string
}

export interface getDocumentRequestParam {
  industry: string | null
  region: string | null
}

export interface getDocumentApiResponse {
  status: string
  errors: null | string // Assuming errors can be an array of strings or null
  result: {
    Documents: Document[] // Assuming Documents is an array of Document objects
  }
}

export interface ChatRequestParam {
  doc_list: string[]
  query: string
}

export interface responseTableType {
  id: number
  control_family: string
  domain: string
  sub_domain: string
  control_description: string
  test_procedure: string
  accepted_evidence: string
}

export interface evidenceTableType {
  id: number
  name: string | null
  description: string | null
  evidence: string | null
  box: boolean
  file: File | null
  result: string | null
  summary: string | null
}

export interface evidenceResponseType {
  id: number
  result: string
  summary: string
}

export interface evidenceRequestType {
  id: number
  name: string | null
  description: string | null
  evidence: string | null
  box: boolean
  filename: string | null
  result: string | null
  summary: string | null
}
// export interface CheckedDocumentType {

// }
