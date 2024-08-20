import React, {useState} from "react";
import {SideBar} from '../Utililties/Constents'

const SideBarComponent = () => {
    const [openDropdown, setOpenDropdown] = useState(null);

    const handleDropdownToggle = (index) => {
        setOpenDropdown(openDropdown === index ? null : index);
    };

    return (
        <div className="bg-gray-900 text-white w-64 p-6 flex flex-col gap-6">
            <a href="/" className="flex items-center gap-2" prefetch={false}>
                <span className="text-2xl font-bold">Admin</span>
            </a>
            <nav className="flex flex-col gap-2 overflow-y-auto max-h-screen justify-around">
                {SideBar.map((sideBar, index) => (
                    <a
                        key={index}
                        href={sideBar.href}
                        className="items-center content-center gap-2 px-4 py-2 cursor-pointer rounded-md hover:bg-gray-800 transition-colors"
                        prefetch={false}
                        onClick={() => sideBar.children && handleDropdownToggle(index)}
                    >
                        <div className='flex items-center content-center cursor-pointer'>
                            {React.createElement(sideBar.icon, {className: "h-[1.4rem] w-[1.4rem] "})}
                            <span className="text-[1.3rem] pl-[12px]">{sideBar.name}</span>
                        </div>

                        {sideBar.children && openDropdown === index && (
                            <div className="block px-4 py-2 cursor-pointer">
                                {sideBar.children.map((child, childIndex) => (
                                    <a
                                        key={childIndex}
                                        href={child.href}
                                        className="block px-4 py-2 rounded-md hover:bg-gray-800 transition-colors"
                                    >
                                        {child.name}
                                    </a>
                                ))}
                            </div>
                        )}
                    </a>
                ))}


            </nav>
        </div>
    )
}
export default SideBarComponent