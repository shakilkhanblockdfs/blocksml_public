import React, { Component } from 'react'

class EventBind extends Component {
  constructor(props) {
    super(props)
  
    this.state = {
       message: "Hello123"
    }
  
      this.clickHandler = this.clickHandler.bind(this)
    }

  clickHandler(){
    this.setState({
        message: "Good bye"
    })

  }
    
  render() {
    return (
      <div>
        <div>
            {this.state.message}
        </div>
        {/* <button onClick={this.clickHandler.bind(this)}>Clicked_by_event_binding</button> */}
        <button onClick={this.clickHandler}>Clicked_by_event_binding</button>
      </div>
    )
  }
}

export default EventBind
