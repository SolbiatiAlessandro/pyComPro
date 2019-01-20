#include <cstdio>
#include <complex>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <iomanip>
#include <cassert>
#include <bitset>
#include <queue>
#include <list>
#include <ctime>
#include <sstream>
#include <stack>
using namespace std;
#define range(n) for (int i=0;i<n;i++)

int cols, rows, num_players;
int speeds[10];
int matrix[1010][1010];
char str[1010];
int res[10];

int main(){
	scanf("%d%d%d",&cols,&rows,&num_players);
	range(num_players) scanf("%d",&speeds[i]);
	memset(matrix, -1, sizeof(int) * 1010 * 1010);
	memset(res, 0, sizeof(res));

	for(int i = 0; i < cols; i++){
		scanf("%s", str);
		for(int j = 0; j < rows; j++){
			char cc = str[j];
			if(cc == '#') matrix[i][j] = 0;
			else if(cc != '.'){
				matrix[i][j] = (int) cc - (int)'0';
				res[(int) cc - (int)'1'] += 1;
			}
		}
	}

	range(num_players){
		printf("%d ",res[i]);
	}

}
