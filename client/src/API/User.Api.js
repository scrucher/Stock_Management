import {url} from "../Utililties/Config";

const CreateUser = (data) => {
    const response = async (data) => {
        try {
            const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            console.log(response)
            return await response.json();

        }catch (e) {
            console.log(e);
            return ({'error': e});
        }
    }

}

const DeleteUser = () => {

}

const UpdateUser = () => {

}

const GetUsers = () => {

}

const GetUser = () => {

}


export {
    CreateUser,
    DeleteUser,
    UpdateUser,
    GetUser,
    GetUsers
}