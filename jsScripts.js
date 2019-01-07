const fs = require('fs');
const virtualRatings = require("./data/virtualRatings.json")
const data = require("./data.json")
const deletedPlaces = [
"5a7c5a9514f4ba437b8716b0",
"5a7c5b3814f4ba437b8717a2",
"5a7c5be114f4ba437b8718a9",
"5a7c6a6d14f4ba437b873321",
"5a7c6a8b14f4ba437b873351",
"5a7c6a5114f4ba437b8732f7",
"5a7c6a5414f4ba437b8732fc",
"5a7c6aaa14f4ba437b873385",
"5a7c6ae914f4ba437b8733e5",
"5a7c6af414f4ba437b8733f6",
"5a7c6b0f14f4ba437b87341f",
"5a7c6c4d14f4ba437b87369e",
"5a7c6c2014f4ba437b873656",
"5a7c6cd814f4ba437b873776",
"5a7c60c514f4ba437b871e06",
"5a7c60c914f4ba437b871e09",
"5a7c63cf14f4ba437b8728b7",
"5a7c66ae14f4ba437b872d32",
"5a7c66bb14f4ba437b872d49",
"5a7c66c214f4ba437b872d56",
"5a7c66d614f4ba437b872d76",
"5a7c67bd14f4ba437b872ee8",
"5a7c68a714f4ba437b87304b",
"5a7c68b414f4ba437b87305e",
"5a7c68cc14f4ba437b873084",
"5a7c69f314f4ba437b87325a",
"5a7c612d14f4ba437b871ebb",
"5a7c634e14f4ba437b8727eb",
"5a7c646f14f4ba437b8729ab",
"5a7c668a14f4ba437b872cf7",
"5a7c672e14f4ba437b872e00",
"5a7c673e14f4ba437b872e1b",
"5a7c685f14f4ba437b872fd5",
"5a7c691a14f4ba437b8730fe",
"5a7c614314f4ba437b871ed9",
"5a7c616714f4ba437b871f19",
"5a7c616914f4ba437b871f1d",
"5a7c633014f4ba437b8727b7",
"5a7c640514f4ba437b87290a",
"5a7c646114f4ba437b872992",
"5a7c647014f4ba437b8729ad",
"5a7c652314f4ba437b872ac7",
"5a7c658414f4ba437b872b64",
"5a7c672114f4ba437b872deb",
"5a7c692414f4ba437b87310e",
"5a7c694014f4ba437b87313a",
"5a9be5bb2e23931eeefbb1f3",
"5a9cb59971521d0c8a6e139e",
"5a9da43680c2041b35ee5c4e",
"5a9fe6a9f69e0356673bed62",
"5a93f5cf35427db22cf2ef1d",
"5a93f9b835427db22cf3dcd8",
"5a93f41535427db22cf27fb5",
"5a93f41835427db22cf28040",
"5a93f83535427db22cf38139",
"5a99ca1cbe387071b805d790",
"5aa006c7609d276ee1c4785a",
"5aa50a02bb4cec2c1bf9ef90",
"5aa50b93bb4cec2c1bf9ef93",
"5b4cb95fd64813ebac8dcd18",
"5b4cd405d64813ebac965f61",
"5b4df1a5d64813ebacf35e7b",
"5b4df7ccd64813ebacf4fbd3",
"5b4df20dd64813ebacf3797c",
"5b4df106d64813ebacf33600",
"5b4df716d64813ebacf4c889",
"5b91591a7928d192efd04dfc",
"5b9159077928d192efd04548"
]

function turnToId () {
  const objectId = []
  deletedPlaces.forEach((place) => {
    objectId.push(`ObjectId(${place})`)
  })

  removeFromRatings(objectId)
// console.log("objectId", objectId);
}

let places = virtualRatings

function removeFromRatings (deletedPlaces) {

  deletedPlaces.forEach((id) => {
    places = places.filter(place => place.place != id)
  })

  writeToFile('./removedRatings.json', places)
}

function writeToFile (path, data) {
console.log("data", data.length);
  console.log("in wirte to file");
  fs.writeFile(path, JSON.stringify(data, null,4), (err) => {
    if (err) throw err;
    console.log(path, 'saved!');
  })
}

function createMappingTable () {
console.log("data length", data.length);
}

createMappingTable()

// turnToId()
