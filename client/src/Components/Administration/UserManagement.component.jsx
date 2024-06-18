import React from 'react';
import {UserTable} from "./SubComponents";


const UserManagement = () => {

    return (
        <main className="p-4">
            <h2 className="text-3xl font-bold text-center p-2"> User Management</h2>
            <div className='container grid grid-cols-2 gap-4'>
                <form className="grid grid-cols-1 gap-4 rounded-bl max-h-[500px] shadow-2xl p-4 bg-[#ffffff] ">
                    <h3 className="text-black font-bold text-2xl">Create User</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
                        <div className="grid">
                            <label htmlFor="username" className="text-start">Name</label>
                            <input type="text" placeholder="Name"
                                   className="rounded border-2 text-lg text-gray h-12 w-full pl-[10px]"/>
                        </div>
                        <div className="grid">
                            <label htmlFor="phone" className="text-start">Phone</label>
                            <input type="tel" placeholder="0678787898"
                                   className="rounded border-2 text-lg text-gray h-12 w-full pl-[10px]"/>
                        </div>
                        <div className="grid">
                            <label htmlFor="username" className="text-start">Username</label>
                            <input type="text" placeholder="Username"
                                   className="rounded border-2 text-lg text-gray h-12 w-full pl-[10px]"/>
                        </div>
                        <div className="grid">
                            <label htmlFor="password" className="text-start">Password</label>
                            <input type="password" placeholder="Password"
                                   className="rounded border-2 text-lg text-gray h-12 w-full pl-[10px]"/>
                        </div>
                        <div className="grid">
                            <label htmlFor="email" className="text-start">Email</label>
                            <input type="email" placeholder="example@example.com"
                                   className="rounded border-2 text-lg text-gray h-12 w-full pl-[10px]"/>
                        </div>
                        <div className="grid">
                            <label htmlFor="service" className="text-start">Role</label>
                            <input type="text" placeholder="Role"
                                   className="rounded border-2 text-lg text-gray h-12 w-full pl-[10px]"/>
                        </div>
                        <div className="grid">
                            <label htmlFor="CIN" className="text-start">CIN</label>
                            <input type="text" placeholder="AB763863"
                                   className="rounded border-2 text-lg text-gray h-12 w-full pl-[10px]"/>
                        </div>
                    </div>
                    <div className="flex items-center justify-center">
                        <button className="p-[.25rem] font-bold text-lg bg-neutral-950 text-white h-12 rounded"
                                type="submit">Create User
                        </button>
                    </div>
                </form>


                <div className='grid'>
                    <UserTable/>
                </div>

            </div>


        </main>
    )
}

export default UserManagement