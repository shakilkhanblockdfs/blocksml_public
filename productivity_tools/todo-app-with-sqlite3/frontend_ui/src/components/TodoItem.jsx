import React from 'react';
import styles from './todoitem.module.css';

function TodoItem({ todo, updateTodo, deleteTodo }) {
  // Handles marking the todo as done or not done
  function handleClick() {
    // Toggle the 'done' status and pass it to updateTodo function
    updateTodo({ ...todo, done: !todo.done });
  }

  // Handles deleting the todo item
  function handleDelete() {
    deleteTodo(todo.id); // Call the deleteTodo function passed via props
  }

  // Apply the 'completed' class if the todo is done
  const className = todo.done ? styles.completed : '';

  return (
    <div className={styles.item}>
      <div className={styles.itemName}>
        {/* Clicking on the todo toggles the done state */}
        <span className={className} onClick={handleClick}>
          {todo.name}
        </span>
        {/* Clicking the delete button triggers the delete function */}
        <span>
          <button onClick={handleDelete} className={styles.deleteButton}>x</button>
        </span>
        <hr className={styles.line} />
      </div>
    </div>
  );
}

export default TodoItem;
