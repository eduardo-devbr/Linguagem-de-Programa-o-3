package br.edu.ifsp.orderflow;


import br.edu.ifsp.orderflow.domain.Produto;

import java.math.BigDecimal;

public class Main {

    public static void main(String[] args) {
       Produto mouse = new Produto(
               "SKU-1",
               "Mouse sem fio",
               new BigDecimal("120.00"));

       Produto teclado = new Produto (
               "SKU-2",
               "Teclado mecanico",
               new BigDecimal("120.00"));

       Produto monitor = new Produto (
                "SKU-3",
                "Monitor 27",
                new BigDecimal("180.00"));

       System.out.println(mouse);
       System.out.println(teclado);
       System.out.println(monitor);



    }
}

