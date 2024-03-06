import {useState} from 'react';
import {toast} from 'react-toastify';
import './style.css';
import axios from 'axios';

export const FileUploader = ({onSuccess}) =>{
    const [files, setFiles] = useState([]);
    const onInputChange = (e) => {
        // console.log(e.target.files);
        setFiles(e.target.files);
    };
 
    const onSubmit = (e) => {
        e.preventDefault();
        const data = new FormData();

        for(let i=0; i< files.length; ++i){
            data.append('file', files[i]);
        }

        // debugger                // We can put the debugger keyword to debug things at the browser

        axios.post('//localhost:8000/upload', data)
        .then((response) =>{
            // console.log('Success');
            toast.success('Upload Success');
            onSuccess(response.data);
        })
        .catch((e) =>{
            // console.error('Error', e);
            toast.error('Upload Error');
        })
    };

    return (  
    <form method="post" action="#" id="#" onSubmit={onSubmit}>
    <div className="form-group files">
      <label>Upload Your File </label>
      <input 
      type="file" 
      onChange={onInputChange}
      className="form-control" 
      multiple />
    </div>
   
    <button>Submit</button> 
</form>)
};