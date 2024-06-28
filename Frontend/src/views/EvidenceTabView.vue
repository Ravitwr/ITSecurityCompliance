<template>
  <div class="w-full">
    <!-- heading -->
    <div class="w-full p-2 font-bold text-lg">Evidence Analysis</div>
    <p class="px-2">
      Following requires you to select the required control and upload the corresponding evidence
      document. Alternatively you can submit a list of documents in the csv template and request the
      analysis
    </p>

    <!-- buttons -->
    <div class="flex py-4 gap-x-12">
      <div class="w-fit rounded-lg border bg-gradient-to-r from-purple-800 to-purple-600 text-white p-2">
        <a href="'/src/assets/sample.xlsx" download="sample.xlsx">
          <button>Download Template</button>
        </a>
      </div>
      <div class="w-fit rounded-lg border bg-gradient-to-r from-purple-800 to-purple-600 text-white p-2">
        <input type="file" @change="uploadCsv" placeholder="Upload Template" />
      </div>
    </div>

    <!-- table -->
    <div class="mb-2 w-full" :class="props.sideBarVisible ? 'max-w-[914px]' : 'max-w-[1200px]'"
      v-if="tableDataSource.length > 0">
      <a-table :columns="columns" :data-source="tableDataSource" :scroll="{ x: 1500, y: 400 }">
        <template #bodyCell="{ column, record }">
          <div v-if="column.key === 'checkbox'">
            <input type="checkbox" v-model="record.box" />
          </div>
          <template v-if="column.key === 'file'">
            <button v-if="record.box" class="rounded-md p-2">
              <input type="file" @change="uploadPdf($event, record)" placeholder="Upload Template" />
              Upload PDF
            </button>
          </template>
        </template>
      </a-table>
      <div class="flex justify-center">
        <a-button type="primary" class="bg-gradient-to-r from-purple-800 to-purple-600 md:min-w-[240px] min-w-[120px]"
          @click="submitRecords">Verify</a-button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as XLSX from 'xlsx'
import { ref } from 'vue'
import * as evidenceRepository from '@/repository/getEvidenceResultRepository'
import type {
  evidenceRequestType,
  evidenceResponseType,
  evidenceTableType
} from '@/interfaces/types'
const props = defineProps({
  sideBarVisible: { type: Boolean, required: true }
})
const columns = [
  {
    title: 'CONTROL ID',
    dataIndex: 'id',
    key: 'id',
    width: 140
    //fixed: 'left'
  },
  {
    title: 'CONTROL NAME',
    dataIndex: 'name',
    key: 'name',
    width: 140
    //fixed: 'left'
  },
  {
    title: 'CONTROL DESC',
    dataIndex: 'description',
    key: 'description',
    width: 240
  },
  {
    title: 'ACC EVIDENCE',
    dataIndex: 'evidence',
    key: 'evidence',
    width: 240
  },
  {
    title: 'CHECKBOX',
    dataIndex: 'box',
    key: 'checkbox',
    width: 120,
    fixed: 'right'
  },
  {
    title: 'UPLOAD FEATURE',
    dataIndex: 'file',
    key: 'file',
    width: 150,
    fixed: 'right'
  },
  {
    title: 'PASS/FAIL',
    dataIndex: 'result',
    key: 'result',
    fixed: 'right',
    width: 120
  },
  {
    title: 'SUMMARY',
    dataIndex: 'summary',
    key: 'summary',
    fixed: 'right',
    width: 150
  }
]
const tableDataSource = ref<evidenceTableType[]>([])
//const checkedDataTables = ref<evidenceTableType[]>([])
const checkedDataTables = ref<evidenceRequestType[]>([])
const checked = ref<any>([])
const pdfFile = ref()
// const enableupload = (key: any, column: any) => {
//   console.log(column)
//   console.log(key)
//   console.log('----------\n')
//   tableDataSource.value = tableDataSource.value.map((item: any) => {
//     if (item.id === key.id) {
//       return { ...item, box: item.box }
//     } else {
//       return item
//     }
//   })
// }

const validateColumnName = (headers: any): boolean => {
  console.log(headers)
  return true
}
// completed
const uploadCsv = (event: any) => {
  const file = event.target.files[0]
  if (!file) return

  const reader = new FileReader()

  reader.onload = (e: any) => {
    const data = e.target.result
    const workbook = XLSX.read(data, { type: 'array' })
    const firstSheetName = workbook.SheetNames[0]
    const worksheet = workbook.Sheets[firstSheetName]
    const jsonData: { [key: string]: any }[] = XLSX.utils.sheet_to_json(worksheet, { header: 1 })

    const headers = jsonData[0]
    const validCsv = validateColumnName(headers)
    if (validCsv) {
      for (let i = 1; i < jsonData.length; i++) {
        checked.value.push(false)
        let obj: evidenceTableType = {
          id: jsonData[i][0],
          name: jsonData[i][1],
          description: jsonData[i][2],
          evidence: jsonData[i][3],
          result: '',
          summary: '',
          box: false,
          file: null
        }
        tableDataSource.value.push(obj)
      }
    }
  }
  reader.readAsArrayBuffer(file)
}

const formData = new FormData()
// Upload evidence file in pdf format
const uploadPdf = (event: any, record: evidenceTableType) => {
  const file = event.target.files[0]
  const filename = file.name
  console.log('Ye le filename ', filename)
  console.log('The file looks like: ', file)
  if (file) {
    pdfFile.value = file
    //record.filename = filename
    record.file = file
    checkedDataTables.value.push({
      id: record.id,
      name: record.name,
      description: record.description,
      evidence: record.evidence,
      box: record.box,
      filename: filename,
      result: '',
      summary: ''
    })
    formData.append('data', JSON.stringify(record))
    //update tableDataSource for pass/fail and summary
  }
}

const submitRecords = async () => {
  // Display the entries in the FormData object
  for (const entry of formData.entries()) {
    console.log(entry)
  }
  console.log('Form submitted')
  // const res: evidenceResponseType[] = await axios.post('', formData, {
  //   headers: { 'Content-Type': 'multipart/form-data' }
  // })
  // Check if the file property is not empty in any of the objects
  const isFileNotEmpty = checkedDataTables.value.every(
    (item) => item.filename !== null && item.filename !== undefined
  )
  if (isFileNotEmpty) {
    const res: evidenceResponseType[] = await evidenceRepository.getTestCaseResultRepository(
      checkedDataTables.value
    )
    // Iterate over tableDataSource array
    for (const item of tableDataSource.value) {
      // Find the corresponding item in res array based on id
      const matchingItem = res.find((resItem) => resItem.id === item.id)

      // If a matching item is found in res array
      if (matchingItem) {
        // Update 'result' and 'summary' properties in tableDataSource
        item.result = matchingItem.result
        item.summary = matchingItem.summary
      }
    }
  } else {
    throw new Error('First upload all the PDF files')
  }
}
</script>

<style>
.ant-table-pagination.ant-pagination {
  margin: 8px 0 !important;
}
</style>