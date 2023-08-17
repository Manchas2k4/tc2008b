#include <iostream>
#include <iomanip>
#include <random>
#include <ctime>
#include <utility>
#include <algorithm>
#include <vector>

using namespace std;

//mt19937 generator(clock());

const int    MIN_SIZE = 25;
const int    MAX_SIZE = 50;
const double PCT_TRASH = 0.35;
const int    MIN_TRASH = 2;
const int    MAX_TRASH = 8;
const double PCT_OBSTACLES = 0.10;
const int    MIN_SIZE_OBS = 1;
const int    MAX_SIZE_OBS = 3;
typedef pair<int, int> Coord;

mt19937 generator(clock());
uniform_int_distribution<int> space(MIN_SIZE, MAX_SIZE);
uniform_int_distribution<int> trash(MIN_TRASH, MAX_TRASH);
uniform_int_distribution<int> obstable(MIN_SIZE_OBS, MAX_SIZE_OBS);
vector<Coord> positions;
vector<vector<char> > matrix;

int main(int argc, char* argv[]) {
    int width, height, k, total;
    int trash_amount, obstable_amount;
    Coord start, paper_bin, pos;

    width = space(generator);
    height = space(generator);

    total = width * height;

    matrix.resize(height);
    for (int i = 0; i < matrix.size(); i++) {
        matrix[i].resize(width, '0');
    }
    positions.resize(total);

    k = 0;
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            positions[k++] = Coord(i, j);
        }
    }

    for (int i = 0; i < 3; i++) {
        shuffle (positions.begin(), positions.end(), generator);
    }

    start = positions[0];
    matrix[start.first][start.second] = 'S';

    paper_bin = positions[positions.size() - 1];
    matrix[paper_bin.first][paper_bin.second] = 'P';

    k = 1;
    trash_amount = (int) (total * PCT_TRASH);
    for (int i = 0; i < trash_amount; i++) {
        pos = positions[k++];
        matrix[pos.first][pos.second] = (char) ('0' + trash(generator));
    }

    obstable_amount = (int) (total * PCT_OBSTACLES);
    for (int i = 0; i < obstable_amount; i++) {
        pos = positions[k++];
        matrix[pos.first][pos.second] = 'X';
    }

    cout << height << " " << width << "\n";
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}