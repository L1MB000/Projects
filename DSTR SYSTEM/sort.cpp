#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <chrono>
#include "sort.h"

using namespace std;

const int MAX_RECORDS = 1500; // Maximum number of records

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
};

InstitutionData data[MAX_RECORDS]; // Array to store data
int numRecords = 0; // Current number of records

// Function to parse a CSV line and create a structure
InstitutionData parseCSVLine(const string& line) {
    InstitutionData record;

    stringstream ss(line);
    string field;

    // Read each field and convert to the appropriate type
    try {
        std::getline(ss, field, ',');
        record.rank = field.empty() ? 0 : std::stoi(field);

        std::getline(ss, record.institution, ',');
        std::getline(ss, record.locationCode, ',');
        std::getline(ss, record.location, ',');

        std::getline(ss, field, ',');
        record.arScore = field.empty() ? 0.0f : std::stof(field);

        std::getline(ss, field, ',');
        record.arRank = field.empty() ? 0 : std::stoi(field);

        std::getline(ss, field, ',');
        record.erScore = field.empty() ? 0.0f : std::stof(field);

        std::getline(ss, field, ',');
        record.erRank = field.empty() ? 0 : std::stoi(field);

        std::getline(ss, field, ',');
        record.fsrScore = field.empty() ? 0.0f : std::stof(field);

        std::getline(ss, field, ',');
        record.fsrRank = field.empty() ? 0 : std::stoi(field);

        std::getline(ss, field, ',');
        record.cpfScore = field.empty() ? 0.0f : std::stof(field);

        std::getline(ss, field, ',');
        record.cpfRank = field.empty() ? 0 : std::stoi(field);

        std::getline(ss, field, ',');
        record.ifrScore = field.empty() ? 0.0f : std::stof(field);

        std::getline(ss, field, ',');
        record.ifrRank = field.empty() ? 0 : std::stoi(field);

        std::getline(ss, field, ',');
        record.isrScore = field.empty() ? 0.0f : std::stof(field);

        std::getline(ss, field, ',');
        record.isrRank = field.empty() ? 0 : std::stoi(field);

        std::getline(ss, field, ',');
        record.irnScore = field.empty() ? 0.0f : std::stof(field);

        std::getline(ss, field, ',');
        record.irnRank = field.empty() ? 0 : std::stoi(field);

        getline(ss, field, ',');
        record.gerScore = field.empty() ? 0.0f : std::stof(field);

        getline(ss, field, ',');
        record.gerRank = field.empty() ? 0 : field.empty() ? 0 : std::stoi(field);

        getline(ss, field, ',');
        record.scoreScaled = field.empty() ? 0.0f : stof(field);
    } catch (const std::invalid_argument& e) {
        cerr << "Error converting field to valid data: " << e.what() << endl;
        // You can choose to handle or skip this record as per your requirement
        
    }

    return record;
}

// Function to read data from CSV file
void readDataFromCSV(const string& filename) {
    ifstream file(filename);
    string line;

    if (!file.is_open()) {
        cout << "Failed to open file: " << filename << endl;
        return;
    }

    // Skip header line
    getline(file, line);

    while (getline(file, line)) {
        if (numRecords == MAX_RECORDS) {
            cout << "Maximum number of records reached. Cannot read more data." << endl;
            return;
        }

        data[numRecords] = parseCSVLine(line);
        numRecords++;
    }

    cout << "Data read successfully from file: " << filename << endl;
    file.close();
}

// Function to print the data
void printData() {
    for (int i = 0; i < numRecords; i++) {
        InstitutionData record = data[i];
        cout << "Rank: " << record.rank << endl;
        cout << "Institution: " << record.institution << endl;
        cout << "Location Code: " << record.locationCode << endl;
        cout << "Location: " << record.location << endl;
        cout << "ArScore: " << record.arScore << endl;
        cout << "ArRank: " << record.arRank << endl;
        cout << "ErScore: " << record.erScore << endl;
        cout << "ErRank: " << record.erRank << endl;
        cout << "FsrScore: " << record.fsrScore << endl;
        cout << "FsrRank: " << record.fsrRank << endl;
        cout << "CpfScore: " << record.cpfScore << endl;
        cout << "CpfRank: " << record.cpfRank << endl;
        cout << "IfrScore: " << record.ifrScore << endl;
        cout << "IfrRank: " << record.ifrRank << endl;
        cout << "IsrScore: " << record.isrScore << endl;
        cout << "IsrRank: " << record.isrRank << endl;
        cout << "IrnScore: " << record.irnScore << endl;
        cout << "IrnRank: " << record.irnRank << endl;
        cout << "GerScore: " << record.gerScore << endl;
        cout << "GerRank: " << record.gerRank << endl;
        cout << "ScoreScaled: " << record.scoreScaled << endl;
        cout << endl;
    }
}

