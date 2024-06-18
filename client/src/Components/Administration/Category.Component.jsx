import React from 'react';
import {CategoryTable} from "./SubComponents";
import {SearchIcon} from "../Assets/Svg";



const Category = () => {

    return (
        <main className="p-4">
            <h2 className="text-3xl font-bold text-center p-2"> Category Management</h2>
            <div className='container grid grid-cols-3 grid-flow-row-dense gap-4 pt-4'>
                <div className='grid-cols-1 grid gap-4'>
                    <div className="relative">
                        <input
                            type="search"
                            placeholder="Search..."
                            className="rounded border-2 text-lg text-gray h-12 w-full pl-[10px]"
                        />
                        <button type="button"
                                className="absolute inset-y-0 right-0 flex items-center pr-3 cursor-pointer">
                            <SearchIcon className="w-5 h-5 text-gray-400 dark:text-gray-500"/>
                        </button>
                    </div>
                    <form className="grid gap-4 rounded-bl max-h-[300px] col-span-1 shadow-2xl p-4">
                        <h3 className="text-black font-bold text-2xl">Create Category</h3>
                        <div className="max-w-[400px]">
                            <div className="grid gap-4">
                                <label htmlFor="username" className="text-start">Name</label>
                                <input type="text" placeholder="Name"
                                       className="rounded border-2 text-lg text-gray h-12 w-full pl-[10px]"/>
                            </div>
                        </div>
                        <div className="flex items-center justify-center">
                            <button className="p-[.25rem] font-bold text-lg bg-neutral-950 text-white h-12 rounded"
                                    type="submit">Create Category
                            </button>
                        </div>
                    </form>
                </div>


                <div className='grid col-span-2'>
                    <CategoryTable/>
                </div>

            </div>


        </main>
    )
}

export default Category