import React, { useState, useEffect } from 'react';
import { Delete, GetAll, Update } from "../../../API";

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
const ProductTable = ({path}) => {
    const [isDeleteModalOpen, setDeleteModalOpen] = useState(false);
    const [isEditModalOpen, setEditModalOpen] = useState(false);
    const [edit, setEdit] = useState(null);
    const [list_all, setListAll] = useState([]);

    const handleDelete = async (id) => {
        try {
            await Delete(id, path);
            setListAll(GetAll.filter(item => item.id !== id));
            setDeleteModalOpen(false);
        } catch (error) {
            console.error('Error deleting item:', error);
        }
    };

    const handleEdit = async (updatedItem) => {
        try {
            await Update(updatedItem.id,updatedItem, path);
            setListAll(GetAll.map(item => (item.id === updatedItem.id ? updatedItem : item)));
            setEditModalOpen(false);
        } catch (error) {
            console.error('Error editing item:', error);
        }
    };

    useEffect(() => {
        const fetchData = async (path) => {
            try {
                const list_allData = await GetAll(path);
                setListAll(list_allData.list); // Assuming GetCategories returns an object with a 'data' property
            } catch (error) {
                console.error('Error fetching list_all:', error);
            }
        };

        fetchData(path);
    }, [path]);

    return (
        <div className='p-4'>
            <div className="shadow-lg rounded-3xl bg-gray-200">
                <div className="">
                    <table className="w-full table-fixed rounded-2xl bg-gray-100">
                        <thead className="rounded-3xl bg-gray-200">
                        <tr>
                            <th className="p-2 text-left w-1/7">Id</th>
                            <th className="p-2 text-left w-1/7">Name</th>
                            <th className="p-2 text-left w-1/7">Category</th>
                            <th className="p-2 text-left w-1/7">Unit</th>
                            <th className="p-2 text-left w-1/7">Unit Price</th>
                            <th className="p-2 text-left w-1/7">Expiration Date</th>
                            <th className="p-2 text-left w-1/7">Action</th>
                        </tr>
                        </thead>
                    </table>
                    <div className="overflow-y-auto max-h-[395px]">
                        <table className="w-full table-fixed rounded-2xl bg-gray-100">
                            <tbody>
                            {list_all.map((data, index) => (
                                <tr key={index} className="border-t text-left">
                                    <td className="p-2 w-1/7">{data.id}</td>
                                    <td className="p-2 w-1/7">{data.name}</td>
                                    <td className="p-2 w-1/7">{data.category}</td>
                                    <td className="p-2 w-1/7">{data.unit}</td>
                                    <td className="p-2 w-1/7">{data.unit_price}</td>
                                    <td className="p-2 w-1/7">{data.expiration_date}</td>
                                    <td className="p-2 w-1/7">
                                        <div className="flex gap-2">
                                            <Button
                                                className="bg-red-500 hover:bg-red-300 text-center"
                                                onClick={() => {
                                                        setEdit(data);
                                                        setDeleteModalOpen(true)
                                                    }
                                                }
                                            >
                                                Delete
                                            </Button>
                                            <Button
                                                className="bg-gray-950 text-white hover:bg-gray-700"
                                                onClick={() => {
                                                    setEdit(data);
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
                <p>This will permanently delete the data. This action cannot be undone.</p>
                <div className="mt-4 text-right">
                    <Button className="mr-2 bg-red-500 hover:bg-red-300"
                            onClick={() => setDeleteModalOpen(false)}>Cancel</Button>
                    <Button onClick={() => handleDelete(edit?.id)}
                            className="bg-gray-950 text-white hover:bg-gray-700">Continue</Button>
                </div>
            </Modal>

            {/* Edit Modal */}
            <Modal isOpen={isEditModalOpen} onClose={() => setEditModalOpen(false)} title="Edit data">
                <div className="grid gap-4 py-4">
                    <div className="grid items-center grid-cols-4 gap-4">
                        <label htmlFor="name" className="text-right">Name</label>
                        <input
                            id="name"
                            defaultValue={edit?.name}
                            className="col-span-3 p-2 border rounded"
                            onChange={(e) => setEdit({ ...edit, name: e.target.value })}
                        />
                    </div>
                </div>
                <div className="mt-4 text-right">
                    <Button onClick={() => handleEdit(edit)}
                            className="bg-gray-950 text-white hover:bg-gray-700">Save changes</Button>
                </div>
            </Modal>
        </div>
    );
};

export default ProductTable;
