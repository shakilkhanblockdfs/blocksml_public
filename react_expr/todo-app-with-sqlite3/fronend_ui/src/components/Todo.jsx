import React, { useEffect } from 'react';
import Form from './Form';
import TodoList from './TodoList';
import Footer from './Footer';
import axios from 'axios';

function Todo() {
  const [todos, setTodos] = React.useState([]);

  // Fetch todos from the backend
  useEffect(() => {
    axios.get('http://localhost:4000/todos')
      .then(response => setTodos(response.data))
      .catch(error => console.error('Error fetching todos:', error));
  }, []);

  // Add a new todo
  const addTodo = (newTodo) => {
    axios.post('http://localhost:4000/todos', newTodo)
      .then(response => setTodos([...todos, response.data]))
      .catch(error => console.error('Error adding todo:', error));
  };

  // Update the "done" state of a todo
  const updateTodo = (updatedTodo) => {
    // Send the update request to the backend
    axios.put(`http://localhost:4000/todos/${updatedTodo.id}`, updatedTodo)
      .then(response => {
        // Refresh the entire page after the response from backend
        window.location.reload();
      })
      .catch(error => console.error('Error updating todo:', error));
  };

  // Delete a todo
  const deleteTodo = (id) => {
    axios.delete(`http://localhost:4000/todos/${id}`)
      .then(() => setTodos(todos.filter(todo => todo.id !== id)))
      .catch(error => console.error('Error deleting todo:', error));
  };

  const completedTodos = todos.filter(todo => todo.done).length;
  const totalTodos = todos.length;

  return (
    <div>
      <Form todos={todos} setTodos={setTodos} addTodo={addTodo} />
      <TodoList todos={todos} updateTodo={updateTodo} deleteTodo={deleteTodo} />
      <Footer completedTodos={completedTodos} totalTodos={totalTodos} />
    </div>
  );
}

export default Todo;
