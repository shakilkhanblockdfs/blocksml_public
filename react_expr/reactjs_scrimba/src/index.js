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
    </nav>
);

// ReactDOM.render(navbar, document.getElementById("root"));
// ReactDOM.createRoot(document.getElementById("root")).render(navbar);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(navbar);
