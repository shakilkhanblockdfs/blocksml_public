const fs = require('fs')
const pdfparse = require('pdf-parse')


//console.log(process.argv[0]);
//console.log(process.argv[1]);
//console.log(process.argv[2]);

const pdffile = fs.readFileSync(process.argv[2])

pdfparse(pdffile).then(function(data){
	//console.log(data.numpages)
	//console.log(data.info)
	 console.log(data.text)
})
