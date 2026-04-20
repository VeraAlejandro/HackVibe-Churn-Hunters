package com.crm.backend.model;

import jakarta.persistence.*;

@Entity
@Table(name = "clients")
public class Client {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int clientId;

    private String first_Name;
    private String last_Name;
    private String email;
    private String phone;

    // Constructor vacío (OBLIGATORIO)
    public Client() {}

    // Getters y Setters manuales

    public int getClientId() {
        return clientId;
    }

    public void setClientId(int clientId) {
        this.clientId = clientId;
    }

    public String getFirstName() {
        return first_Name;
    }

    public void setFirstName(String first_Name) {
        this.first_Name = first_Name;
    }

    public String getLastName() {
        return last_Name;
    }

    public void setLastName(String last_Name) {
        this.last_Name = last_Name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
}

//conecta con la tabla clients con cada atirbuto es cada columna   por que JPA lo convierte en objeto JAVA 
