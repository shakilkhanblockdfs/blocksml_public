import React from 'react'
import styles from "./todoitem.module.css"

function TodoItem({todo, todos, setTodos}) {
  function handleDelete(item){
    console.log("Delete button clicked", todo);
    setTodos(todos.filter((todo)=> item !== todo));
  }  

  function handleClick(name){
    const newArray = todos.map((todo)=> todo.name === name ? {...todo, done : !todo.done} : todo);
    setTodos(newArray);
  }

  const className = todo.done ? styles.completed : "";
  return (
    <div className={styles.item}>
        <div className={styles.itemName}>
            <span className={className} onClick={()=>handleClick(todo.name)}>
            {todo.name}
            </span>
            <span>
                <button onClick={()=>handleDelete(todo)} className={styles.deleteButton}>x</button>
            </span>
            <hr className={styles.line}/>
        </div>
    </div>
  )
}

export default TodoItem
