import React, { Component } from 'react'

class UserGreeting extends Component {

constructor(props) {
  super(props)

  this.state = {
     isLoggedIn: false
  }
}
  render() {
    // approach 4th
    return (
        this.state.isLoggedIn && <div> Welcome Shakil</div>
    )

    // approach 3
    // return (
    //     this.state.isLoggedIn ?
    //     <div> Welcome Shakil </div>:
    //     <div> Welcome Guest </div>
    // )

    // approach 2
    // let message
    // if(this.state.isLoggedIn){
    //     message = <div> Welcome Shakil</div>
    // }else {
    //     message = <div> Welcome Guest</div>
    // }        
    // return (
    //     <div> {message} </div>
    // )

    // approach 1
    // if (this.state.isLoggedIn){
    //     return (
    //         <div>
    //             Welcome shakil
    //         </div>
    //     )
    // }else
    // return (
    //     <div>
    //         Welcome Guest
    //     </div>
    // )

    // approach 0
    // return (
    //   <div>
    //     <div> Welcome Shakil </div>
    //     <div> Welcome Guest </div>
    //   </div>
    // )
  }
}

export default UserGreeting
