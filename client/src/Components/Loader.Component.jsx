import React from 'react'


const PreLoader = () => {

    return (
        <div className="flex items-center justify-center h-screen bg-black">
            <div className="relative">
                <div className="h-24 w-24 rounded-full border-t-8 border-b-8 border-red-600"></div>
                <div
                    className="absolute top-0 left-0 h-24 w-24 rounded-full border-t-8 border-b-8 border-gray-100 animate-spin">
                </div>
            </div>
        </div>
    )
}

export {PreLoader}