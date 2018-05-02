// TicTacToe.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream> 
#include <string>
#include <vector>

using namespace std;

struct Board {
	int size = 3;
	vector<vector<char>> board;
	void Initialize()
	{
		vector <char> a;

		for (int i = 0; i < 3; i++) {
			board.push_back(a); 
			for (int j = 0; j < 3; j++)
				board[i].push_back(' ');
		}

	}
	void ReSet(Board val)
	{
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++)
				board[i][j] = val.board[i][j];
		}
	}
	void Print()
	{
		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++)
				cout << board[i][j] << '\t';
			cout << endl; 
		}
	}
	bool Set(int i, int j, char piece)
	{
		if (board[i][j] == ' ')
		{
			board[i][j] = piece;
			return true;
		}
		else return false;
	}

	int Active()
	{

		for (int i = 0; i < size; i++)
			if ((board[i][0] == 'X' && board[i][1] == 'X' && board[i][2] == 'X') || (board[i][0] == 'O' && board[i][1] == 'O' && board[i][2] == 'O'))
				if (board[i][0] == 'X')
					return -1;
				else
					return 1;
		for (int i = 0; i < size; i++)
			if ((board[0][i] == 'X' && board[1][i] == 'X' && board[2][i] == 'X') || (board[0][i] == 'O' && board[1][i] == 'O' && board[2][i] == 'O'))
				if (board[0][i] == 'X')
					return -1;
				else
					return 1;
		if (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X')
			return -1;
		else if (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O')
			return 1;
		else if (board[2][0] == 'X' && board[1][1] == 'X' && board[0][2] == 'X')
			return -1;
		else if (board[2][0] == 'O' && board[1][1] == 'O' && board[0][2] == 'O')
			return 1;
		for (int i = 0; i < 3; i++)
		{
			for (int j = 0; j < 3; j++)
			{
				if (board[i][j] == ' ')
					return -4; 
			}
		}
		return 0; 
	}
};
pair<Board,int> BestMove(Board val, bool CPUTurn, bool first = false)
{
	int active = val.Active(); 
	if (active != -4) {
		return make_pair(val, active);
	}
	pair<Board, int> maxmin; 
	if (CPUTurn)
		maxmin.second = -232;
	else
		maxmin.second = 342; 
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			if (val.board[i][j] == ' ')
			{
				if (CPUTurn) {
					val.Set(i, j, 'O');
					pair<Board, int> temp = BestMove(val, !CPUTurn);
					val.board[i][j] = ' ';
					if (!first)
						temp.first = val; 
					if (temp.second == 1)
						return temp; 
					if (temp.second > maxmin.second)
						maxmin = temp; 
				}
				else
				{
					val.Set(i, j, 'X');
					pair<Board, int> temp = BestMove(val, !CPUTurn);
					val.board[i][j] = ' ';
					if (!first)
						temp.first = val;
					if (temp.second < maxmin.second)
						maxmin = temp;
				}
			}
		}
	}
	return maxmin; 
}
int main()
{
	Board CurrentBoard; 
	CurrentBoard.Initialize(); 
	cout << "Are you going first? (y/n): "; 
	char first; 
	cin >> first; 
	if (first == 'n')
	{
		CurrentBoard.Set(1, 1, 'O'); 
		CurrentBoard.Print(); 
	}
	while (CurrentBoard.Active() == -4)
	{
		cout << "Set a Move: "; 
		int x, y; 
		cin >> x >> y; 
		CurrentBoard.Set(x, y, 'X');
		CurrentBoard.Print(); 
		if (CurrentBoard.Active() != -4)
			break; 
		//BestMove(CurrentBoard, true, true).first.Print(); 
		CurrentBoard.ReSet(BestMove(CurrentBoard,true, true).first); 
		CurrentBoard.Print(); 
	}
	if (CurrentBoard.Active() == 1)
		cout << "Sorry You Lost";
	else
		cout << "Draw"; 
    return 0;
}

