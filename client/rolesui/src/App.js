import Header from "./components/Header"
import AddRole from './components/AddRole'

function App() {
  // Add Role
  const addRole = async (teamRole) => {
    const res = await fetch('/api/role', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(teamRole),
    })

   await res.json()
  }

  return (
    <div style={containerStyle}>
      <Header  />
      <AddRole onAdd= {addRole}/>
      <p id="status"></p>
    </div>
  );
}

// CSS in JS
const containerStyle = {
  'maxWidth': '500px',
  'margin': '30px auto',
  'overflow': 'auto',
  'minHeight': '300px',
  'border': '1px solid steelblue',
  'padding': '30px',
  'borderRadius': '5px',
}

export default App;
