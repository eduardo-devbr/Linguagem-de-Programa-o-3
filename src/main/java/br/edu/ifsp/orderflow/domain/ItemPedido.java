package br.edu.ifsp.orderflow.domain;

public class ItemPedido {

    Produto proiduti;
    Quantidade int;

    private final Produto produto;
    private final  int quantidade;


    public ItemPedido(Produto produto;, int quantidade) {

        this.produto = produto;
        this.quantidade = quantidade;
    }

    public Produto getProiduti() {
        return proiduti;
    }

    public Produto getProduto() {
        return produto;
    }
}
