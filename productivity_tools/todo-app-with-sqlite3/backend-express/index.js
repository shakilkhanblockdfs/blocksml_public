const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

// Change from in-memory to file-based database by providing a path to the database file
// This will create the file if it doesn't already exist.
const db = new sqlite3.Database('./todos.db'); // File-based DB: 'todos.db' in the current directory

app.use(cors());
app.use(bodyParser.json());

// Initialize the database (creates the table if it doesn't exist)
db.serialize(() => {
  db.run("CREATE TABLE IF NOT EXISTS todos (name TEXT, done BOOLEAN)");
});

// Get all todos
app.get('/todos', (req, res) => {
  db.all("SELECT rowid AS id, name, done FROM todos", (err, rows) => {
    if (err) {
      res.status(500).send(err);
    } else {
      res.json(rows);
    }
  });
});

// Add a new todo
app.post('/todos', (req, res) => {
  const { name, done } = req.body;
  db.run(`INSERT INTO todos (name, done) VALUES (?, ?)`, [name, done], function(err) {
    if (err) {
      return res.status(500).send(err);
    }
    res.json({ id: this.lastID, name, done });
  });
});

// Update a todo
app.put('/todos/:id', (req, res) => {
  const { done } = req.body;
  const { id } = req.params;
  db.run(`UPDATE todos SET done = ? WHERE rowid = ?`, [done, id], function(err) {
    if (err) {
      return res.status(500).send(err);
    }
    res.json({ id, done });
  });
});

// Delete a todo
app.delete('/todos/:id', (req, res) => {
  const { id } = req.params;
  db.run(`DELETE FROM todos WHERE rowid = ?`, id, function(err) {
    if (err) {
      return res.status(500).send(err);
    }
    res.json({ id });
  });
});

const PORT = 4000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
