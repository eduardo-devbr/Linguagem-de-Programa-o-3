# OrderFlow

Projeto da disciplina **Linguagem de Programação 3 (SPOLPG3)**
IFSP, Câmpus São Paulo
Tecnologia em Análise e Desenvolvimento de Sistemas, 2026/2
Prof. Ronaldo Nogueira

## Sobre o projeto

O OrderFlow simula o processamento de pedidos de uma loja.

Inicialmente, todo pedido percorre o seguinte fluxo:

> **validar → reservar estoque → pagar → notificar**

Um pedido pode ser pago ou cancelado por falta de estoque ou por recusa do pagamento. Nesse último caso, o estoque que já tiver sido reservado precisa ser devolvido.

O projeto será o **fio condutor da disciplina**. Em vez de trabalharmos apenas com exemplos isolados, vamos evoluir o mesmo sistema ao longo do semestre.

Threads, sincronização, filas, `ExecutorService`, `CompletableFuture`, programação funcional, atores, programação reativa, reflexão, anotações e outros conteúdos serão introduzidos conforme surgirem problemas que façam sentido resolver com essas ferramentas.

### Algumas escolhas do projeto

Não usaremos Spring, banco de dados ou HTTP. O objetivo é trabalhar diretamente com Java e observar com mais clareza os diferentes modelos de execução.

Algumas operações externas também serão simuladas com atrasos controlados. Por exemplo, o pagamento e o envio de notificações terão tempos de espera artificiais para representar operações de I/O.

Esses tempos serão importantes quando começarmos a analisar desempenho e concorrência.

## Estado inicial

O projeto começa propositalmente simples, contendo apenas o `pom.xml` e uma classe `Main` para verificar o ambiente.

A partir do **Encontro 3**, começaremos a implementar o domínio, os contratos entre os componentes e o primeiro fluxo completo de processamento de pedidos.

## Como executar

### Requisitos

* JDK 21 ou superior
* Maven 3.8 ou superior
* IntelliJ IDEA, Eclipse ou outra IDE com suporte a Maven

### Pela IDE

Abra a pasta como um projeto Maven e execute a classe `Main`.

### Pelo terminal

```bash
mvn -q compile
java -cp target/classes br.edu.ifsp.orderflow.Main
```

Saída esperada:

```text
OrderFlow - LP3 (IFSP Campus Sao Paulo) - 2026/2
Ambiente OK. Java 17.x (ou superior)
Pronto para o Encontro 3.
```

## Histórico das aulas

O repositório oficial terá uma tag correspondente ao estado do projeto ao final de cada encontro:

```text
aula-03
aula-04
aula-05
...
```

Para consultar o projeto como estava em uma aula específica:

```bash
git checkout aula-03
```

Para voltar à versão atual:

```bash
git switch main
```

## Convenção de nomes

Neste projeto, a regra geral será:

> **o domínio fala português; os papéis técnicos falam inglês.**

Conceitos do problema ficam em português:

```java
Pedido
ItemPedido
Produto
Cliente
StatusPedido

processar()
reservar()
pagar()
notificar()
```

Papéis técnicos comuns em projetos Java permanecem em inglês:

```java
PedidoService
PedidoRepository
FakePagamentoGateway
EventBus
```

Também usaremos nomes técnicos como `Service`, `Repository`, `Gateway`, `Handler`, `InMemory`, `Fake` e `Async`.

Um critério simples é pensar:

> Se o nome faz parte do negócio, português. Se representa um papel técnico comum em Java, inglês.

Os identificadores também serão escritos sem acentos, por exemplo:

```java
preco
notificacao
validacao
```
