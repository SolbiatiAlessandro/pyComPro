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

ll N, dp[MAXN], out;
vector< pair<ll, ll> > adj[MAXN];

void dfs(ll node, ll parent){
}

int main () {
	cin >> N;
	for(ll i = 0; i < N; i++){
		cin >> dp[i];
	}
	for(ll i = 1; i < N; i++){
		ll u, v, c;
		cin >> u >> v >> c;
		u--; v--;
		auto v1 = make_pair(u, c);
		auto v2 = make_pair(v, c);
		adj[u].push_back(v2);
		adj[v].push_back(v1);
	}
	dfs(0, -1);
	cout << out << endl;
	return 0;
}
