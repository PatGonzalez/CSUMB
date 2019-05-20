//#include "pch.h"
#include <iostream>
#include <iomanip>

using namespace std;

#include "BST.h"

//--- Definition of constructor
BST::BST()
	: myRoot(0)
{}

bool BST::empty() const
{
	return myRoot == 0;
}

//Create new node to insert into tree
BST::BinNode* BST::newNode(int data)
{
	BinNode* node = new BinNode(data);
	node->left = NULL;
	node->right = NULL;

	return node;
}

/*******************  Part 2 ***************************/
void BST::insert(int array[], int start, int end)
{
	myRoot = insertAux(array, start, end);
}

BST::BinNode* BST::insertAux(int array[], int start, int end)
{
	//End of recurssion
	if (start > end)
	{
		return NULL;
	}

	//Middle = Root
	int mid = (start + end) / 2;
	BinNode* root = newNode(array[mid]);

	//Recursive on the left side
	root->left = insertAux(array, start, mid - 1);

	//Recursive on the right side
	root->right = insertAux(array, mid + 1, end);


	return root;
}

/*******************  Part 2 ***************************/

int BST::findLevel(int item)
{
	return findLevelAux(myRoot, item, 0);
}

int BST::findLevelAux(BinNode* subtreeRoot, int item, int level)
{
	//Base case
	if (subtreeRoot == 0)
	{
		return 0;
	}

	//Item found
	if (subtreeRoot->data == item)
	{
		return level;
	}

	// Recursive on the left side
	int nextLevel = findLevelAux(subtreeRoot->left, item, level + 1);

	if (nextLevel != 0)
	{
		return nextLevel;
	}

	//Recursive on the right side
	nextLevel = findLevelAux(subtreeRoot->right, item, level + 1);
	return nextLevel;
}