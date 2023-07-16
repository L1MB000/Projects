#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <chrono>
#include "binarySearch.h"

using namespace std;

struct Institution {
    string rank;
    string name;
    string locationCode;
    
    Institution(string r, string n, string lc) : rank(r), name(n), locationCode(lc) {}
};

//structure to create binary tree
struct Node {
    Institution data;
    Node* left;
    Node* right;

    Node(Institution institution) : data(institution), left(nullptr), right(nullptr) {}
};

// function to insert data to the binary tree
void insertNode(Node*& root, Institution institution) {
    if (root == nullptr) {
        root = new Node(institution);
    } else if (institution.locationCode < root->data.locationCode) {
        insertNode(root->left, institution);
    } else {
        insertNode(root->right, institution);
    }
}

//function to print institution details
void printInstitutions(Node* node, string locationCode) {
    if (node == nullptr) {
        return;
    }

    if (node->data.locationCode == locationCode) {
        cout << "Rank: " << node->data.rank << "\n";
        cout << "Institution: " << node->data.name << "\n";
        // Print other fields as required
        cout << "----------------------------------\n";
    }

    printInstitutions(node->left, locationCode);
    printInstitutions(node->right, locationCode);
}

void searchByLocationCode(Node* root, string locationCode) {
    if (root == nullptr) {
        return;
    }

    if (locationCode < root->data.locationCode) {
        searchByLocationCode(root->left, locationCode);
    } else if (locationCode > root->data.locationCode) {
        searchByLocationCode(root->right, locationCode);
    } else {
        // Found a match
        cout << "Institutions with location code " << locationCode << ":\n";
        cout << "----------------------------------\n";
        printInstitutions(root, locationCode);
    }
}


// functionto perform binary search of location code
void binarySearch() {
    Node* root = nullptr;
    string line;
    ifstream inputFile("dataUni.csv");

    if (inputFile.is_open()) {
        getline(inputFile, line);  // Skip the header line

        while (getline(inputFile, line)) {
            stringstream ss(line);
            string rank, institution, locationCode;
            // Parse the line and extract required fields
            getline(ss, rank, ',');
            getline(ss, institution, ',');
            getline(ss, locationCode, ',');

            // Create Institution object and insert into BST
            Institution newInstitution(rank, institution, locationCode);
            insertNode(root, newInstitution);
        }

        inputFile.close();
    } else {
        cout << "Unable to open file." << endl;
        return;
    }
    

    // Example: Searching for institutions with location code "LocationCode"
    string locationCode1;
    cout << "Enter location code to search: ";
    getline(std::cin, locationCode1);
    searchByLocationCode(root, locationCode1);
    
}



