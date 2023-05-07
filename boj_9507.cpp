#include <iostream>
#include <vector>

using namespace std;

int main()
{
  long long dp[70];
  dp[0] = 1;
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;
  for (int i = 4; i < 70; i++)
  {
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4];
  }
  int t;
  cin>>t;
  for(int i = 0; i < t; i++)
  {
    int tmp;
    cin>>tmp;
    cout<<dp[tmp] <<"\n";
  }
  return 0;
}
