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

const ll MAXTREE = 1009;
const ll MAXBIRD = 10009;
const ll MAXCOST = 1000000009;
const ll INF     = 100000000000000009;

ll cost[MAXTREE], birds[MAXTREE];
ll dp[MAXTREE][MAXBIRD];

ll N, W, B, X, out;

int main () {
	cin >> N >> W >> B >> X;
	for(ll i = 0; i < N; i++){
		cin >> birds[i];
	}
	for(ll i = 0; i < N; i++){
		cin >> cost[i];
	}
	for(ll tree = 0; tree < MAXTREE; tree++){
		for(ll bird = 0; bird < MAXBIRD; bird++){
			dp[tree][bird] = -INF;
		}
	}

	out = 0;
	dp[0][0] = W;
	for(ll i = 1; i <= birds[0]; i++){
		if(dp[0][0] - cost[0] * i >= 0){
			dp[0][i] = dp[0][0] - cost[0] * i;
			out = max(out, i);
		}
	}
	for(ll tree = 1; tree < N; tree++){
		for(ll bird = MAXBIRD; bird >=0; bird--){
			if(dp[tree - 1][bird] >= 0){
				dp[tree][bird] = min(dp[tree - 1][bird] + X, W + B * bird);
				for(ll new_birds = 1; new_birds <= birds[tree]; new_birds++){
					if(bird + new_birds < MAXBIRD && dp[tree][bird] - cost[tree] * new_birds >= 0){
						dp[tree][bird + new_birds] = max(dp[tree][bird + new_birds], dp[tree][bird] - cost[tree] * new_birds);
						out = max(out, bird + new_birds);
					}
				}
			}
		}
	}

	cout << out  << endl;

	return 0;
}
