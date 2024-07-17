[Português](#listas-encadeadas) / [English](#linked-lists)

<div style="text-align: center;">

# Linked Lists

</div>

### Behavior

When we have a linked list, all items are stored such that each of them points to the location of the next element in the list (singly linked list). The list only knows its first element (head). Its last element (tail) which does not point to any element, indicating the end of the list. See the image below:

![Singly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/C_language_linked_list.png/438px-C_language_linked_list.png)

Given this constructive principle, to search and check if a certain element is contained in the list, we need to traverse the entire list to verify its presence or absence. This allows us to identify the time required to execute actions within the lists.

### Complexities

To evaluate the execution time of tasks, we commonly use the *Big(O)* notation for analysis. In the case of singly linked lists, we have the following analyses:

* **Insertion Time at the Top:** inserting information at the top of the linked list has a time complexity of O(1), as it is constant since, regardless of the size of the list, it is enough to reference the new element as the top and the element that was previously the top as the next in the list.
* **Insertion Time in the Middle/End:** unlike inserting at the top, inserting at the end or middle of the list results in a complexity of Big(O(n)) because it is necessary to traverse each item to identify the next one, and the time varies according to the number of items linked in the list.
* **Removal Time at the Top:** removing information from the top of the linked list has a time complexity of Big(O(1)). It works the same way as insertion but now removes the first item and sets the following item as the first.
* **Removal Time in the Middle/End:** removing in the middle or end results in a complexity of Big(O(n)). It works the same way as insertion but now we need to remove an item after finding it.
* **Reading Items in the List:** since it is necessary to traverse the list to find the desired item, the complexity is Big(O(n)).

### Applied Example

In this example, we have a linked list working like a medical clinic queue. Each person in line receives a card that has a color and a number.

Cards have two colors:

- Yellows
- Greens

This queue has a priority system, where yellow cards have priority over green cards, that is, whenever a patient with a yellow card is registered, they must have priority over patients who received green cards.

Cards have their own way of generating numbers:

- Yellow -> must start from number 201
- Green -> must start from number 1

In the program we have the following options:

- 1 -> Add a patient to the queue
- 2 -> Show the current patient queue
- 3 -> Serve the next patient in the queue (removes the first card from the linked list)

<br />

---

---

<br />

<div style="text-align: center;">

# Listas Encadeadas

</div>

### Funcionamento

Quando temos uma lista encadeada, todos os itens são armazenados e cada deles apontam para a localização do próximo elemento dessa lista (lista simplesmente encadeada), a lista conhece somente o seu primeiro elemento (head). Seu último elemento (tail) não aponta para nenhum elemento, indicando o final da lista. Veja a imagem abaixo:

![Lista Simplesmente Encadeada](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/C_language_linked_list.png/438px-C_language_linked_list.png)

Dado esse princípio construtivo, para fazer uma busca e verificar se determinado elemento está contido na lista precisamos percorrer por toda a lista e verificar se ele está presente ou não. Com isso, é possível identifcar o tempo necessário para executar ações dentro das listas.

### Complexidades

Para avaliar o tempo de execução de tarefas, comumente utilizamos a notação *Big(O)* para análise. No caso das listas simplesmente encadeadas, temos as seguintes análises:
* **Tempo de Inserção no Topo:** para inserir informações no topo da lista encadeada tem-se um tempo de complexidade de O(1), pois é constante já que, independente do tamanho da lista, basta referenciar o novo elemento como topo e o elemento que era o topo anteriormente como o próximo da lista.
* **Tempo de Inserção no no Meio/Final:** diferentemente de inserir no topo, a inserção no fim ou meio da lista gera uma complexidade de O(n) pois, como é ncessário percorrer cada item para identificar o próximo, o tempo varia de acordo com a quantidade de itens encadeados na lista.
* **Tempo de Remoção no Topo:** para remover informações no topo da lista encadeada tem-se um tempo de complexidade de O(1). Mesmo funcionamento da inserção porém agora removendo o primeiro item e definindo o seguinte como primeiro
* **Tempo de Remoção no no Meio/Final:** para remover no meio ou fim gera uma complexidade de O(n). Mesmo funcionamento da inserção porém agora precisamos remover um item depois de encotrá-lo.
* **Ler Items na Lista:** como é necessário percorrer a lista para encontrar o item desejado, tem-se complexidade de O(n).

### Exemplo Aplicado
Neste exemplo, temos uma lista encadeada trabalhando como uma fila de atendimento de uma clínica médica. Cada pessoa na fila recebe um cartão que possui uma cor e uma numeração.

Cartões possuem duas cores:

- Amarelos
- Verdes

Essa fila possui um sistema de prioridades, onde os cartões amarelos possuem prioridades sobre cartões verdes, ou seja, sempre que for cadastrado um paciente com cartão de cor amarela ele deverá ter prioridade sobre os pacientes que receberam o cartões de cor verde.

Os cartões tem sua própria forma de gerar números:

- Amarelos -> devem iniciar a partir do número 201
- Verdes -> devem iniciar a partir do número 1

No programa temos as seguintes opções:

- 1 -> Inserir um paciente na fila
- 2 -> Mostrar a fila de pacientes no momento
- 3 -> Atender o próximo paciente da fila (remove o primeiro cartão da lista encadeada)
