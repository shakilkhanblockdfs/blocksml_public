const express = require('express');
const multer = require('multer');
const cors = require('cors');

const app = express();

app.use(cors());

const storage = multer.diskStorage({
    destination:(req, file, cb) =>{
        cb(null, 'public');
    },
    filename:(req, file, cb) =>{
        cb(null, Date.now() + '-' + file.originalname);
    },
})

const upload = multer({storage}).single('file');

app.post('/upload',(req, res) => {
    upload(req, res, (err) =>{
        if(err){
            return res.status(500).json(err)
        }
        return res.status(200).send(req.file)
    });
})

// app.use(express.static('public'));
// app.post('/demo', (req, res) => res.status(200).send({demo: true}));

app.listen(8000, () => {
    console.log('App is running on port 8000')
});