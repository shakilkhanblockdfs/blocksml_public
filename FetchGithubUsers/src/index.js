import React,{useEffect, useState} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import App from './App';

/// Demo of useEffect and githubdata fetch

function GitHubUser({login}){
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch(`https://api.github.com/users/${login}`)
      .then(res => res.json())
      .then(setData)
      .catch(console.error);
  },[]);

  if(data){
    return (
    <div> 
      <h1> {data.login}</h1>
      <img src={data.avatar_url} width={100} />
      {JSON.stringify(data)}
    </div>);
  }
  return null;
}

function App(){
  return(
		<>
    <GitHubUser login="shakilk1729"/>
    <GitHubUser login="moonhighway"/>
    <GitHubUser login="eveporcello"/>
		</>
  )
}

ReactDOM.render(
	<App />,
	document.getElementById('root')
);

