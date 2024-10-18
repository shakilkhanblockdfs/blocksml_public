import React from 'react';
import TodoItem from './TodoItem';
import styles from './todolist.module.css';

function TodoList({ todos, updateTodo, deleteTodo }) {
  const sortedTodos = todos.slice().sort((a, b) => Number(a.done) - Number(b.done));

  return (
    <div className={styles.list}>
      {sortedTodos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          updateTodo={updateTodo} // Pass the update function
          deleteTodo={deleteTodo} // Pass the delete function
        />
      ))}
    </div>
  );
}

export default TodoList;
