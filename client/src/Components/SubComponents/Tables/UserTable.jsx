import React, {useState} from 'react';

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
const UserTable = () => {
    const [isDeleteModalOpen, setDeleteModalOpen] = useState(false);
    const [isEditModalOpen, setEditModalOpen] = useState(false);
    const [editUser, setEditUser] = useState(null);

    const users = [
        {name: 'John Doe', email: 'john@example.com', role: 'Admin'},
        {name: 'Jane Smith', email: 'jane@example.com', role: 'Manager'},
        {name: 'Bob Johnson', email: 'bjhonson@example.com', role: 'User'},
        {name: 'Robert Erikson', email: 'e.robert@example.com', role: 'User'},
        {name: 'Carl Johnson', email: 'c.jhonson@example.com', role: 'Manager'},
        {name: 'Bob Aderson', email: 'b.aderson@example.com', role: 'User'},
        {name: 'Bob Marvel', email: 'bob@example.com', role: 'Manager'},
        {name: 'Winston Johnson', email: 'bob@example.com', role: 'User'},
        {name: 'Bob Jackson', email: 'bob@example.com', role: 'User'},

    ];

    return (
        <div className='p-4'>
            <div className="flex items-center mb-4">
                <h1 className="font-semibold text-lg md:text-2xl">Users</h1>
            </div>
            <div className="shadow-lg ">
                <div className="">
                    <table className="w-full table-fixed rounded-2xl bg-gray-200">
                        <thead className="rounded-2xl bg-gray-200">
                        <tr>
                            <th className="p-2 text-left w-1/5">Name</th>
                            <th className="p-2 text-left w-2/5">Email</th>
                            <th className="p-2 text-left w-1/5">Role</th>
                            <th className="p-2 text-left w-1/5">Actions</th>
                        </tr>
                        </thead>
                    </table>
                    <div className="overflow-y-auto overflow-x-auto max-h-[445px] rounded-2xl bg-gray-100">
                        <table className="w-full table-fixed">
                            <tbody>
                            {users.map((user, index) => (
                                <tr key={index} className="border-t ">
                                    <td className="p-2 w-1/5 text-left">{user.name}</td>
                                    <td className="p-2 w-2/5 text-left ">{user.email}</td>
                                    <td className="p-2 w-1/5 text-left">{user.role}</td>
                                    <td className="p-2 w-1/5">
                                        <div className="flex gap-2">
                                            <Button
                                                className="bg-red-500 hover:bg-red-300"
                                                onClick={() => setDeleteModalOpen(true)}
                                            >
                                                Delete
                                            </Button>
                                            <Button
                                                className="bg-gray-950 text-white hover:bg-gray-700"
                                                onClick={() => {
                                                    setEditUser(user);
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
                <p>This will permanently delete the user. This action cannot be undone.</p>
                <div className="mt-4 text-right">
                    <Button className="mr-2 bg-red-500 hover:bg-red-300" onClick={() => setDeleteModalOpen(false)}>Cancel</Button>
                    <Button onClick={() => setDeleteModalOpen(false)} className="bg-gray-950 text-white hover:bg-gray-700" >Continue</Button>
                </div>
            </Modal>

            {/* Edit Modal */}
            <Modal isOpen={isEditModalOpen} onClose={() => setEditModalOpen(false)} title="Edit user">
                <div className="grid gap-4 py-4">
                    <div className="grid items-center grid-cols-4 gap-4">
                        <label htmlFor="name" className="text-right">Name</label>
                        <input
                            id="name"
                            defaultValue={editUser?.name}
                            className="col-span-3 p-2 border rounded"
                        />
                    </div>
                    <div className="grid items-center grid-cols-4 gap-4">
                        <label htmlFor="email" className="text-right">Email</label>
                        <input
                            id="email"
                            defaultValue={editUser?.email}
                            className="col-span-3 p-2 border rounded"
                        />
                    </div>
                    <div className="grid items-center grid-cols-4 gap-4">
                        <label htmlFor="role" className="text-right">Role</label>
                        <select
                            id="role"
                            defaultValue={editUser?.role.toLowerCase()}
                            className="col-span-3 p-2 border rounded"
                        >
                            <option value="admin">Admin</option>
                            <option value="manager">Manager</option>
                            <option value="user">User</option>
                        </select>
                    </div>
                </div>
                <div className="mt-4 text-right">
                    <Button onClick={() => setEditModalOpen(false)} className="bg-gray-950 text-white hover:bg-gray-700">Save changes</Button>
                </div>
            </Modal>
        </div>
    );
};

export default UserTable;
