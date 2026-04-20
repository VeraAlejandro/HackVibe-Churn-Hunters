package com.crm.backend.controller;

import com.crm.backend.model.Client;
import com.crm.backend.service.ClientService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/clients")
@CrossOrigin
public class ClientController{

    private final ClientService service;

    public ClientController(ClientService service) {
        this.service = service;
    }

    @GetMapping
    public List<Client> getClients() {
        return service.getAllClients();
    }

    @PostMapping
    public Client createClient(@RequestBody Client client){
        return service.saveClient(client);
    }

}




