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
	listint_t *node = *head, *nw = malloc(sizeof(listint_t));

	if (!nw)
		return (NULL);
	nw->n = number;
	nw->next = NULL;

	if (!node || nw->n < node->n)
	{
		nw->next = node;
		return (*head = nw);
	}
	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			nw->next = node->next;
			node->next = nw;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
