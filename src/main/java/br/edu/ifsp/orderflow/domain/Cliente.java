package br.edu.ifsp.orderflow.domain;

import java.math.BigDecimal;

public class Cliente {

    private final String id;
    private final  String nome;
    private  final String email;



    public Cliente (String id, String nome, String email) {
        this.id = id;
        this.nome = nome;
        this.email = email;
    }

    public String getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public String toString() {
        return this.nome +"<"  + this.email +">";
    }
}