// Function to print the data
void printList() {
    for (int i = 0; i < numRecords; i++) {
        InstitutionData record = data[i];
        cout << record.rank << ". " << record.institution << endl;
    }
}

// Function to swap two InstitutionData structures
void swapData(InstitutionData& a, InstitutionData& b) {
    InstitutionData temp = a;
    a = b;
    b = temp;
}

// Function to partition the data array based on the institution field
int partitionData(InstitutionData data[], int low, int high) {
    string pivot = data[high].institution;
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (data[j].institution <= pivot) {
            i++;
            swapData(data[i], data[j]);
        }
    }

    swapData(data[i + 1], data[high]);

    return i + 1;
}

// Function to perform the QuickSort algorithm
void quickSortData(InstitutionData data[], int low, int high) {
    if (low < high) {
        int pivotIndex = partitionData(data, low, high);

        quickSortData(data, low, pivotIndex - 1);
        quickSortData(data, pivotIndex + 1, high);
    }
}

// Function to sort the data array alphabetically based on the institution field
void sortDataAlphabetically() {
    quickSortData(data, 0, numRecords - 1);
}

// Function to merge two sorted subarrays
void mergeData(InstitutionData data[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    InstitutionData leftArr[n1];
    InstitutionData rightArr[n2];

    for (int i = 0; i < n1; i++) {
        leftArr[i] = data[left + i];
    }

    for (int j = 0; j < n2; j++) {
        rightArr[j] = data[mid + 1 + j];
    }

    int i = 0;
    int j = 0;
    int k = left;

    while (i < n1 && j < n2) {
        if (leftArr[i].institution >= rightArr[j].institution) {
            data[k] = leftArr[i];
            i++;
        } else {
            data[k] = rightArr[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        data[k] = leftArr[i];
        i++;
        k++;
    }

    while (j < n2) {
        data[k] = rightArr[j];
        j++;
        k++;
    }
}

// Function to perform MergeSort on the data array
void mergeSortData(InstitutionData data[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSortData(data, left, mid);
        mergeSortData(data, mid + 1, right);

        mergeData(data, left, mid, right);
    }
}

// Function to sort the data array alphabetically based on the institution field in descending order
void sortDataAlphabeticallyDescending() {
    mergeSortData(data, 0, numRecords - 1);
}


void sortScore() {
    bool swapped;
    for (int i = 0; i < numRecords - 1; i++) {
        swapped = false;
        for (int j = 0; j < numRecords - i - 1; j++) {
            // Compare the scores
            if (data[j].arScore < data[j + 1].arScore ||
                data[j].fsrScore < data[j + 1].fsrScore ||
                data[j].erScore < data[j + 1].erScore) {
                // Swap the records
                InstitutionData temp = data[j];
                data[j] = data[j + 1];
                data[j + 1] = temp;
                swapped = true;
            }
        }
        // If no swap occurred in the inner loop, the array is already sorted
        if (!swapped) {
            break;
        }
    }
}

void quickSort(){
    string filename = "dataUni.csv"; // CSV file name

    readDataFromCSV(filename);
    sortDataAlphabetically();
    printData();
}

void mergeSort(){
    string filename = "dataUni.csv"; // CSV file name

    readDataFromCSV(filename);
    sortDataAlphabeticallyDescending();
    printData();
}

void bubbleSort(){
    string filename = "dataUni.csv"; // CSV file name

    readDataFromCSV(filename);
    sortScore();
    printData();
}

void displayList(){
    string filename = "dataUni.csv"; // CSV file name

    readDataFromCSV(filename);
    printData();
}

void displayName(){
    string filename = "dataUni.csv"; // CSV file name

    readDataFromCSV(filename);
    printList();
}


