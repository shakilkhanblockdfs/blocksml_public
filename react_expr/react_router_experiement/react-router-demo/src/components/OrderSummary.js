import React from 'react'
import { useNavigate } from 'react-router-dom'

export function OrderSummary() {
  const navigate = useNavigate()
  return (
    <>
    <div>
        order Confirmed
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7218777375445020672" height="489" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>
    </div>
    {/* <button onClick={()=> navigate('/about')}>Go Back</button> */}
    <button onClick={()=> navigate(-1)}>Go Back</button>
    </>
  )
}

