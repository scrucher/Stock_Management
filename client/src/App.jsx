import React, {lazy, Suspense, useEffect, useState} from 'react';
import './App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import {
    Category,
    UserManagement,
    NavBar,
    LogIn,
    SideBarComponent,
    Dashboard,
    Service,
    Unit,
    ProductManagement,
    Supplier,
    Client,
    StockDashboard,
    PreLoader
} from "./Components";

const  App = () => {

    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        // Simulate loading time (replace with actual data fetching/loading logic)
        setTimeout(() => setIsLoading(false), 1000); // Adjust the timeout as needed
    }, []);

    if (isLoading) {
        return <PreLoader />;
    }

    return (
        <div className="App flex min-h-screen w-full bg-gray-100">
            <Suspense fallback={PreLoader}>
                <SideBarComponent />
            <div className="flex-1 flex flex-col">
                    <NavBar />
                <BrowserRouter basename="/">
                        <Routes>
                            <Route path="/" element={<Dashboard />} />
                            <Route path="/Users" element={<UserManagement />} />
                            <Route path='/Category' element={<Category />} />
                            <Route path='/Service' element={<Service />} />
                            <Route path='/Unit' element={<Unit />} />
                            <Route path='/Product' element={<ProductManagement />} />
                            <Route path='/Supplier' element={<Supplier />} />
                            <Route path='/Client' element={<Client />} />
                            <Route path='/Analytics' element={<StockDashboard />} />
                        </Routes>

                </BrowserRouter>
            </div>
            </Suspense>
        </div>
    );
}

export default App;
