import React, { useState } from 'react';
import { Table } from "../SubComponents";
import { SearchIcon, SuccessIcon } from "../../Assets/Svg";
import { Create } from "../../API";
import { HandleError, HandleSuccess } from "../../Utililties";

const Service = () => {
    const [formData, setFormData] = useState({ name: '' });
    const [msg, setMsg] = useState('');
    const path = 'Service';

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevState) => ({
            ...prevState,
            [name]: value
        }));
    };

    const HandleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await Create(formData, path);
            const ResponseBlock = document.querySelector('.response-message');
            const FormElements = document.querySelector('.form-control form');
            setMsg(response.message);
            if (response.message) {
                ResponseBlock.style.display = 'block';
                FormElements.style.display = 'none';
                setTimeout(() => {
                    ResponseBlock.style.display = 'none';
                    FormElements.style.display = 'block';
                    event.target.reset();
                }, 10000);
            }
        } catch (error) {
            console.error('Error creating unit:', error);
        }
    };

    return (
        <main className="min-h-screen bg-gray-100 p-6">
            <h2 className="text-4xl font-bold text-left mb-6 text-black">Service Management</h2>
            <div className="container mx-auto grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="md:col-span-1 flex flex-col">
                    <div className="relative mb-6">
                        <input
                            type="search"
                            placeholder="Search..."
                            className="w-full h-12 px-4 pr-10 rounded-2xl border-2 border-gray-300 focus:outline-none focus:border-black"
                        />
                        <button type="button" className="absolute inset-y-0 right-0 flex items-center pr-4">
                            <SearchIcon className="w-5 h-5 text-gray-400" />
                        </button>
                    </div>
                    <div className="form-control bg-white p-6 rounded-2xl shadow-md flex-grow">
                        <form onSubmit={HandleSubmit} className="flex flex-col h-full">
                            <h3 className="text-2xl font-bold mb-4 text-black">Create Service</h3>
                            <div className="flex-grow">
                                <label htmlFor="name" className="block text-gray-700 mb-2">Name</label>
                                <input
                                    type="text"
                                    placeholder="Name"
                                    className="w-full h-12 px-4 rounded-2xl border-2 border-gray-300 focus:outline-none focus:border-black mb-4"
                                    name="name"
                                    id="name"
                                    value={formData.name}
                                    onChange={handleChange}
                                />
                            </div>
                            <div className="text-center mt-auto">
                                <button
                                    className="w-full h-12 bg-black text-white font-bold rounded-2xl hover:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-black"
                                    type="submit"
                                >
                                    Create Service
                                </button>
                            </div>
                        </form>
                        <div className="response-message hidden mt-4">
                            <HandleSuccess msg={msg} />
                        </div>
                    </div>
                </div>
                <div className="md:col-span-2">
                    <div className="mb-6">
                        <h1 className="text-2xl font-semibold text-black">Services</h1>
                    </div>
                    <Table path={path} />
                </div>
            </div>
        </main>
    );
};

export { Service };
