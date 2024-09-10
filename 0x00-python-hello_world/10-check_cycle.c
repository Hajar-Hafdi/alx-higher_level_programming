#include "lists.h"

/**
 * check_cycle - verifies if a linked list has a cyrcle
 *
 * @list: linked list to be verified
 *
 * Return: returns 1 if the linked list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);
	while (s && f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0)
}
