import axios from "axios";

const BarCodeApi = async (code) => {
    try {
        const response = await axios.get(`https://world.openfoodfacts.org/api/v3/product/${code}.json`, {
            headers: {
                'Content-Type': 'application/json',
            }
        });
        const data = response.data; // Access the data property to get the actual JSON data
        console.log({'BarCodeData': data});
        return data;
    } catch (e) {
        console.log({'BarCodeError': e});
        throw e; // Re-throw the error if needed for further handling
    }
}

export {
    BarCodeApi,
}