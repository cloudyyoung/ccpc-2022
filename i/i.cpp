#include <iostream>
#include <unordered_map>
#include <string>
#include <stack>

using namespace std;

int main() {
    while (true) {
        int n;
        string first, second, next;
        unordered_map<string, string> unordered_map;
        stack<string> result;
        cin >> n;

        for (int i = 0; i < n; i++) {
            cin >> first >> second;
            while (1) {
                if (unordered_map.count(second) == 0) break;
                second = unordered_map[second];
            }
            unordered_map[first] = second;
        }

        for (auto& it : unordered_map) {
            next = it.first;
            while (1) {
                if (unordered_map.count(next) == 0) {
                    result.push(it.first + " " + next);
                    break;
                }
                next = unordered_map[next];
            }
        }

        while (!result.empty()) {
            cout << result.top() << endl;
            result.pop();
        }
    }
    return 0;
}