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
	_new = malloc(sizeof(listint_t));
	if (_new == NULL)
		return (NULL);
	_new->n = number;

	if (node == NULL || node->n >= number)
	{
		_new->next = node;
		*head = _new;
		return (_new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	_new->next = node->next;
	node->next = _new;

	return (_new);
}
