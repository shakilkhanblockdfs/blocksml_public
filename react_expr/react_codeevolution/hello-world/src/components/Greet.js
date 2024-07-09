import React from 'react'

// function Greet(){
//     return <h1> Hello Blocksml</h1>   
// }

export const Greet = (props)=> {
    console.log(props)
    return (
        <div>
            <h1> Hello {props.name} A.K.A {props.heroName}</h1>
            {props.children}
        </div>
    )

}

// export default Greet; 