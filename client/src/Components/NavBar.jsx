import React from 'react'
import {BellIcon, MenuIcon} from '../Assets/Svg'

const NavBar = () => {

    return (
        <>
            <header className="bg-white border-b px-6 py-4 flex items-center justify-between">
                <div className="flex items-center gap-4">
                    <button  size="icon">
                        <MenuIcon className="h-6 w-6"/>
                    </button>
                </div>
                <div className="flex items-center gap-4">
                    <button  size="icon">
                        <BellIcon className="h-6 w-6"/>
                        <span className="sr-only">Notifications</span>
                    </button>
                </div>
            </header>
        </>
    )
}

export default NavBar