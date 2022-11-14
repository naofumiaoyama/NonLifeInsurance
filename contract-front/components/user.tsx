import React, {useState, useEffect} from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { makeStyles } from '@mui/material/styles';
import axios from "axios";
import { color } from '@mui/system';

function User(){    
  const BASE_URL = 'http://localhost:8000/'
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get(BASE_URL + 'user')
      .then(response => {
        const json = response.data
        console.log(json);
        if (response.data) {
          return json
        }
        throw response
      })
      .then(data => {
        setUsers(data)
      })
      .catch(error => {
        console.log(error);
        alert(error)
      })
  }, [])

  type userItem = {
    id: string;
    email: string;
    username: string;
    first_name: string;
    last_name: string;
    is_active: boolean;
  }


  return (
    <div>
      <h1>User List</h1>
    
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 500 }} size="small" aria-label="a dense table">
          <TableHead style={{ backgroundColor:'Blue'}}>
            <TableRow>
              <TableCell align="left" style={{color:'white'}}>username</TableCell>
              <TableCell align="left" style={{color:'white'}}>firstname</TableCell>
              <TableCell align="left" style={{color:'white'}}>lastname</TableCell>
              <TableCell align="left" style={{color:'white'}}>email</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {users.map((user: userItem) => (
              <TableRow
                key={user.id}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell align="left">{user.username}</TableCell>
                <TableCell align="left">{user.first_name}</TableCell>
                <TableCell align="left">{user.last_name}</TableCell>
                <TableCell align="left">{user.email}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default User;