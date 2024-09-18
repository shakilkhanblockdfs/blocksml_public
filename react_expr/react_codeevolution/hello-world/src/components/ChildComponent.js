import React from 'react'

function ChildComponent(props) {
  return (
    <div>
        <button onClick={()=> props.greetHandler("child-sk-ak-ak")}>
            GreetParent
        </button>
    </div>
  )
}

export default ChildComponent
