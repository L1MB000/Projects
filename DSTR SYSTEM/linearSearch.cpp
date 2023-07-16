#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <chrono>
#include "linearSearch.h"

struct InstitutionData {
    int rank;
    std::string institution;
    std::string locationCode;
    std::string location;
    float arScore;
    int arRank;
    float erScore;
    int erRank;
    float fsrScore;
    int fsrRank;
    float cpfScore;
    int cpfRank;
    float ifrScore;
    int ifrRank;
    float isrScore;
    int isrRank;
    float irnScore;
    int irnRank;
    float gerScore;
    int gerRank;
    float scoreScaled;
    
    InstitutionData* next;
    InstitutionData* prev;
};

// Function to validate if a string is empty or not
bool isEmpty(const std::string& str) {
    return str.empty() || str.find_first_not_of(' ') == std::string::npos;
}

// Function to validate if a string can be converted to a float
bool isFloat(const std::string& str) {
    std::istringstream iss(str);
    float f;
    iss >> std::noskipws >> f;
    return iss.eof() && !iss.fail();
}

// Function to validate if a string can be converted to an integer
bool isInteger(const std::string& str) {
    std::istringstream iss(str);
    int i;
    iss >> std::noskipws >> i;
    return iss.eof() && !iss.fail();
}

// Function to load institution data from a CSV file into a doubly circular linked list
InstitutionData* loadInstitutionData(const std::string& filename) {
    InstitutionData* head = nullptr;
    InstitutionData* tail = nullptr;

    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cout << "Failed to open file: " << filename << std::endl;
        return nullptr;
    }

    std::string line;
    std::getline(file, line); // Skip header line

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::string data;

        InstitutionData* institution = new InstitutionData();

        // Rank
        if (std::getline(iss, data, ',') && isInteger(data)) {
            institution->rank = std::stoi(data);
        } else {
            institution->rank = 0; // Insert null for empty field or error
        }

        // Institution
        if (std::getline(iss, data, ',')) {
            institution->institution = data;
        } else {
            institution->institution = ""; // Insert null for empty field or error
        }

        // Location Code
        if (std::getline(iss, data, ',')) {
            institution->locationCode = data;
        } else {
            institution->locationCode = ""; // Insert null for empty field or error
        }

        // Location
        if (std::getline(iss, data, ',')) {
            institution->location = data;
        } else {
            institution->location = ""; // Insert null for empty field or error
        }

        // AR Score
        if (std::getline(iss, data, ',') && isFloat(data)) {
            institution->arScore = std::stof(data);
        } else {
            institution->arScore = 0.0f; // Insert null for empty field or error
        }

        // AR Rank
        if (std::getline(iss, data, ',') && isInteger(data)) {
            institution->arRank = std::stoi(data);
        } else {
            institution->arRank = 0; // Insert null for empty field or error
        }

        // ER Score
        if (std::getline(iss, data, ',') && isFloat(data)) {
            institution->erScore = std::stof(data);
        } else {
            institution->erScore = 0.0f; // Insert null for empty field or error
        }

        // ER Rank
        if (std::getline(iss, data, ',') && isInteger(data)) {
            institution->erRank = std::stoi(data);
        } else {
            institution->erRank = 0; // Insert null for empty field or error
        }
        
        // Fsr Score
        if (std::getline(iss, data, ',') && isFloat(data)) {
            institution->fsrScore = std::stof(data);
        } else {
            institution->fsrScore = 0.0f; // Insert null for empty field or error
        }

        // FSR Rank
        if (std::getline(iss, data, ',') && isInteger(data)) {
            institution->fsrRank = std::stoi(data);
        } else {
            institution->fsrRank = 0; // Insert null for empty field or error
        }

        // CPF Score
        if (std::getline(iss, data, ',') && isFloat(data)) {
            institution->cpfScore = std::stof(data);
        } else {
            institution->cpfScore = 0.0f; // Insert null for empty field or error
        }

        // CPF Rank
        if (std::getline(iss, data, ',') && isInteger(data)) {
            institution->cpfRank = std::stoi(data);
        } else {
            institution->cpfRank = 0; // Insert null for empty field or error
        }

        // IFR Score
        if (std::getline(iss, data, ',') && isFloat(data)) {
            institution->ifrScore = std::stof(data);
        } else {
            institution->ifrScore = 0.0f; // Insert null for empty field or error
        }

        // IFR Rank
        if (std::getline(iss, data, ',') && isInteger(data)) {
            institution->ifrRank = std::stoi(data);
        } else {
            institution->ifrRank = 0; // Insert null for empty field or error
        }

        // ISR Score
        if (std::getline(iss, data, ',') && isFloat(data)) {
            institution->isrScore = std::stof(data);
        } else {
            institution->isrScore = 0.0f; // Insert null for empty field or error
        }

        // ISR Rank
        if (std::getline(iss, data, ',') && isInteger(data)) {
            institution->isrRank = std::stoi(data);
        } else {
            institution->isrRank = 0; // Insert null for empty field or error
        }

        // IRN Score
        if (std::getline(iss, data, ',') && isFloat(data)) {
            institution->irnScore = std::stof(data);
        } else {
            institution->irnScore = 0.0f; // Insert null for empty field or error
        }

        // IRN Rank
        if (std::getline(iss, data, ',') && isInteger(data)) {
            institution->irnRank = std::stoi(data);
        } else {
            institution->irnRank = 0; // Insert null for empty field or error
        }

        // GER Score
        if (std::getline(iss, data, ',') && isFloat(data)) {
            institution->gerScore = std::stof(data);
        } else {
            institution->gerScore = 0.0f; // Insert null for empty field or error
        }

        // GER Rank
        if (std::getline(iss, data, ',') && isInteger(data)) {
            institution->gerRank = std::stoi(data);
        } else {
            institution->gerRank = 0; // Insert null for empty field or error
        }
        // Score Scaled
        if (std::getline(iss, data, ',') && isFloat(data)) {
            institution->scoreScaled = std::stof(data);
        } else {
            institution->scoreScaled = 0.0f; // Insert null for empty field or error
        }

        // Set next and prev pointers for doubly circular linked list
        if (head == nullptr) {
            head = institution;
            tail = institution;
        } else {
            tail->next = institution;
            institution->prev = tail;
            tail = institution;
        }
    }

    file.close();

    // Make the linked list circular
    if (head != nullptr) {
        tail->next = head;
        head->prev = tail;
    }

    return head;
}

