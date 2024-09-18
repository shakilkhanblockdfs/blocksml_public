import React, { Component } from 'react'

class ClassClick extends Component {
    clickHandler(){
        console.log("Clicked the button from class component");
    }

  render() {
    return (
      <div>
        <button onClick={this.clickHandler}>ClickMe</button>
      </div>
    )
  }
}

export default ClassClick
