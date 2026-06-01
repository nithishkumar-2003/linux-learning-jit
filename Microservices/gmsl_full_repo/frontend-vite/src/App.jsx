import React, { useEffect, useState } from 'react'

export default function App(){
  const [registers, setRegisters] = useState([])
  useEffect(() => {
    fetch('http://localhost:8080/api/registers')
      .then(r => r.json())
      .then(setRegisters)
      .catch(e => console.error('fetch err', e))
  }, [])

  return (
    <div style={{ padding: 20, fontFamily: 'Arial' }}>
      <h2>GMSL — Registers (Monolith)</h2>
      <table border="1" cellPadding="8">
        <thead><tr><th>ID</th><th>Name</th><th>Address</th><th>Value</th></tr></thead>
        <tbody>
          {registers.map(r => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.name}</td>
              <td>{r.address}</td>
              <td>{r.value}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p>To run frontend: <code>npm install</code> then <code>npm run dev</code></p>
    </div>
  )
}
