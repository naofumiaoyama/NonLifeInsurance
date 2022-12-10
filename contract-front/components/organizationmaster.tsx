import React, {useState, useEffect, useRef, ChangeEvent} from 'react';
import Box from '@mui/material/Box';
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import axios from "axios";

const VISIBLE_FIELDS = ['name', 'rating', 'country', 'dateCreated', 'isAdmin'];

export default function OrganizatiomMaster() {
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
  
  // Otherwise filter will be applied on fields such as the hidden column id
  const columns = React.useMemo(
    () => data.columns.filter((column) => VISIBLE_FIELDS.includes(column.field)),
    [data.columns],
  );

  return (
    <Box sx={{ height: 400, width: 1 }}>
      <DataGrid
        {...data}
        disableColumnFilter
        disableColumnSelector
        disableDensitySelector
        columns={columns}
        components={{ Toolbar: GridToolbar }}
        componentsProps={{
          toolbar: {
            showQuickFilter: true,
            quickFilterProps: { debounceMs: 500 },
          },
        }}
      />
    </Box>
  );
}
