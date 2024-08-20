import axios from "axios";
import {url} from "../Utililties";

const BaseUrl = `${url}`;



const Create = async (data,path) => {
  try {
    const response = await axios.post(
      `${BaseUrl}/${path}/create`,
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

const Update = async (id,data, path)=>{
    try {
    const response = await axios.put(
      `${BaseUrl}/${path}/update/${id}`,
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
const Delete = async (id,path)=>{
    try {
    const response = await axios.delete(
      `${BaseUrl}/${path}/delete/${id}`,
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

const Get = (id, path)=>{

}

const GetAll = async(path) =>{
    try {
    const response = await axios.get(
      `${BaseUrl}/${path}/list`,
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
    Create,
    Update,
    Delete,
    Get,
    GetAll
}