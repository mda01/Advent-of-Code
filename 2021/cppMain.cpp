#include "day1_1.cpp"
#include <iostream>
#include <fstream>

using namespace std;


int main() {
    ifstream in;
    in.open("2021/input1.txt");
    solve1_1(in);
    in.close();
    in.open("2021/input1.txt");
    solve1_2(in);
    in.close();
    return 0;
};