
#include <iostream>
#include <string>
#include <vector>

std::vector<int> prefix(std::string p) {
    std::vector<int> pi(p.size(), 0); // sizes of prefix functions for all substrings

    std::cout << "Start calculating prefix function\n";
    std::cout << "Suffix of '" << p[0] << "' on position '0' equals 0\n";
    for (int i = 1; i < p.size(); i++) {
        int j = pi[i - 1];
        // found equals symbols
        while (j > 0 && p[i] != p[j]) {
            std::cout << "Symbol on position " <<i<< " not equals symbol on position " <<j<<". Looking suffix with length " << pi[j - 1]<<std::endl;
            j = pi[j - 1];
        }

        // if symbols equals add prefix function to i
        if (p[i] == p[j]) {
            std::cout << "Found equals symbols. Suffix of '"<<p[i] << "' on position '"<<i<<"' equals "<<j+1<<std::endl;
            j++;
            pi[i] = j;
        } else {
            std::cout<< "Position of j '0'. That's why pi("<<i<<") = 0, where p["<<i<<"] = "<< p[i]<<std::endl;
            pi[i] = 0;
        }
        std::cout<<std::endl;
    }

    std::cout<<"Prefix functions for substring:\n";
    for(int i = 0; i < pi.size(); i++){
        std::cout<<p[i]<<" ";
    }
    std::cout<<std::endl;

    for(int i = 0; i < pi.size(); i++){
        std::cout<<pi[i]<<" ";
    }
    std::cout<<std::endl;
    return pi;
}

void kmp(std::vector<int> pi, std::string p, std::string t) {
    int j = 0;
    std::vector<size_t> indexes;
    for (int i = 0; i < t.size(); i++) {
        while (j > 0 && p[j] != t[i]) {
            std::cout<<"Return to to the index "<<pi[j-1]<<std::endl;
            j = pi[j - 1];
        }
        // if symbols equals
        if (p[j] == t[i]) {
            j++;
            std :: cout << "Symbol '"<<p[j - 1]<<"' was found on substring and text on positions "<<j - 1<<" and "<<i<< " respectively\n";
        }
        // when found substring
        if (j == p.size()) {
            std::cout<<"substring was found on text start with position: "<<i - p.size() + 1<<std::endl;
            indexes.push_back(i - p.size() + 1);

        }
        std::cout<<"Go to the next symbol of text:"<< t[i+1]<<std::endl;
    }

    // print founded indexes
    if (indexes.empty()) {
        std::cout << -1;
    } else {
        for (int k = 0; k < indexes.size() - 1; k++) {
            std::cout << indexes[k] << ",";
        }
        std::cout << indexes[indexes.size() - 1];
    }
}

int main() {
    std::string p, t;
    std::cin >> p;
    std::cin >> t;
    kmp(prefix(p), p, t);
    return 0;
}


