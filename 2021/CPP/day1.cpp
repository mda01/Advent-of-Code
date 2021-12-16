#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

static void solve1_1(ifstream &in) {
  vector<int> nums;
  int x;
  while (in >> x)
    nums.push_back(x);
  int cnt = 0;
  for (int i = 1; i < nums.size(); i++) {
    if (nums[i] > nums[i - 1])
      cnt++;
  }
  cout << cnt << endl;
}

static void solve1_2(ifstream &in) {
  vector<int> nums;
  int x;
  while (in >> x)
    nums.push_back(x);
  int cnt = 0;
  for (int i = 3; i < nums.size(); i++) {
    if (nums[i] + nums[i - 1] + nums[i - 2] >
        nums[i - 1] + nums[i - 2] + nums[i - 3])
      cnt++;
  }
  cout << cnt << endl;
}

int main(int argc, char **argv) {
  ifstream in;
  in.open("../input1.txt");
  solve1_1(in);
  in.close();
  in.open("../input1.txt");
  solve1_2(in);
  in.close();
  return 0;
}