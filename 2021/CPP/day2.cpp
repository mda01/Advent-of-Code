#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

static void solve2_1(ifstream &in) {
    string dir;
    int val;
    int x = 0, y = 0;
    while (in >> dir >> val) {
        if (dir == "down")
            y += val;
        else if (dir == "up")
            y -= val;
        else if (dir == "forward")
            x += val;
    }
    cout << x * y << endl;
}

static void solve2_2(ifstream &in) {
    vector<int> nums;
    string dir;
    int val, aim = 0, depth = 0, pos = 0;
    while (in >> dir >> val) {
        if (dir == "down")
            aim += val;
        else if (dir == "up")
            aim -= val;
        else if (dir == "forward") {
            pos += val;
            depth += aim * val;
        }
    }
    cout << depth * pos << endl;
}


int main(int argc, char **argv) {
    ifstream in;
    in.open("../input2.txt");
    solve2_1(in);
    in.close();
    in.open("../input2.txt");
    solve2_2(in);
    in.close();
    return 0;
};