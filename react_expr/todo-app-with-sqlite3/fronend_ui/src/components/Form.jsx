import React from 'react';
import { useState } from 'react';
import styles from './form.module.css';

function Form({ addTodo }) {
  const [todo, setTodo] = React.useState({ name: '', done: false });

  function handleSubmit(e) {
    e.preventDefault();
    addTodo(todo); // Call the function to add todo
    setTodo({ name: '', done: false });
  }

  return (
    <form className={styles.todoform} onSubmit={handleSubmit}>
      <div className={styles.inputContainer}>
        <input
          className={styles.modernInput}
          onChange={(e) => setTodo({ name: e.target.value, done: false })}
          value={todo.name}
          type="text"
          placeholder="Enter Todo Items"
        />
        <button className={styles.modernButton} type="submit">
          Add
        </button>
      </div>
    </form>
  );
}

export default Form;