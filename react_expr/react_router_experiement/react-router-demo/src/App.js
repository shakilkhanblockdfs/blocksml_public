// import logo from './logo.svg';
// import './App.css';

import {Routes, Route} from 'react-router-dom';
import {Home} from './components/Home';
import {About} from './components/About';
import { Navbar } from './components/Navbar';
import { OrderSummary } from './components/OrderSummary';
import { NoMatch } from './components/NoMatch';

function App() {
  return (
    <>
    <Navbar/>
    <Routes>
      <Route path="/" element={<Home/>}> </Route>
      <Route path="/home" element={<Home/>}> </Route>
      <Route path="/about" element={<About />}> </Route>
      <Route path="/order-summary" element={<OrderSummary />}> </Route>
      <Route path="*" element={<NoMatch />}> </Route>
    </Routes>
    </>
  );
}

export default App;
