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

ll N, M, W[MAXN];

int main () {
	cin >> N;
	ll s = 0;
	for(ll i = 0; i < N; i++){
		cin >> W[i];
		s += W[i];
	}
	vector<ll> p (W, W + N);
	sort(p.begin(), p.end());

	cin >> M;
	for(ll i = 0; i < M; i++){
		ll t;
		cin >> t;
		cout << s - p[N - t] << "\n";
	}
	return 0;
}
