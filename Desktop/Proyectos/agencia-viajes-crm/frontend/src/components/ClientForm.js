import { useState } from "react";
import { createClient } from  "../services/api";

function ClientForm({ onClientAdded }) {

    //estado del formulario 
    const [form, setForm] = useState({
        firstName: "",
        lastName: "",
        email: "",
        phone: ""
    });

    //manejar cambios en imputs
    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value
        });
    };

    //enviar fromulario 
    const handleSubmit = async (e) => {
        e.preventDefault();

        try{
            await createClient(form);

            //limpiar formulario 
            setForm({
                firstName: "",
                lastName: "",
                email: "",
                phone: ""
            });

            //actualizar lista en el padre 
            onClientAdded();

        }catch(error){
            console.error("Error al crear cliente:", error); 

        }
    };

    return(
        <form onSubmit={handleSubmit} className="bg-white p-6 shadow-lg rounded-lg max-w-md">
        
            <h2 className="text-2xl font-bold mb-4 text-gray-700">Añadir Client</h2>

            <input
                name = "firstName"
                value = {form.firstName} 
                onChange = {handleChange}
                placeholder = "First Name"
                className="border border-gray-300 p-2 w-full mb-3 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
            />
            
            <input
                name = "lastName"
                value = {form.lastName} 
                onChange = {handleChange}
                placeholder = "Last Name"
                className="border border-gray-300 p-2 w-full mb-3 rounded"
            />

            <input
                name = "email"
                value = {form.email} 
                onChange = {handleChange}
                placeholder = "Email"
                className="border border-gray-300 p-2 w-full mb-3 rounded"
            />

            <input
                name = "phone"
                value = {form.phone} 
                onChange = {handleChange}
                placeholder = "Phone"
                className="border border-gray-300 p-2 w-full mb-3 rounded"
            />

            <button className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded w-full">
                Guardar
            </button>

        </form>
    );
}

export default ClientForm;