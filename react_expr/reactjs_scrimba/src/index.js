import React from "react";
import ReactDOM from "react-dom/client";

console.log("Hello World!");
console.log(React.version);

const navbar = (
    <nav>
        <h1>Bob's Bistro123</h1>
        <ul>
            <li>Menu</li>
            <li>About</li>
            <li>Contact1234</li>
        </ul>
        <p> This is a paragrpah tag123</p>
    </nav>
);

// ReactDOM.render(navbar, document.getElementById("root"));
// ReactDOM.createRoot(document.getElementById("root")).render(navbar);

// const root = ReactDOM.createRoot(document.getElementById("root"));
// root.render(navbar);

// Process 1, but this will not display jsx properly rather it will just dump it
// let root = document.getElementById("root");
// console.log(root);
// root.append(JSON.stringify(navbar));

// Process:2 Correct way of displaying the JSX 
ReactDOM.createRoot(document.getElementById("root")).render(navbar);

