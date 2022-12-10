import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom';
import User from '../components/user'
import Address from '../components/address'
import Organizatiom_master from '../components/organization_masters'
import DataTable from '../components/organizationmaster';
export default function Home(){
  return (
    <>
      <User />
      <Address />
      <Organizatiom_master />
    </>
    
  );
}
  