[Português](#tabelas-hash) / [English](#hash-tables)

<div style="text-align: center;">

# Hash Tables

</div>

In this example we have a hash table with 10 positions that varies according to the value described in this part of the code:

```py
hash_table = Hash_table(10)
```

In this table, each position is composed of a linked list, where each node in this linked list stores its state that contains the following characteristics:
* State acronym
* State name

To generate the hash code and determine where the state will be stored, the following encoding was used:

```py
(acronym_char0 + acronym_char1) MOD 10
```

This will generate the position where the state will be allocated. It will then be inserted at the top of the corresponding linked list.

There is only one condition in which the state of the Federal District must be included in position 7 of the table.

<br />

-------------------------------------------------- 

-------------------------------------------------- 

<br />

<div style="text-align: center;">

# Tabelas Hash

</div>

Nesse exemplo temos uma tablea hash com 10 posições que varia de acordo com o valor descrito nessa parte do código:

```py
hash_table = Hash_table(10)
```

Nessa tabela, cada posição é composta por uma lista encadeada, onde cada nó dessa lista encadeada armazena o seu estado que contém as seguintes características:
* Sigla do estado
* Nome do estado

Para gerar o código hash e determinar onde o estado será armazenado, foi utilizada a seguinte codificação:

```py
(sigla_char0 + sigla_char1) MOD 10
```

Com isso será gerado a posição onde o estado será alocado. Em seguida, ele será inserido no topo da lista encadeada correspondente.

Há somente uma condição em que o estado do Distrito Federal deve ser incluído na posição 7 da tabela.