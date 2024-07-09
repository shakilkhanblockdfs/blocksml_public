import React from 'react'

function Person({person}) {
  return (
    <div>
      <h2>
        I am {person.name} and I am {person.age} years old and my id is {person.id} and my skills are {person.skills}  
      </h2>
    </div>
  )
}

export default Person
