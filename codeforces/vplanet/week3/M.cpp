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

const ll MAXN = 300009;

ll N, W[MAXN], out;
vector< pair<ll, ll> > adj[MAXN];

void dfs(ll node, ll parent){
	ll top1 = 0, top2 = 0;
	for(auto i: adj[node]) if(i.first != parent){
		dfs(i.first, node);
		ll value = W[i.first] - i.second;
		if( value > top2 ){
			top2 = value;
			if( top2 > top1 ){
				swap(top1, top2);
			}
		}
	}
	out = max(out, top1 + top2 + W[node]);
	W[node] += top1;
}

int main () {
	out = 0;
	cin >> N;
	for(ll i = 0; i < N; i++){
		cin >> W[i];
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
