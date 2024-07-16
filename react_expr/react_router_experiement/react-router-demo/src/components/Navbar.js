import React from 'react'
import { NavLink } from 'react-router-dom'

const NavLinkStyles = ({isActive}) => {
  return {
    
    fontWeight:  isActive ? 'bold' : 'normal',
    textDecoration: isActive ? 'none' : 'underline'
  }
} 

export const Navbar = () => {
  return (
    <nav>
      <NavLink style={NavLinkStyles} to='/'> Home </NavLink>
      <NavLink style={NavLinkStyles} to='/about'> About </NavLink>
    </nav>
  )
}

// export default Home
