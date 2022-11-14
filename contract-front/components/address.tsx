import React, {useState, useEffect} from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import axios from "axios";

function Address(){    
  const BASE_URL = 'http://localhost:8000/'
  const [addresses, setAddreses] = useState([]);

  useEffect(() => {
    axios.get(BASE_URL + 'address')
      .then(response => {
        const json = response.data
        console.log(json);
        if (response.data) {
          return json
        }
        throw response
      })
      .then(data => {
        setAddreses(data)
      })
      .catch(error => {
        console.log(error);
        alert(error)
      })
  }, [])

  type addressItem = {
    id: string;
    postal_code: string;
    prefecture_code: string;
    city_ward_name: string;
    street: string;
    building_name: string;
  }

  return (
    <div>
      <h1>Address List</h1>
    
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 500 }} size="small" aria-label="a dense table">
          <TableHead style={{ backgroundColor:'Blue',}}>
            <TableRow>
              <TableCell align="left" style={{color:'white'}}>postal_code</TableCell>
              <TableCell align="left" style={{color:'white'}}>prefecture_code</TableCell>
              <TableCell align="left" style={{color:'white'}}>city_ward_name</TableCell>
              <TableCell align="left" style={{color:'white'}}>street</TableCell>
              <TableCell align="left" style={{color:'white'}}>building_name</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {addresses.map((address: addressItem) => (
              <TableRow
                key={address.id}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell align="left">{address.postal_code}</TableCell>
                <TableCell align="left">{address.prefecture_code}</TableCell>
                <TableCell align="left">{address.city_ward_name}</TableCell>
                <TableCell align="left">{address.street}</TableCell>
                <TableCell align="left">{address.building_name}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default Address;