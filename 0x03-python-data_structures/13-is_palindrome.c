#include "lists.h"

/**
 * is_palindrom - parses rec pal 
 *
 * @head: head list
 *
 * Return: 1 if it's a pall an 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (x_pal(head, *head));
}
/**
 * x_pal - function to verify if is pal
 *
 * @hed: hd lst
 * @ennd: end lst
 */
int x_pal(listint_t **hed, listint_t *ennd)
{
	if (end == NULL)
		return (1);
	if (x_pal(hed, ennd->next) && (*hed)->n == ennd->n)
	{
		*hed = (*hed)->next;
		return (1);
	}
	return (0);
}