<script setup lang="ts">
import { ref, nextTick } from 'vue'
import { useGetPreferenceListStore } from '@/stores/getPreferenceListStore'
import { usePreferenceValueStore } from '@/stores/getPreferenceValueStore'
import { useDocumentsStore } from '@/stores/getDocumentsStore'
import { useCheckedDocumentStore } from '@/stores/getCheckedDocumentStore'
import { getTestCaseResults } from '@/repository/getTestCaseResultRepository'
import type {
  Chat,
  Industry,
  Region,
  ChatRequestParam,
  responseTableType
} from '@/interfaces/types'
import NavBar from '@/components/NavigationBar.vue'
import EvidenceTabView from './EvidenceTabView.vue'

const activeKey = ref('1')
// Read more button
const showDetails = ref(false)
const screenWindow = ref()
const toggleDetails = () => {
  showDetails.value = !showDetails.value
  setTimeout(() => {
    scrollToScreenBottom()
  }, 5)
}
// Reading store values
const preferenceListStore = useGetPreferenceListStore()
const preferenceValueStore = usePreferenceValueStore()
const documentStore = useDocumentsStore()
const checkedDocumentStore = useCheckedDocumentStore()
const industryList: Industry[] = preferenceListStore.IndustryList
const regionList: Region[] = preferenceListStore.RegionList

async function scrollToScreenBottom() {
  // Get the chat content container
  // Wait for the next tick to ensure DOM has updated
  await nextTick()
  // Scroll to the bottom of the chat content
  screenWindow.value.scrollTop = screenWindow.value.scrollHeight
  // Wait for the browser to update the scroll position
  // screenWindow.value.scrollTop = screenWindow.value.scrollTop +
  console.log(screenWindow.value.scrollTop)
}

const valueSelectedIndustry = ref<Industry | null>(null) //Technology
const valueSelectedRegion = ref<Region | null>(null) //North America
const handleIndustryChange = () => {
  preferenceValueStore.setSelectedIndustry(valueSelectedIndustry.value)
}
const handleRegionChange = () => {
  preferenceValueStore.setSelectedRegion(valueSelectedRegion.value)
}
// const plainOptions = ref(documentStore.getDocuments)
// const getDocumentList = async () => {
//   console.log('Here is the document')
//   // connect with the store function
//   await documentStore.fetchDocuments()
//   console.log(documentStore.getDocuments)

//   let documentList = documentStore.getDocuments
//   plainOptions.value = documentList?.map(document => document.DocumentName);

//   console.log(plainOptions.value.length)
// }

const plainOptions = ref<string[]>([])

const getDocumentList = async () => {
  isLoadingDocument.value = true
  console.log('Fetching documents...')

  // Fetch documents from the store
  await documentStore.fetchDocuments()

  // Assuming documentStore.getDocuments is a reactive property or a getter returning an array
  let documentList = documentStore.getDocuments

  // Update plainOptions with the names of the documents
  plainOptions.value = documentList.map((document) => document.DocumentName)
  isLoadingDocument.value = false
  console.log('Number of documents:', plainOptions.value.length)
}

//  [
//   'PCI',
//   'ISO',
//   'Internal',
//   'PCI DSS',
//   'ISO',
//   'Internal',
//   'PCI DSS',
//   'ISO',
//   'Internal'
// ]

const checkedList = ref([])
const handleChecked = () => {
  checkedDocumentStore.setCheckedDocument(checkedList.value)
  console.log('The current value is: ', checkedList.value)
}

const focus = () => {
  console.log('focus')
}
//const value = ref<string>('')
// const handleChange = (value: string) => {
//   console.log(`selected ${value}`)
// }
const textValue = ref('')
// Create a reactive variable using ref
const chatRequestParam = ref<ChatRequestParam>({
  doc_list: [],
  query: ''
})
//Mock Server related
const chatHistory = ref<Chat[]>([])
const responseTableArray = ref<responseTableType[]>([])
const responseTableWs = ref<responseTableType>()
const submitChat = async () => {
  isLoadingTable.value = true
  console.log(textValue.value)
  chatRequestParam.value = { query: textValue.value, doc_list: checkedList.value }
  chatHistory.value.push({ message: textValue.value, by: 'human' })
  textValue.value = ''
  // Make the API call for getting test results
  responseTableWs.value = await getTestCaseResults(chatRequestParam.value)
  responseTableArray.value.push(responseTableWs.value)
  chatHistory.value.push({ message: 'Server Responded', by: 'server' })
  isLoadingTable.value = false
  //call to backend and add ai message to chathistory
  // Send the message to the WebSocket server
  // socket.send(JSON.stringify(chatRequestParam.value)) //Websocket Code
  // Clear the text value

  console.log(chatHistory.value)
  scrollToBottom()
}

const chatContent = ref()
async function scrollToBottom() {
  // Get the chat content container
  // Wait for the next tick to ensure DOM has updated
  await nextTick()
  // Scroll to the bottom of the chat content
  chatContent.value.scrollTop = chatContent.value.scrollHeight
}

const isLoadingTable = ref(false)
const isLoadingDocument = ref(false)
// Websocket related functions

