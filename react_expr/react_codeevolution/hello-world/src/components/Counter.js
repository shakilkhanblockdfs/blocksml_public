import React, { Component } from 'react'

class Counter extends Component {

  constructor(props) {
    super(props)
    this.state = {
        count:  0
    }
  }

//   increment(){
//     // this.state.count += 1               //This will not work
//     this.setState({
//         count: this.state.count +1
//     },()=>{
//         console.log(this.state.count)
//     })
//   }

    increment(){
        this.setState((prevState, props)=> ({
            count: prevState.count +1
        }), ()=>{
            console.log(this.state.count)
        })
        console.log("this is from the normal call not the call back " + this.state.count)
    }

  incrementFive(){
    this.increment()
    this.increment()
    // this.increment()
    // this.increment()
    // this.increment()
  }
  
  render() {
    return (
      <div>

        count - {this.state.count}
        <div> 
            <button onClick={()=> this.increment()}>
                InCreament
            </button>
        </div>
      </div>
    )
  }
}

export default Counter
