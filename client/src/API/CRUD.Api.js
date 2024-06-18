import axios from "axios";


const url = 'http://localhost:5000/Category';



const CreateCategory = async (data) => {
  try {
    const response = await axios.post(
      `${url}/create`,
      JSON.stringify(data),
      {
        headers: {
          'Content-Type': 'application/json'
        }
      }
    );
    console.log('Response data:', response.status);
    return response.data;
  } catch (error) {
    console.error('Error creating category:', error.message);
    console.error('Error details:', error);
    throw error;
  }
};

const UpdateCategory = async (id,data)=>{
    try {
    const response = await axios.put(
      `${url}/update/${id}`,
      JSON.stringify(data),
      {
        headers: {
          'Content-Type': 'application/json'
        }
      }
    );
    console.log('Response data:', response.status);
    return response.data;
  } catch (error) {
    console.error('Error creating category:', error.message);
    console.error('Error details:', error);
    throw error;
  }
}
const DeleteCategory = async (id)=>{
    try {
    const response = await axios.delete(
      `${url}/delete/${id}`,
      {
        headers: {
          'Content-Type': 'application/json'
        }
      }
    );
    console.log('Response data:', response.status);
    return response.data;
  } catch (error) {
    console.error('Error creating category:', error.message);
    console.error('Error details:', error);
    throw error;
  }
}

const GetCategory = ()=>{

}

const GetCategories = async() =>{
    try {
    const response = await axios.get(
      `${url}/list`,
      {
        headers: {
          'Content-Type': 'application/json'
        }
      }
    );
    console.log('Response data:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error creating category:', error.message);
    console.error('Error details:', error);
    throw error;
  }
}


export {
    CreateCategory,
    UpdateCategory,
    DeleteCategory,
    GetCategory,
    GetCategories
}