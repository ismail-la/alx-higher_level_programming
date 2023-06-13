#include "lists.h"

/**
 * reverse_listint - it reverses a linked list
 * @head: a pointer to the first node in the list
 * Return: a pointer to the first node in the new list
 *
 */

void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - it checks if a linked list is a palindrome
 * @head: pointer to pointer to the linked list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *temp = *head, *dupp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /* empty list */

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dupp = slow->next;
			break;
		}
		if (!fast->next)
		{
			dupp = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dupp);

		while (dupp && temp)
	{
		if (temp->n == dupp->n)
		{
			dupp = dupp->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dupp)
		return (1);

	return (0);
}
