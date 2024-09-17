#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - parses rec pal 
 *
 * @head: head list
 *
 * Return: 1 if it's a pall an 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palindrome(head, *head));
}
/**
 * check_palindrome - function to verify if is pal
 *
 * @head: hd lst
 * @end: end lst
 */
int check_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (check_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
