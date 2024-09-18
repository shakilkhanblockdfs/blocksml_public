import React from 'react'
import Person from './Person'
function NameList() {
const names = [
    {
        name: "shakil",
        age: 50,
        id: 1,
        skills: ["react", "node", "mongodb"],
    },
    {
        name: "Adil",
        age: 12,
        id: 2,
        skills: ["Calculus", "Python", "Trigonometry"],
    },
    {
        name: "Alisha",
        age: 7,
        id: 4,
        skills: ["Boowriting", "Mathematics"]
    },
    {
        name: "Zareen",
        age: 37,
        id: 3,
        skills: ["AWS", "GCP", "Terraform"]
    }
]
const namesList = names.map(person => (
    <Person key={person.id} person={person}> </Person>
))
  return (
    <div>
      {namesList}
    </div>
  )
}

export default NameList
