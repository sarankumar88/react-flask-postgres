import { useState } from 'react'

const AddRole = ({ onAdd }) => {
  const [team, setTeam] = useState('')
  const [role, setRole] = useState('')

  const onSubmit = (e) => {
    e.preventDefault()

    if (!team) {
      alert('Please enter team Name')
      return
    }
    if(!role) {
      alert('Please enter role Name')
    }

    onAdd({ team, role })

    setTeam('')
    setRole('')
  }

  return (
    <form style={{'marginBottom': '40px'}} onSubmit={onSubmit}>
      <div style={{'margin': '20px 0'}}>
        <label style={{'display': 'block'}}>Team</label>
        <input
          type='text' 
          style={{'width': '100%', 'padding': '3px 7px' , 'margin' : '5px'}}
          placeholder='Enter team name'
          value={team}
          onChange={(e) => setTeam(e.target.value)}
        />
      </div>
      <div style={{'display': 'block'}}>
        <label style={{'display': 'block'}}>Role Name</label>
        <input
          type='text'
          style={{'width': '100%', 'padding': '3px 7px' , 'margin' : '5px'}}
          placeholder='Enter role name'
          value={role}
          onChange={(e) => setRole(e.target.value)}
        />
      </div>

      <input type='submit' value='Save Role' className='btn btn-block' />
    </form>
  )
}


export default AddRole