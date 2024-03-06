import {useState} from 'react';
import { FileUploader } from './components/FileUploader';
import './App.css';
import {ToastContainer} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import {Preview} from './components/Preview';

function App() {
  const [files, setFiles] = useState([]);
  const onSuccess = (savedFiles) => {
    setFiles(savedFiles)
  };

  return (
    <div className="App">
      <FileUploader onSuccess={onSuccess} />
      <Preview files={files} />
      <ToastContainer />
    </div>
  );
}

export default App;
 