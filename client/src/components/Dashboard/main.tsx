import React from "react";
import {Metrix} from './matrix1'


export const Dashboard: React.FC = () => {

    return (
        <div className="grid grid-cols-2 gap-4 justify-evenly items-center text-black h-screen w-screen pl-[350px] pt-[50px] ">
            <div className='card h-[400px] w-[400px] text-center items-center justify-center'>
                < Metrix />
            </div>
            <div className='card h-[400px] w-[400px] text-center'>
                text
            </div>
            <div className='card h-[400px] w-[400px] text-center'>
                text
            </div>
            <div className='card h-[400px] w-[400px] text-center'>
                text
            </div>
        </div>
    )
}