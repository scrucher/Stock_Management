import React, { useState, useEffect } from 'react';
import { GetAll } from "../../../API";

// Custom Button Component
const Button = ({className, children, ...props}) => (
    <button className={`px-4 py-2 bg-blue-500 text-white rounded ${className}`} {...props}>
        {children}
    </button>
);

// Custom Modal Component
const Modal = ({isOpen, onClose, title, children}) => (
    isOpen ? (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
            <div className="bg-white rounded-lg overflow-hidden w-11/12 md:max-w-md mx-auto p-4">
                <h2 className="text-xl font-semibold">{title}</h2>
                <div className="mt-4">{children}</div>
                <div className="mt-4 text-right">
                </div>
            </div>
        </div>
    ) : null
);

// Main Component
const CategoryTable = () => {
    const [isDeleteModalOpen, setDeleteModalOpen] = useState(false);
    const [isEditModalOpen, setEditModalOpen] = useState(false);
    const [editCategory, setEditCategory] = useState(null);
    const [categories, setCategories] = useState([]);
    const path = 'Category'

    useEffect(() => {
        const fetchData = async () => {
            try {
                const categoriesData = await GetAll(path);
                setCategories(categoriesData.category); // Assuming GetCategories returns an object with a 'category' property
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div className='p-4'>
            <div className="flex items-center mb-4">
                <h1 className="font-semibold text-lg md:text-2xl">Categories</h1>
            </div>
            <div className="shadow-lg rounded-3xl bg-gray-200">
                <div className="">
                    <table className="w-full table-fixed rounded-2xl bg-gray-100">
                        <thead className="rounded-3xl bg-gray-200">
                        <tr>
                            <th className="p-2 text-left w-1/4">Id</th>
                            <th className="p-2 text-left w-1/4">Name</th>
                            <th className="p-2 text-left w-1/4">Actions</th>
                        </tr>
                        </thead>
                    </table>
                    <div className="overflow-y-auto max-h-[395px]">
                        <table className="w-full table-fixed rounded-2xl bg-gray-100">
                            <tbody>
                            {categories.map((category, index) => (
                                <tr key={index} className="border-t text-left">
                                    <td className="p-2 w-1/4">{category.id}</td>
                                    <td className="p-2 w-1/4">{category.name}</td>
                                    <td className="p-2 w-1/4">
                                        <div className="flex gap-2">
                                            <Button
                                                className="bg-red-500 hover:bg-red-300 text-center"
                                                onClick={() => setDeleteModalOpen(true)}
                                            >
                                                Delete
                                            </Button>
                                            <Button
                                                className="bg-gray-950 text-white hover:bg-gray-700"
                                                onClick={() => {
                                                    setEditCategory(category);
                                                    setEditModalOpen(true);
                                                }}
                                            >
                                                Edit
                                            </Button>
                                        </div>
                                    </td>
                                </tr>
                            ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            {/* Delete Modal */}
            <Modal isOpen={isDeleteModalOpen} onClose={() => setDeleteModalOpen(false)} title="Are you sure?">
                <p>This will permanently delete the category. This action cannot be undone.</p>
                <div className="mt-4 text-right">
                    <Button className="mr-2 bg-red-500 hover:bg-red-300"
                            onClick={() => setDeleteModalOpen(false)}>Cancel</Button>
                    <Button onClick={() => setDeleteModalOpen(false)}
                            className="bg-gray-950 text-white hover:bg-gray-700">Continue</Button>
                </div>
            </Modal>

            {/* Edit Modal */}
            <Modal isOpen={isEditModalOpen} onClose={() => setEditModalOpen(false)} title="Edit category">
                <div className="grid gap-4 py-4">
                    <div className="grid items-center grid-cols-4 gap-4">
                        <label htmlFor="name" className="text-right">Name</label>
                        <input
                            id="name"
                            defaultValue={editCategory?.name}
                            className="col-span-3 p-2 border rounded"
                        />
                    </div>

                </div>
                <div className="mt-4 text-right">
                    <Button onClick={() => setEditModalOpen(false)}
                            className="bg-gray-950 text-white hover:bg-gray-700">Save changes</Button>
                </div>
            </Modal>
        </div>
    );
};

export default CategoryTable;
