/*Centraliza llamadas
Escalable (luego login, tokens, etc.)*/
import axios from "axios";

//configuracion base de axios
const API = axios.create ({
    baseURL: "http://localhost:8080/api"
});

//obtener clientes
export const getClients = () => API.get("/clients");

//crear cliente 
export const createClient = (data) => API.post("/clients", data);

export default API;