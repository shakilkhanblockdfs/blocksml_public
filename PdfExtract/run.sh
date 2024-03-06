npm init -y >/dev/null 2>&1
npm install pdf-parse >/dev/null 2>&1
node extractPdf.js sample.pdf
rm -fr node_modules
rm -fr package.json
rm -fr package-lock.json
