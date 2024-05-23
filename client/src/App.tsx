import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Dashboard, Login, SideBar} from './components'

function App() {
    return (
        <>
        <div className="App flex">
            <div className='fixed'>
               <SideBar/>
            </div>

            <div className="flex-1 ">
                <Dashboard/>
            </div>
        </div>
        </>
    );
}

export default App;
