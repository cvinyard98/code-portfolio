#include <iostream>
#include <string>
#include <vector>

using namespace std;


class Player {
	public:
		string name;
		char piece;
};


bool checkLine(vector<char>);
void printBoard(vector< vector<char>> &board);
void startGame();
string makePlayer();
void mainGameLoop(Player &p1, Player &p2);
bool gameOver(vector< vector<char>> &board, int);

int main(){
	startGame();
}


void startGame(){
	Player p1;
	Player p2;
	p1.name = makePlayer();
	p1.piece = 'X';
	p2.name = makePlayer();
	p2.piece = 'O';
	
	mainGameLoop(p1, p2);
}

void mainGameLoop(Player &p1, Player &p2){
	int n = 7;
	int m = 6;
	vector< vector<char> > board(n, vector<char> (m, ' '));
	int play = 0;
	int turn = 0;

	while (!gameOver(board, play)){
		printBoard(board);
		cout << "Which row (1-7)? ";
		cin >> play;
		--play;
		bool placed = false;

		for(int i = 0; i < 6; ++i){
			if((i == 6 || board[play][i + 1] != ' ') && !placed){
				if(turn % 2 == 0){
					board[play][i] = p1.piece;
				}
				else{
					board[play][i] = p2.piece;
				}
				placed = true;
			}
		}

		++turn;
	}
	

	printBoard(board);

	if (turn % 2 == 1){
		cout << p1.name << " Wins!\n";
	}
	else{
		cout << p2.name << " Wins!\n";
	}
	cout << "Congratulations!\n";
}

void printBoard(vector< vector<char>> &board){
	string line = "";
	for(int i = 0; i < 6; ++i){
		printf("%c %c %c %c %c %c %c \n", board[0][i], board[1][i], board[2][i], board[3][i], board[4][i], board[5][i], board[6][i]);
	}
	printf("1 2 3 4 5 6 7 \n\n");
}

bool gameOver(vector< vector<char>> &board, int play){
	vector<char> vertical;
	vector<char> horizontal;
	vector<char> DR;
	vector<char> UR;
	int row = 10;
	
	bool rowFound = false;
	bool full = true;
	for (int i = 0; i < 7; ++i){
		for (int j = 0; j < 6; ++j){
			if(board[i][j] == ' '){
				full = false;
			}
		}
	}
	
	for (int i = 0; i < 6; ++i){
		vertical.push_back(board[play][i]);
		if(!rowFound && board[play][i] != ' '){
			row = i;
			rowFound = true;
		}
	}
	int DRstart = row - play;
	int URstart = row + play;
	if (row != 10){
		for (int i = 0; i < 7; ++ i){
			horizontal.push_back(board[i][row]);
			if(DRstart + i >= 0){
				DR.push_back(board[i][DRstart + i]);
			}
			if(URstart - i <= 5){
				UR.push_back(board[i][URstart - i]);
			}
		}
	}
	return(checkLine(vertical) || checkLine(horizontal) || checkLine(UR) || checkLine(DR) || full);
	


}

bool checkLine(vector<char> line){
	if(line.size() < 4){
		return(false);
	}

	for (int i = 0; i < int(line.size()) - 3 ; ++i){
		if(line[i] != ' ' && line[i] == line[i + 1] && line[i] == line[i + 2] && line[i] == line[i + 3]){
			return(true);
		}
	}
	return(false);
}

string makePlayer(){
	string name;
	cout << "Enter Name: ";
	cin >> name;
	return name;
}