// Function to perform linear search on the doubly circular linked list based on institution name
InstitutionData* linearSearch(InstitutionData* head, const std::string& institutionName) {
    if (head == nullptr) {
        return nullptr;
    }

    InstitutionData* current = head;

    do {
        if (current->institution == institutionName) {
            return current;
        }
        current = current->next;
    } while (current != head);

    return nullptr;
}

void linearUniSearch() {
    std::string filename = "dataUni.csv";
    InstitutionData* head = loadInstitutionData(filename);

    std::string institutionName;
    std::cout << "Enter institution name to search: \n";
    std::getline(std::cin, institutionName);

    InstitutionData* result = linearSearch(head, institutionName);

    if (result != nullptr) {
        std::cout << "Rank: " << result->rank << std::endl;
        std::cout << "Institution: " << result->institution << std::endl;
        std::cout << "Location Code: " << result->locationCode << std::endl;
        std::cout << "Location: " << result->location << std::endl;
        std::cout << "ArScore: " << result->arScore << std::endl;
        std::cout << "ArRank: " << result->arRank << std::endl;
        std::cout << "ErScore: " << result->erScore << std::endl;
        std::cout << "ErRank: " << result->erRank << std::endl;
        std::cout << "FsrScore: " << result->fsrScore << std::endl;
        std::cout << "FsrRank: " << result->fsrRank << std::endl;
        std::cout << "CpfScore: " << result->cpfScore << std::endl;
        std::cout << "CpfRank: " << result->cpfRank << std::endl;
        std::cout << "IfrScore: " << result->ifrScore << std::endl;
        std::cout << "IfrRank: " << result->ifrRank << std::endl;
        std::cout << "IsrScore: " << result->isrScore << std::endl;
        std::cout << "IsrRank: " << result->isrRank << std::endl;
        std::cout << "IrnScore: " << result->irnScore << std::endl;
        std::cout << "IrnRank: " << result->irnRank << std::endl;
        std::cout << "GerScore: " << result->gerScore << std::endl;
        std::cout << "GerRank: " << result->gerRank << std::endl;
        std::cout << "ScoreScales: " << result->scoreScaled << std::endl;
        std::cout << std::endl;
    } else {
        std::cout << "Institution not found" << std::endl;
    }

    // Clean up memory
    if (head != nullptr) {
        InstitutionData* current = head;
        do {
            InstitutionData* temp = current;
            current = current->next;
            delete temp;
        } while (current != head);
    }
}

// Function to print all institution data in the doubly circular linked list
void printInstitutionData(InstitutionData* head) {
    if (head == nullptr) {
        std::cout << "No data available." << std::endl;
        return;
    }

    InstitutionData* current = head;

    do {
        std::cout << "Rank: " << current->rank << std::endl;
        std::cout << "Institution: " << current->institution << std::endl;
        std::cout << "Location Code: " << current->locationCode << std::endl;
        std::cout << "Location: " << current->location << std::endl;
        std::cout << "AR Score: " << current->arScore << std::endl;
        std::cout << "AR Rank: " << current->arRank << std::endl;
        // Print the remaining fields...

        std::cout << std::endl;

        current = current->next;
    } while (current != head);
}
