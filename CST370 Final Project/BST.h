#include <iostream>
using namespace std;

#ifndef BINARY_SEARCH_TREE
#define BINARY_SEARCH_TREE

class BST
{
public:
	/***** Function Members *****/
	BST();
	bool empty() const;
	void insert(int array[], int start, int end);
	int findLevel(int item);
	
private:
	/***** Node class *****/
	class BinNode
	{
	public:
		int data;
		BinNode * left;
		BinNode * right;

		// BinNode constructors
		// Default -- data part is default int value; both links are null.
		BinNode()
			: left(0), right(0)
		{}

		// Explicit Value -- data part contains item; both links are null.
		BinNode(int item)
			: data(item), left(0), right(0)
		{}

	};// end of class BinNode declaration

	/***** Data Members *****/
	BinNode * myRoot;
	BinNode* newNode(int data);
	BinNode* insertAux(int array[], int start, int end);
	int findLevelAux(BinNode* subtreeRoot, int item, int level);

}; // end of class declaration

#endif