// // Replace 'ws://localhost:3000' with your WebSocket server URL
// const socket = new WebSocket('ws://localhost:3000')

// socket.onopen = () => {
//   console.log('WebSocket connection established')
// }

// // For receiving message
// socket.onmessage = (event) => {
//   const data = JSON.parse(event.data)
//   responseTableWs.value = data?.responseTable
//   console.log('My data looks like this: ', data?.chatMessage)
//   chatHistory.value.push(data)
//   // Scroll to the bottom of the chat content
//   scrollToBottom()
// }
// // change yaha rok de ab
// watchEffect(() => {
//   // Example cleanup function on component unmount
//   return () => {
//     socket.close()
//   }
// })

//Demo data for table
// const multilineString: String = `1. Inquire with control owners to determine whether a process is in place to register and provision user access to systems.
//     2. Verify that access to personal information is restricted by procedures that address:
//       - Authorizing and registering internal personnel and individuals
//       - Identifying and authenticating internal personnel and individuals
//       - Making changes and updating access profiles
//       - Granting system access privileges and permissions
//       - Preventing individuals from accessing other than their own personal or sensitive information
//     3. Obtain and inspect policies and procedures and verify that procedures are in accordance with access requirements as listed in the policies, and cover the management of access to network systems, management networks, and information systems`
// const tableDataSource = ref([
//   {
//     id: 1,
//     control_family: 'Access Control',
//     domain: '1',
//     sub_domain: '2',
//     control_description: 'rfwf',
//     test_procedure: 'dddjdjdj',
//     accepted_evidence: 2
//   },
//   {
//     id: 2,
//     control_family: 'fsfgsg',
//     domain: 's',
//     sub_domain: 'gsgs',
//     control_description: 'gsg',
//     test_procedure: 'ddd',
//     accepted_evidence: 2
//   },
//   {
//     id: 3,
//     control_family: 'gsg',
//     domain: 'sgsg',
//     sub_domain: 'gsgs',
//     control_description: 'gsg',
//     test_procedure: 'gsg',
//     accepted_evidence: 4
//   },
//   {
//     id: 4,
//     control_family: 'gs',
//     domain: 'sgsg',
//     sub_domain: 'gsgs',
//     control_description: 'gsg',
//     test_procedure: 'gs',
//     accepted_evidence: 3
//   },
//   {
//     id: 5,
//     control_family: 'gsg',
//     domain: 'sgsg',
//     sub_domain: 'gsgdkddjs',
//     control_description: 'gsg',
//     test_procedure: createVNode('div', { innerHTML: multilineString.replace(/\n/g, '<br>') }),
//     accepted_evidence: 10
//   }
// ])
const sideBarVisible = ref(true)
const toggleSidebar = () => {
  sideBarVisible.value = !sideBarVisible.value
}
const tableColumns = ref([
  {
    title: 'Control Family',
    dataIndex: 'control_family',
    key: 'control_family'
  },
  {
    title: 'Domain',
    dataIndex: 'domain',
    key: 'domain'
  },
  {
    title: 'Sub-Domain',
    dataIndex: 'sub_domain',
    key: 'sub_domain'
  },
  {
    title: 'Control Description',
    dataIndex: 'control_description',
    key: 'control_description'
  },
  {
    title: 'Test Procedure',
    dataIndex: 'test_procedure',
    key: 'test_procedure'
  },
  {
    title: 'Accepted Evidence',
    dataIndex: 'accepted_evidence',
    key: 'accepted_evidence'
  }
])
</script>

