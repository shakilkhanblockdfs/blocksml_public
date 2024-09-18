import React from 'react'

// const Hello = ()=> {
//     return (
//         <div>
//             <h1> Hello Blocksml</h1>   
//         </div>
//     )
// }


const Hello = ()=>{
    return React.createElement(
        'div', 
        {id: 'hewllo', className: 'Dummyclass'}, 
        React.createElement('h1', null, 'Hello blocksml'))
  }


export default Hello; 