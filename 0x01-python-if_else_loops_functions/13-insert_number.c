#include "lists.h"
#include <stdlib.h>

/*
 * insert_node - inserts nd in srtd lst
 *
 * @head: add of hd ptr
 * @number: num to be inserted
 *
 * Return: returns inserted nd
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!node || new->n < node->n)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node->next && new->n < node->next->n)
	{
		node = node->next;
	}
	new->next = node->next;
	node->next = new;
	
	return (new);
}
