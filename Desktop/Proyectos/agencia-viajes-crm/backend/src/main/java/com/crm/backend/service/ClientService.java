package com.crm.backend.service;

import com.crm.backend.model.Client;
import com.crm.backend.repository.ClientRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ClientService{

    private final ClientRepository repository;

    public ClientService(ClientRepository repository) {
        this.repository = repository;
    }

    public List<Client> getAllClients() {
        return repository.findAll();
    }

    public Client saveClient(Client client){
        return repository.save(client);
    }
}