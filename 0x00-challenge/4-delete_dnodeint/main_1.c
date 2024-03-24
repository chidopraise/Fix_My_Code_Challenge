#include <stdio.h>
#include <stdlib.h>

/* Structure for a doubly linked list node */
typedef struct DListNode {
	int data;
	struct DListNode *prev;
	struct DListNode *next;
} DListNode;

/* Function to create a new doubly linked list node */
DListNode *createNode(int data) {
	DListNode *newNode = (DListNode *)malloc(sizeof(DListNode));
	if (newNode == NULL) {
		fprintf(stderr, "Memory allocation failed\n");
		exit(EXIT_FAILURE);
	}
	newNode->data = data;
	newNode->prev = NULL;
	newNode->next = NULL;
	return newNode;
}

/* Function to insert a node at the end of a doubly linked list */
void insertAtEnd(DListNode **head, int data) {
	DListNode *newNode = createNode(data);
	if (*head == NULL) {
		*head = newNode;
	} else {
		DListNode *current = *head;
		while (current->next != NULL) {
			current = current->next;
		}
		current->next = newNode;
		newNode->prev = current;
	}
}

/* Function to print the elements of a doubly linked list */
void printList(DListNode *head) {
	while (head != NULL) {
		printf("%d\n", head->data);
		head = head->next;
	}
}

/* Function to free memory allocated for a doubly linked list */
void freeList(DListNode *head) {
	DListNode *temp;
	while (head != NULL) {
		temp = head;
		head = head->next;
		free(temp);
	}
}

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
	int array[] = {0, 1, 2, 3, 4, 98, 402, 1024};
	int n = sizeof(array) / sizeof(array[0]);
	int i, j;

	for (i = 0; i < n; i++)
	{
		for (j = i; j < n; j++)
		{
			printf("%d\n", array[j]);
		}
		printf("-----------------\n");
	}

	return (0);
}
