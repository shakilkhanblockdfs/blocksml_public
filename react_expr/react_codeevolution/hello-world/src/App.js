import logo from './logo.svg';
import './App.css';
import {Greet} from './components/Greet'
import Welcome from './components/Welcome'
import Message from './components/Message'
import Hello from './components/Hello'
import Counter from './components/Counter'
import FunctionClick  from './components/FunctionClick';
import ClassClick  from './components/ClassClick';
import EventBind from './components/EventBind';
import UserGreeting from './components/UserGreeting';
import NameList from './components/NameList';

import React from 'react';
import ParentComponent from './components/ParentComponent';

function App() {
  return (
    <div className="App">
      <NameList />
      {/* <ParentComponent /> */}
      {/* <UserGreeting /> */}
      {/* <Counter> </Counter>
      <Welcome name="Bruce" heroName="Batman" />
      <FunctionClick></FunctionClick>
      <ClassClick></ClassClick>
      <EventBind></EventBind> */}

      {/* <Message>

      </Message> */}
    {/* //   <Greet name="Bruce" heroName="Batman">
    //     <p>
    //       This is the children Props
    //     </p>
    //     <p>
    //       This is another children Props
    //     </p>
    //   </Greet>
    //   <Greet name="clark" heroName="SuperMan" />
    //   <Greet name="Diana" heroName="AquaMan" />
    //   <Welcome name="Bruce" heroName="Batman" />
    //   <Welcome name="clark" heroName="SuperMan" />
    //   <Welcome name="Diana" heroName="AquaMan" /> 
      <Hello /> 
    */}
    </div>
  );
}

export default App;
 