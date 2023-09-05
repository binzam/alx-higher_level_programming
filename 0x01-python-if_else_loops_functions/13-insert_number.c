#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted list.
 * @head: A pointer the head of the linked list.
 * @number: number to insert.
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;

	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}

	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (new);
		}
		node = node->next;
	}
	return (NULL);
}
