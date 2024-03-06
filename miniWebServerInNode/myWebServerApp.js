// npm install nodemon -g
// nodemon ./myWebServerApp.js
// If we run the server with nodemon then we don't need to stop and start the server.

const fs = require("fs");
const http = require("http");
const path = require("path");

const server = http.createServer((req, res) => {

    // http://localhost:5000
    if(req.url == '/'){
        fs.readFile(path.join(__dirname,"index.html"), (err,data) => {
            if(err) throw err;
            res.writeHead(200,{'Content-Type': 'text/html'});  
            res.end(data);
        });
    }

    // http://localhost:5000/about
    if(req.url == '/about'){
        fs.readFile(path.join(__dirname,"about.html"), (err,data) => {
            if(err) throw err;
            res.writeHead(200,{'Content-Type': 'text/html'});  
            res.end(data);
        });
    }

    // http://localhost:5000/api/users
    if(req.url == '/api/users'){
       const users = [
           {name: "Bobby", age:24},
           {salary: "$1B"},
           {occupation: "Fruit Trader"}
        ];
        res.writeHead(200,{'Content-Type': 'application/json'});  
        res.end(JSON.stringify(users));
    }

});

const PORT = process.env.PORT || 5000;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));

 
