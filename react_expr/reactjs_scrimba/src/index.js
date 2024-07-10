import React from "react";
import ReactDOM from "react-dom/client";

const page = (
        <div>
            <img src="react-logo.png" alt="React Logo" />
            <h1> Fun Facts about React</h1>
            <ul>
                <li>Was first release in 2013</li>
                <li>Was Originally created by Jordan Walke</li>
                <li>Was Created by Facebook</li>
            </ul>
        </div>
);

// console.log(page)

ReactDOM.createRoot(document.getElementById("root")).render(page);
