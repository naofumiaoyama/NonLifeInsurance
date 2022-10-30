import React, {useState, useEffect} from 'react';
import { useForm, Controller } from "react-hook-form";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function User(){
    
  const BASE_URL = 'http://localhost:8000/'
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(BASE_URL + 'user/get_all')
      .then(response => {
        const json = response.json()
        console.log(json);
        if (response.ok) {
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
    
      {users.map((user: userItem) => {
        return (
          <ul>
            <li key={user.id}>
              <span>
                {user.username}
              </span>
            </li>
            <li>
              <span>
                {user.email}
              </span>
            </li>
            <li>
              <span>
                {user.first_name}
              </span>
            </li>
            <li>
              <span>
                {user.last_name}
              </span>
            </li>
        
          </ul>
        );
      })}

      {users.map((user: userItem) => (
        <Card sx={{ minWidth: 275 }}>
          <CardContent>
            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
            {user.id} 
            </Typography>
            <Typography variant="h5" component="div">
            {user.username}
            </Typography>
            <Typography sx={{ mb: 1.5 }} color="text.secondary">
              {user.first_name}
            </Typography>
            <Typography variant="body2">
            {user.last_name}
            </Typography>
          </CardContent>
          <CardActions>
            <Button size="small">{user.email}</Button>
          </CardActions>
        </Card>

      ))}

      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 500 }} size="small" aria-label="a dense table">
          <TableHead>
            <TableRow>
              <TableCell align="left">username</TableCell>
              <TableCell align="left">firstname</TableCell>
              <TableCell align="left">lastname</TableCell>
              <TableCell align="left">email</TableCell>
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
