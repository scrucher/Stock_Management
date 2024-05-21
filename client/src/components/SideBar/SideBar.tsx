import React from 'react';
import {Data} from '../../data'


export const SideBar = () => {
    const navData = Data.navBar;

    return (
        <div className='side-bar flex flex-col h-screen fixed w-[300px] text-center text-white bg-[#430A5D]'>
            <div className='text-4xl font-bold h-[100px] pb-8 pt-8'>
                stock manager
            </div>
            <ul className='list-none flex flex-col flex-grow items-center justify-evenly text-center h-full overflow-y-auto bg-[#430A5D] scroll-smooth'>
                {navData.map((data, index) => (
                    <li className='flex text-2xl font-medium' key={index}>
                        <a href='#'>{data.name}</a>
                    </li>
                ))}
            </ul>
        </div>
    );
}