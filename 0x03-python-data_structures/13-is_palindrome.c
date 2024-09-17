#include "lists.h"
#include <stdlib.h>

/**
 *  * reverse_list - Reverses a singly linked list.
 *   *
 *    * @head: Pointer to the pointer to the head of the list.
 *     *
 *      * Return: Pointer to the new head of the reversed list.
 *       */
listint_t *reverse_list(listint_t **head)
{
	    listint_t *prev = NULL;
	        listint_t *current = *head;
		    listint_t *next = NULL;

		        while (current != NULL)
				    {
					            next = current->next;
						            current->next = prev;
							            prev = current;
								            current = next;
									        }
			    *head = prev;
			        return *head;
}

/**
 *  * is_palindrome - Checks if a singly linked list is a palindrome.
 *   *
 *    * @head: Pointer to the pointer to the head of the list.
 *     *
 *      * Return: 1 if the list is a palindrome, 0 otherwise.
 *       */
int is_palindrome(listint_t **head)
{
	    listint_t *slow = *head, *fast = *head, *second_half, *first_half;
	        int palindrome = 1;

		    if (head == NULL || *head == NULL || (*head)->next == NULL)
			            return 1;

		        /* Find the middle of the list */
		        while (fast != NULL && fast->next != NULL)
				    {
					            fast = fast->next->next;
						            slow = slow->next;
							        }

			    /* Reverse the second half */
			    second_half = reverse_list(&slow);

			        /* Compare the first and second half */
			        first_half = *head;
				    while (second_half != NULL)
					        {
							        if (first_half->n != second_half->n)
									        {
											            palindrome = 0;
												                break;
														        }
								        first_half = first_half->next;
									        second_half = second_half->next;
										    }

				        /* Restore the original list */
				        reverse_list(&slow);

					    return palindrome;
}

