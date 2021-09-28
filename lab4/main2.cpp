
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

void circle(std::string a, std::string b) {
    // if a != b
    if (a.size() != b.size()) {
        std::cout << -1;
        return;
    }
    // double string
    std::string doubleString = a + a;
    std::cout<<"String was doubled\n";
    std::vector<int> pi = prefix(b);
    int index = -1;
    int j = 0;
    for (int i = 0; i < doubleString.size(); i++) {
        while (j > 0 && doubleString[i] != b[j]) {
            std::cout<<"Return to to the index "<<pi[j-1]<<std::endl;
            j = pi[j - 1];
        }
        // if symbols equals
        if (b[j] == doubleString[i]) {
            j++;
            std :: cout << "Symbol '"<<b[j - 1]<<"' was found on substring and text on positions "<<j - 1<<" and "<<i<< " respectively\n";
        }
        // when found substring
        if (j == b.size()) {
            std::cout<<"substring was found on text start with position: "<<i - b.size() + 1<<std::endl;
            index = i - b.size() + 1;
            break;
        }
        std::cout<<"Go to the next symbol of text:"<< doubleString[i+1]<<std::endl;
    }

    std::cout << index;
}


int main() {
    std::string p, t;
    std::cin >> p;
    std::cin >> t;
    circle(p, t);
    return 0;
}
