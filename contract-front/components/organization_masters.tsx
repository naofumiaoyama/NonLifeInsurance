import React, {useState, useEffect, useRef, ChangeEvent} from 'react';
import Button from '@mui/material/Button';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import axios from "axios";

function OrganizatiomMaster(){    
  const BASE_URL = 'http://localhost:8000/'
  const [organization_masters, setOrganization_masters] = useState([]);
  const [orgName, setOrgName] = React.useState('')

  type organization_master_item = {
    id: string;
    name: string;  
  }

  function get_all(){
    axios.get(BASE_URL + 'organizationmaster')
    .then(response => {
      const json = response.data
      console.log(json);
      if (response.data) {
        return json
      }
      throw response
    })
    .then(data => {
      setOrganization_masters(data)
    })
    .catch(error => {
      console.log(error);
    })
  }
  
  useEffect(() => {
    get_all();
  }, [])

  function createPost() {
    axios.post(BASE_URL + 'organizationmaster/', {
      "name": orgName,
      })
      .then((response) => {
        console.log(response.data)
      });

      get_all();
  }


  // テキストボックスの値が変更された時Stateを更新する
  const onChangeValue = (event: ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();
    console.log(event.target.value);
    setOrgName(event.target.value);  // 値をStateへセットする
  };

  return (
    <div>
      <h1>OrganizatiomMaster List</h1>
      <div>
        <input type="text" onChange={onChangeValue} />
        <button onClick={createPost}>submit</button>
      </div>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 500 }} size="small" aria-label="a dense table">
          <TableHead style={{ backgroundColor:'Blue',}}>
            <TableRow>
              <TableCell align="left" style={{color:'white'}}>name</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {organization_masters.map((orgamization_master: organization_master_item) => (
              <TableRow
                key={orgamization_master.id}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell align="left">{orgamization_master.name}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
}

export default OrganizatiomMaster;