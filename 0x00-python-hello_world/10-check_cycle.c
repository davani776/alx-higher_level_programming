#include "lists.h"
#include <stdbool.h>
/**
 * check_cycle - entry point
 * @list: linked list 
 *
 * Return: True if the list has a cycle, otherwise False
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	if (!list)
		return (false);
	while ((slow) && (fast) && (fast->next))
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (true);
	}
	return (0);
}
