import React from "react"

function HeaderComponent() {
    return (    
        <header>
            <nav className="nav">
                
                <img className="img-style" src="./react-logo.png" width="40px" />
                <ul className="nav-item">
                    <li>Pricing</li>    
                    <li>About</li>    
                    <li>Contact</li>
                </ul>   
                <h3> ReactJS Separate HeaderComponent </h3>

            </nav>
        </header>
    )
}

export default HeaderComponent;