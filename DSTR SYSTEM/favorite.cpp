#include <iostream>
#include <string>
#include <queue>
#include <map>
#include "favorite.h"

struct Favorite {
    std::string username;
    std::string institution;
};

std::queue<Favorite> favorites; // Queue to store favorites

// Function to save a favorite university
void saveFavorite() {
    Favorite newFavorite;
    std::cout << "Enter your username: ";
    std::getline(std::cin >> std::ws, newFavorite.username);

    std::cout << "Enter favorite institution: ";
    std::getline(std::cin >> std::ws, newFavorite.institution);

    favorites.push(newFavorite);

    std::cout << "Favorite saved!" << std::endl;
}

// Function to count occurrences and print top 10 favorites
void countOccurrences() {
    std::map<std::string, int> occurrenceMap;

    // Count occurrences of each favorite institution
    std::queue<Favorite> tempFavorites = favorites;
    while (!tempFavorites.empty()) {
        occurrenceMap[tempFavorites.front().institution]++;
        tempFavorites.pop();
    }

    // Sort the occurrences in descending order
    std::multimap<int, std::string, std::greater<int>> sortedOccurrences;
    for (const auto& entry : occurrenceMap) {
        sortedOccurrences.insert(std::make_pair(entry.second, entry.first));
    }

    // Print the top 10 favorites with the most occurrences
    int count = 0;
    std::cout << "Favorites University:" << std::endl;
    for (const auto& entry : sortedOccurrences) {
        if (count >= 10) {
            break;
        }
        std::cout << entry.second << ": " << entry.first << " occurrences" << std::endl;
        count++;
    }
}

// Function to print all favorites for a given username
void printFavoritesByUsername() {
    std::string username;
    std::cout << "Enter the username: ";
    std::getline(std::cin >> std::ws, username);

    std::cout << "Favorites for user " << username << ":" << std::endl;
    std::queue<Favorite> tempFavorites = favorites;
    while (!tempFavorites.empty()) {
        if (tempFavorites.front().username == username) {
            std::cout << tempFavorites.front().institution << std::endl;
        }
        tempFavorites.pop();
    }
}

void sampleData() {
    // Sample data for testing
    // favorites.push({"user", "Yale University"});
    // favorites.push({"user", "Tsinghua University"});
    // favorites.push({"user1", "Harvard University"});
    // favorites.push({"user1", "Tsinghua University"});
}
