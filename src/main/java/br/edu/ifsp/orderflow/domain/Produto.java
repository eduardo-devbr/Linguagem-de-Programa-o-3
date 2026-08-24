package br.edu.ifsp.orderflow.domain;

import java.math.BigDecimal;

public class Produto {

    private final String id;
    private final  String nome;
    private  final BigDecimal preco;

    public Produto (String id, String nome, BigDecimal preco) {
        this.id = id;
        this.nome = nome;
        this.preco = preco;

    }

    public String getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public BigDecimal getPreco() {
        return preco;
    }

    @Override
    public String toString() {
        return this.nome +" (R$ "  + this.preco +")";
    }
}
