package com.crm.backend.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
public class SecurityConfig {
    
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {

        http
            .csrf(csrf -> csrf.disable()) //con esto se desactiva la proteccion CSRF
            .authorizeHttpRequests(auth -> auth
                .anyRequest().permitAll() //permite estar sin login
            
            );
        return http.build();
    }
}
