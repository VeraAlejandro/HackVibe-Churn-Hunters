import { useEffect, useState } from "react";
import { getClients } from "../services/api";
import ClientForm from "../components/ClientForm";

function ClientsPage() {

    const [clients, setClients] = useState([]);

    const loadClients = async () => {
        const res = await getClients();
        setClients(res.data);
    };

    useEffect(() => {
        loadClients();
    }, []);

    return(
        <div className="container mx-auto p-4">
            <h1 className="text-3xl font-bold mb-6 text-gray-800">Clientes</h1>

            <div className="grid md:grid-cols-2 gap-6"></div>

            {/* Formulario */}
            <ClientForm onClientAdded={loadClients} />

            {/* Lista */}
             <div>
        <h2 className="text-xl font-semibold mb-3">Client List</h2>

        {clients.map(c => (
          <div
            key={c.clientId}
            className="bg-white p-4 mb-3 shadow rounded-lg"
          >
            <p className="font-bold">
              {c.firstName} {c.lastName}
            </p>
            <p className="text-gray-600">{c.email}</p>
            <p className="text-gray-500">{c.phone}</p>
          </div>
        ))}
      </div>

    </div>
    );
}

export default ClientsPage;