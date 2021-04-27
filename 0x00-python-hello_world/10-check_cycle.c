#include "lists.h"
/**
 * check_cycle - check is a linked list is cycle.
 *
 * @list: head of list
 * Return: Always 0
 */
int check_cycle(listint_t *list)
{
	/* Create two runners */
	/* Assigned each runner your respective speed */
	const listint_t *turtle = list;
	const listint_t *hare = list;
	/* Validate if is the linked list is null and return null */
	if (list == NULL)
		return (0);
	/* Iterate the linked list */
	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next; /* Jump every two lists */
		turtle = turtle->next; /* Jump evry one list  */

		if (turtle == hare) /* Conditional that is valid if it is cycle */
			return (1);
	}
	return (0);
}
