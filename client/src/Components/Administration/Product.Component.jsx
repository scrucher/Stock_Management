import React, { useEffect, useState } from 'react';
import { ProductTable } from "../SubComponents";
import { Create, GetAll } from '../../API';
import { BarCodeApi, HandleSuccess } from '../../Utililties';

const ProductManagement = () => {
    const path = 'Product';
    const CatPath = 'Category';
    const UnPath = 'Unit';
    const SupPath = 'Supplier';
    const [formData, setFormData] = useState({
        name: '',
        image_name: "",
        category: '',
        expiration_date: '',
        unit_price: '',
        unit: '',
        barcode: ''
    });
    const [placeholders, setPlaceholders] = useState({
        name: 'Name',
        image_name: 'Image',
        category: 'Select Category',
        expiration_date: 'Expiration Date',
        unit_price: 'Unit Price',
        unit: 'Select Unit',
        barcode: 'Barcode'
    });
    const [msg, setMsg] = useState('');
    const [categories, setCategories] = useState([]);
    const [suppliers, setSupplier] = useState([])
    const [units, setUnits] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await GetAll(UnPath);
                setUnits(data.list);
                const data_1 = await GetAll(CatPath);
                setCategories(data_1.data);
                const data_2 = await GetAll(SupPath);
                setSupplier(data_2.list);
            } catch (error) {
                console.error('Error fetching list_all:', error);
            }
        };

        fetchData();
    }, []);

    const handleChange = (e) => {
        const { name, value, } = e.target;
        
            setFormData({ ...formData, [name]: value });
    };

    const handleBarcodeBlur = async (e) => {
        const barcode = e.target.value;
        if (barcode) {
            setIsLoading(true);
            try {
                const product = await BarCodeApi(barcode); // Await the result of BarCodeApi
                if (product){
                    setFormData({
                        ...formData,
                        name: product.product.product_name,
                        image_name: product.product.image_url, // Handle image_name separately if needed
                        barcode: product.code
                    });
                    setPlaceholders({
                        name: product.product_name || 'Name',
                        image_name: 'Image', // Assuming placeholder for image_name
                        barcode: product.code || 'Barcode'
                    });    
                }
                
            } catch (error) {
                console.error('Error fetching product by barcode:', error);
            } finally {
                setIsLoading(false);
            }
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await Create(formData, path);
            const responseBlock = document.querySelector('.response-message');
            const formElements = document.querySelector('.form-control form');
            setMsg(response.message);
            if (response.message) {
                responseBlock.style.display = 'block';
                formElements.style.display = 'none';
                setTimeout(() => {
                    responseBlock.style.display = 'none';
                    formElements.style.display = 'block';
                    event.target.reset();
                }, 10000);
            }
        } catch (error) {
            console.error('Error creating product:', error);
        }
    };

    const openModal = () => {
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    return (
        <main className="p-4">
            <h2 className="text-3xl font-bold text-center p-2">Product Management</h2>
            <div className='container grid grid-cols-1 gap-4 pt-[80px]'>
                <button 
                    onClick={openModal} 
                    className="block text-white bg-black hover:bg-gray-900 focus:ring-4 focus:outline-none focus:ring-gray-300 rounded-lg text-xl font-bold px-5 py-2.5 text-center dark:bg-gray-900 dark:hover:bg-black w-[250px] dark:focus:ring-gray-800" 
                    type="button"
                >
                    Create Product
                </button>

                {isModalOpen && (
                    <div 
                        id="authentication-modal" 
                        tabIndex="-1" 
                        aria-hidden="true" 
                        className="fixed inset-0 z-50 flex min-w-[750px] items-center justify-center overflow-y-auto overflow-x-hidden h-[calc(100%-1rem)] max-h-full"
                    >
                        <div className="relative p-4  max-h-full">
                            <div className="relative bg-white rounded-lg shadow dark:bg-gray-800 w-[750px]">
                                <div className="flex items-center justify-between p-4 md:p-5 border-b rounded-t  dark:border-gray-700">
                                    <h3 className="text-xl font-semibold text-gray-900 dark:text-white">
                                        Create Product
                                    </h3>
                                    <button 
                                        type="button" 
                                        onClick={closeModal} 
                                        className="text-gray-400 bg-transparent hover:bg-red-500 hover:text-gray-900 rounded-lg text-sm w-8 h-8 inline-flex justify-center items-center dark:hover:bg-red-600 dark:hover:text-white"
                                    >
                                        <svg 
                                            className="w-3 h-3" 
                                            aria-hidden="true" 
                                            xmlns="http://www.w3.org/2000/svg" 
                                            fill="none" 
                                            viewBox="0 0 14 14"
                                        >
                                            <path 
                                                stroke="currentColor" 
                                                strokeLinecap="round" 
                                                strokeLinejoin="round" 
                                                strokeWidth="2" 
                                                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                                            />
                                        </svg>
                                        <span className="sr-only">Close modal</span>
                                    </button>
                                </div>
                                <div className="p-4 md:p-5 min-h[650px] min-w[700px] form-control">
                                    <form
                                        className="grid grid-cols-1 gap-6 rounded-2xl shadow-2xl p-8 bg-white"
                                        id="ProductForm"
                                        onSubmit={handleSubmit}
                                    >
                                        <h3 className="text-black font-bold text-3xl mb-6">Create Product</h3>
                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                                            <div className="grid">
                                                <label htmlFor="barcode" className="text-lg font-medium mb-2">Barcode</label>
                                                <input
                                                    value={formData.barcode}
                                                    onChange={handleChange}
                                                    onBlur={handleBarcodeBlur}
                                                    type="text"
                                                    placeholder="Barcode"
                                                    name="barcode"
                                                    className="border border-gray-300 text-lg text-gray-800 h-12 w-full px-4 rounded-lg bg-gray-50"
                                                />
                                                {isLoading && <p className="text-gray-500 mt-2">Loading...</p>}
                                            </div>
                                            <div className="grid">
                                                <label htmlFor="name" className="text-lg font-medium mb-2">Name</label>
                                                <input
                                                    value={formData.name}
                                                    onChange={handleChange}
                                                    type="text"
                                                    placeholder={placeholders.name}
                                                    name="name"
                                                    className="border border-gray-300 text-lg text-gray-800 h-12 w-full px-4 rounded-lg bg-gray-50"
                                                />
                                            </div>
                                            <div className="grid">
                                                <label className="text-lg font-medium mb-2" htmlFor="image_name">Image</label>
                                                <input
                                                    className="hidden"
                                                    onChange={handleChange}
                                                    type="hidden"
                                                    value={formData.image_name}
                                                    name="image_name"
                                                />
                                                <img className="w-48 h-48 object-contain rounded-lg" src={formData.image_name} alt="Product" />
                                            </div>
                                            <div className="grid">
                                                <label htmlFor="category" className="text-lg font-medium mb-2">Category</label>
                                                <select
                                                    value={formData.category}
                                                    onChange={handleChange}
                                                    name="category"
                                                    className="border border-gray-300 text-lg text-gray-800 h-12 w-full px-4 rounded-lg bg-gray-50"
                                                >
                                                    <option value="">Select Category</option>
                                                    {categories.map((category) => (
                                                        <option key={category.id} value={category.id}>{category.name}</option>
                                                    ))}
                                                </select>
                                            </div>
                                            <div className="grid">
                                                <label htmlFor="unit_price" className="text-lg font-medium mb-2">Unit Price</label>
                                                <input
                                                    value={formData.unit_price}
                                                    onChange={handleChange}
                                                    type="number"
                                                    step="0.01"
                                                    placeholder="Unit Price"
                                                    name="unit_price"
                                                    className="border border-gray-300 text-lg text-gray-800 h-12 w-full px-4 rounded-lg bg-gray-50"
                                                />
                                            </div>
                                            <div className="grid">
                                                <label htmlFor="unit" className="text-lg font-medium mb-2">Unit</label>
                                                <select
                                                    value={formData.unit}
                                                    onChange={handleChange}
                                                    name="unit"
                                                    className="border border-gray-300 text-lg text-gray-800 h-12 w-full px-4 rounded-lg bg-gray-50"
                                                >
                                                    <option value="">Select Unit</option>
                                                    {units.map((unit) => (
                                                        <option key={unit.id} value={unit.id}>{unit.name}</option>
                                                    ))}
                                                </select>
                                            </div>
                                            <div className="grid">
                                                <label htmlFor="expiration_date" className="text-lg font-medium mb-2">Expiration Date</label>
                                                <input
                                                    value={formData.expiration_date}
                                                    onChange={handleChange}
                                                    type="date"
                                                    name="expiration_date"
                                                    className="border border-gray-300 text-lg text-gray-800 h-12 w-full px-4 rounded-lg bg-gray-50"
                                                />
                                            </div>
                                            <div className="grid">
                                                <label htmlFor="unit" className="text-lg font-medium mb-2">Supplier</label>
                                                <select
                                                    value={formData.unit}
                                                    onChange={handleChange}
                                                    name="unit"
                                                    className="border border-gray-300 text-lg text-gray-800 h-12 w-full px-4 rounded-lg bg-gray-50"
                                                >
                                                    <option value="">Select Supplier</option>
                                                    {suppliers.map((supplier) => (
                                                        <option key={supplier.id} value={supplier.id}>{supplier.name}</option>
                                                    ))}
                                                </select>
                                            </div>
                                        </div>
                                        <div className="flex items-center justify-center mt-8">
                                            <button
                                                className="py-3 px-6 font-bold text-lg bg-black text-white rounded-lg hover:bg-gray-800 transition duration-300"
                                                type="submit"
                                            >
                                                Create Product
                                            </button>
                                        </div>
                                    </form>


                                    <div className="response-message hidden mt-4">
                                        <HandleSuccess msg={msg} />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}

                <div className='grid'>
                    <ProductTable path={path} />
                </div>
            </div>
        </main>
    );
}

export { ProductManagement };
