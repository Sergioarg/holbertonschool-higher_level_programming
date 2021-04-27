#include "list.h"
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
	listint_t *turtle = list;
	listint_t *hare = list;
	/* Validate if is the linked list is null and return null */
	/* Iterate the linked list */
	if (list == NULL)
		return (0);
	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		turtle = turtle->next;

		if (turtle == hare)
			return (1);
	}
	return (0);
}
