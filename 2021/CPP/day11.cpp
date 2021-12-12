#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int flash(vector<vector<int>> &octos, int x, int y) {
    int cnt = 1;
    for (int i = max(x - 1, 0); i <= min(x + 1, (int) octos.size() - 1); i++) {
        for (int j = max(y - 1, 0); j <= min(y + 1, (int) octos.size() - 1); j++) {
            octos[i][j]++;
            if (octos[i][j] == 10) {
                cnt += flash(octos, i, j);
            }
        }
    }
    return cnt;
}

int updateAndCount(vector<vector<int>> &octos) {
    int cnt = 0;
    for (int i = 0; i < octos.size(); i++) {
        for (int j = 0; j < octos.size(); j++) {
            octos[i][j]++;
            if (octos[i][j] == 10) {
                cnt += flash(octos, i, j);
            }
        }
    }
    for (int i = 0; i < octos.size(); i++) {
        for (int j = 0; j < octos.size(); j++) {
            if (octos[i][j] >= 10) {
                octos[i][j] = 0;
            }
        }
    }
    return cnt;
}

static void solve11_1(ifstream &in) {
    vector<vector<int>> octopuses;
    string s;
    while (in >> s) {
        vector<int> line;
        for (const char &c: s) {
            line.push_back(c - '0');
        }
        octopuses.push_back(line);
    }
    int cnt = 0;
    for (int i = 0; i < 100; i++) {
        cnt += updateAndCount(octopuses);
    }
    cout << cnt << endl;
}

static void solve11_2(ifstream &in) {
    vector<vector<int>> octopuses;
    string s;
    while (in >> s) {
        vector<int> line;
        for (const char &c: s) {
            line.push_back(c - '0');
        }
        octopuses.push_back(line);
    }
    int i = 0;
    bool allFlash = false;
    while (!allFlash) {
        allFlash = true;
        updateAndCount(octopuses);
        for (auto &l: octopuses)
            for (auto &x: l)
                if (x != 0) allFlash = false;
        i++;
    }
    cout << i << endl;
}


int main(int argc, char **argv) {
    ifstream in;
    in.open("../input11.txt");
    solve11_1(in);
    in.close();
    in.open("../input11.txt");
    solve11_2(in);
    in.close();
    return 0;
};