console.log("JS Loaded.")
searchForm = document.getElementById('search')
summarizeForm = document.getElementById("summarize")


//APIs
testUrl = "/test/"
searchUrl = "/search/" //post
summarizeUrl = "/summarizer/summarize/" //post


// Primary search
const simpleSearchSubmit = async (event) => {
  event.preventDefault()
  keywords = searchForm.querySelector("[name='keywords']").value
  sources = searchForm.querySelector("[name='sources']").value
  // Non helper function
  const response = await fetch(
    testUrl,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "keywords": keywords,
        "sources": sources
      })
    }
  )
  data = await response.json()
  console.log(data)
}


// general postData function
async function postData(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    body: JSON.stringify(data)
  });
  return response.json();
}


// Data append
function displayData(data){
  // const elem = document.getElementById("output")
  // elem.append(JSON.stringify(data, undefined, 2))
  document.getElementById("output").textContent = JSON.stringify(data, undefined, 2);

}

// Search Module

async function searchSubmit(event) {
  event.preventDefault();
  keywords = searchForm.querySelector("[name='keywords']").value
  sources = searchForm.querySelector("[name='sources']").value
  data = {
    keywords: keywords,
    sources: sources
  }
  response = await postData(testUrl, data)
  displayData(response)
}

// var data = {
//   "data": {
//     "x": "1",
//     "y": "1",
//     "url": "http://url.com"
//   },
//   "event": "start",
//   "show": 1,
//   "id": 50
// }

async function summarizeSubmit(event) {
  event.preventDefault();
  article = summarizeForm.querySelector("[name='article']").value
  displayData("Loading..")
  console.log("Making API call..")
  response = await postData(
    summarizeUrl,
    {
      text: article
    }
  )
  displayData(response)
}


// Event listeners
if (searchForm) {
  console.log("searchForm")
  searchForm.addEventListener('submit', searchSubmit)
}
if (summarizeForm) {
  console.log("summarizeForm")
  summarizeForm.addEventListener('submit', summarizeSubmit)
}