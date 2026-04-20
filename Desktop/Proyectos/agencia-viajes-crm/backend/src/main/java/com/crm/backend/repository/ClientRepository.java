package com.crm.backend.repository;

import com.crm.backend.model.Client;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ClientRepository extends JpaRepository<Client, Integer>{
}

//aqui ya tengo el CRUD sin sql comands 