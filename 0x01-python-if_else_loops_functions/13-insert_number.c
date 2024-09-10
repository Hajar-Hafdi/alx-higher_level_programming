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
	listint_t *nd = *head, *nw = malloc(sizeof(listint_t));

	if (!nw)
		return (NULL);
	nw->n number;
	nw->next = NULL;

	if (!nd || nw->n < nd->n)
	{
		nw->next = nd;
		return (*head = nw);
	}
	while (nd)
	{
		if (!nd->next || new->n < nd->next->n)
		{
			nw->next = nd->next;
			nd->next = nw;
			return (nd);
		}
		nd = nd->next;
	}
	return (NULL);
}
