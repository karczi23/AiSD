#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;
/**
 * Generates numbers from 0 to len, then shuffles them
 * @param len - length of the list
 * @return
 */
vector<long int> rand_gen(long int len) {
    vector<long int> numbers;

    for (long int i = 0; i < len; i ++) {
        numbers.push_back(i);
    }

    mt19937 seed(chrono::system_clock::now().time_since_epoch().count());
    shuffle(numbers.begin(), numbers.end(), seed);

//    print all numbers of shuffled numbers
//    for (long int num: numbers) {
//        cout << num << " ";
//    }

    return numbers;
}