#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - verifies if a linked list has a cyrcle
 *
 * @list: linked list to be verified
 *
 * Return: returns 1 if the linked list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0)
}
