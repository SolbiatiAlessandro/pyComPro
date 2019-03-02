// I don't use C++ as my main language, so this template is pretty dumb, and helps me to remember basic syntax (W PYTHON)
#include <iostream>
#include <cmath>
#include <algorithm>
#include <limits>
#include <vector>
#include <bitset>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <time.h>
using namespace std;
#define ll long long

const ll MAXN = 1000009;

ll N, colors[MAXN], out;
vector< ll > adj[MAXN];
vector< vector< int > > br(MAXN);

void dfs(ll node, ll parent){
	for(auto i: adj[node]) if(i != parent){
		dfs(i, node);
		br[node][1] += br[i][1];
		br[node][2] += br[i][2];
	}
}


int main () {
	cin >> N;
	for(ll i = 0; i < N; i++){
		cin >> colors[i];
		br[i].push_back(0);
		br[i].push_back(0);
		br[i].push_back(0);
		br[i][colors[i]]++;
	}

	for(ll i = 1; i < N; i++){
		ll u, v, c;
		cin >> u >> v;
		u--; v--;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}
	dfs(0, -1);

	for(ll node = 1; node < N; node++){
		pair<ll, ll> first_subtree(br[0][1] - br[node][1], br[0][2] - br[node][2]);
		pair<ll, ll> second_subtree(br[node][1], br[node][2]);
		if(first_subtree.first != 0 && first_subtree.second!= 0) continue;
		if(second_subtree.first != 0 && second_subtree.second!= 0) continue;
		out++;
	}
	cout << out << endl;

	return 0;
}
