import React from 'react'
import styles from "./footer.module.css"

function Footer({completedTodos, totalTodos}) {
  return (
    <div className={styles.footer}>
      <span className={styles.item}>
        Completed Todos: {completedTodos}
      </span>
      <span className={styles.item}>
          Total Todos: {totalTodos}
      </span>
    </div>
  )
}

export default Footer
