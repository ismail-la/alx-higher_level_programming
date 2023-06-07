#include "lists.h"

/**
 * insert_node - Inserts a number into
 * a sorted singly-linked list
 * @head: A pointer the head of the linked list
 * @number: The number to insert
 *
 * Return: If the function fails - NULL
 * Otherwise - a pointer to the new node
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	nnew = malloc(sizeof(listint_t));
	if (nnew == NULL)
		return (NULL);
	nnew->n = number;

	if (node == NULL || node->n >= number)
	{
		nnew->next = node;
		*head = nnew;
		return (nnew);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	nnew->next = node->next;
	node->next = nnew;

	return (nnew);
}