<template>
  <div class="w-full h-fit" ref="screenWindow">
    <NavBar />
    <!-- <div
      class="w-full flex justify-center bg-gradient-to-r from-purple-600 to-purple-500 items-center text-5xl text-white font-bold p-4 h-[8vh]"
    >
      ComplAI
    </div> -->
    <div
      class="w-full flex flex-col justify-center bg-gradient-to-r from-purple-800 to-purple-600 items-start text-white p-4 min-h-[10vh]">
      <div class="text-lg font-semibold">ComplAI</div>
      <!-- <div class="h-[10px]"></div> -->
      <div class="text-white text-xs mt-2 text-left" v-if="showDetails">
        A Gen-AI powered Automated Control Testing platform that leverages the power of machine
        learning to promptly generate test cases, validate control effectiveness, evidence analysis,
        learn from failures, and adapt to changing system behaviors.
      </div>
      <button @click="toggleDetails" class="text-white cursor-pointer text-[10px]">
        {{ showDetails ? 'Read less' : 'About ComplAI...' }}
      </button>
    </div>
    <div class="w-full flex min-h-[72vh] h-full relative">
      <!-- Button to toggle sidebar -->
      <button
        class="absolute top-52 left-[236px] transform translate-x-1/2 -translate-y-1/2 bg-purple-300 rounded-full p-2"
        @click="toggleSidebar" v-if="sideBarVisible">
        <!-- You can use any icon for the button -->
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-white" fill="none" viewBox="0 0 24 24"
          stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
      </button>
      <button v-else
        class="absolute top-52 left-1 transform -translate-x-1/2 -translate-y-1/2 bg-purple-300 rounded-full p-2"
        @click="toggleSidebar">
        <!-- You can use any icon for the button -->
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-white" fill="none" viewBox="0 0 24 24"
          stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
      </button>
      <div class="md:w-[280px] flex-grow h-full flex flex-col p-2 items-center" v-if="sideBarVisible">
        <div class="text-base font-bold">Preferences</div>
        <div class="w-full flex flex-col px-4 gap-2">
          <div class="w-full flex flex-col space-y-1">
            <div class="font-semibold text-sm">Industry</div>
            <a-space>
              <a-select ref="select" size="small" v-model:value="valueSelectedIndustry" class="md:w-[220px]"
                @focus="focus" @change="handleIndustryChange">
                <div v-for="industry in industryList" :key="industry.IndustryName">
                  <a-select-option :value="industry">{{ industry.IndustryName }}</a-select-option>
                </div>
              </a-select>
            </a-space>
          </div>

          <div class="w-full flex flex-col space-y-1">
            <h class="font-semibold text-sm">Region</h>
            <a-space>
              <a-select ref="select" size="small" v-model:value="valueSelectedRegion" class="md:w-[220px]"
                @focus="focus" @change="handleRegionChange">
                <div v-for="region in regionList" :key="region.RegionName">
                  <a-select-option :value="region">{{ region.RegionName }}</a-select-option>
                </div>
              </a-select>
            </a-space>
          </div>
          <div class="flex justify-center">
            <a-button type="primary" size="small"
              class="mt-2 bg-gradient-to-r from-purple-800 to-purple-600 text-[12px] w-full justify-center"
              style="font-size: 12px !important" @click="getDocumentList">Select Document</a-button>
          </div>
          <div class="mt-2 text-center" v-if="isLoadingDocument"><a-spin /></div>
          <div class="w-full flex flex-col space-y-1" v-if="plainOptions.length > 0">
            <h class="font-semibold text-sm">Documents</h>
            <!-- <a-checkbox-group v-model:value="checkedList" name="checkboxgroup" size="small" :options="plainOptions"
              @change="handleChecked" /> -->
            <div class="max-w-[220px] overflow-x-scroll">
              <a-checkbox-group v-model:value="checkedList" name="checkboxgroup" class="flex" size="small"
                :options="plainOptions" @change="handleChecked" />
            </div>
          </div>
        </div>
      </div>
      <div
        class="w-full border-l h-full border-gray-50 shadow-lg bg-gradient-to-tl from-purple-200 to-white px-8 flex-grow">
        <a-tabs v-model:activeKey="activeKey">
          <a-tab-pane key="1" tab="Home" class="h-full">
            <div class="w-full h-[48vh] mb-4 p-2 overflow-y-auto" style="scrollbar-width: none" ref="chatContent">
              <div class="w-full mb-2 last:mb-0" :key="index" v-for="(chat, index) in chatHistory">
                <div class="flex gap-x-[1px] w-full" :class="chat.by == 'human' ? ' justify-start' : 'justify-end'">
                  <div v-if="chat.by == 'human'">
                    <img src="@/assets/user-icon.svg" alt="User" />
                    <div class="rounded-lg p-2 min-w-[200px] max-w-[360px] md:max-w-[520px] -asdasdmt-1 bg-gray-200">
                      {{ chat.message }}
                    </div>
                  </div>
                  <div v-else>
                    <img src="@/assets/robot-icon.svg" alt="Bot" />
                    <div class="rounded-lg p-2 min-w-[200px] w-full -asdasdmt-1 bg-purple-500 text-white">
                      <a-table :dataSource="[responseTableArray[Math.floor(index / 2)]]" :columns="tableColumns"
                        :scroll="{ y: 440 }" class="custom-table">
                        <template #bodyCell="{ text }">
                          <div class="whitespace-pre-line from-neutral-500">
                            {{ text }}
                          </div>
                        </template>
                      </a-table>
                    </div>
                  </div>
                </div>
              </div>
              <div v-if="isLoadingTable" class="text-center align-middle"><a-spin /></div>
            </div>
            <div class="mb-1 w-full space-x-4 min-h-[10vh] h-full flex">
              <a-textarea v-model:value="textValue" placeholder="Basic usage" :rows="2"
                class="flex min-h-[5vh] h-full max-h-[10vh] shadow-lg" />
              <a-button type="primary" class="bg-gradient-to-r from-purple-800 to-purple-600"
                @click="submitChat">Query</a-button>
            </div>
            <div class="mb-2 text-[8px] text-center w-full text-slate-700">
              Please note that this content is AI generated and may not be 100% accurate. Refrain
              from entering personal data or client information. Users are responsible for
              validating the information before using.
            </div>
          </a-tab-pane>
          <a-tab-pane key="2" tab="Evaluation" force-render class="h-full p-2">
            <EvidenceTabView :sideBarVisible="sideBarVisible"></EvidenceTabView>
          </a-tab-pane>
        </a-tabs>
      </div>
    </div>
  </div>
</template>
<style>
.ant-table-tbody {
  vertical-align: top !important;
}

.ant-checkbox-wrapper {
  font-size: 12px;
}
</style>
