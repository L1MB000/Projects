#include <iostream>
#include <string>
#include <vector>
#include "signLog.h"

struct User {
    std::string username;
    std::string password;
};

std::vector<User> users; // Vector to store user credentials

void defaultUser(){
    // Add default admin and user accounts
    users.push_back({"admin", "admin123"});
    users.push_back({"user", "user123"});
    users.push_back({"user1", "user321"});
}


// Function to check if a username already exists
bool isUsernameExists(const std::string& username) {
    for (const auto& user : users) {
        if (user.username == username) {
            return true;
        }
    }
    return false;
}



bool passcheck(const std::string& password) {
    bool chkdigit = false;
    bool chkalpha = false;

    for (char c : password) {
        if (std::isdigit(c)) {
            chkdigit = true;
        } else if (std::isalpha(c)) {
            chkalpha = true;
        }

        if (chkdigit && chkalpha) {
            return true;
        }
    }

    return false;
}

// Function to sign up a new user
void signUp() {
    User newUser;

    bool isValidUser = false;

    while (!isValidUser) {
    std::cout << "=================" << std::endl;
    std::cout << "Enter a username: ";
    std::cin >> newUser.username;
    if (newUser.username.length() >= 8) {
        if (isUsernameExists(newUser.username)) {
        std::cout << "Username already exists. Please choose a different username." << std::endl;
        }
        else {break;
        }
    } else {
        std::cout << "Input is invalid. It should have a minimum length of 8 characters." << std::endl;
    }
    

    }
    

    bool isValidPassword = false;

    while (!isValidPassword) {
        std::cout << "Enter a password: ";
        std::cin >> newUser.password;
        if (newUser.password.length() >= 8) {
            if (passcheck(newUser.password)) {
                users.push_back(newUser);
                std::cout << "Sign up successful!" << std::endl;
                std::cout << "===================" << std::endl;
                break;
            } else {
                std::cout << "Invalid password. It should contain at least one digit and one alphabet." << std::endl;
            }
        } else{
        
            std::cout << "Input is invalid. It should have a minimum length of 8 characters." << std::endl;
            }

    }
}

// Function to login an existing user
bool logIn() {
    std::string username, password;
    std::cout << "Enter your username: ";
    std::cin >> username;
    std::cout << "Enter your password: ";
    std::cin >> password;

    for (const auto& user : users) {
        if (user.username == username && user.password == password) {
            std::cout << "Login successful!" << std::endl;
            return true;
        }
    }
    std::cout << "Invalid username or password. Please try again." << std::endl;
    return false;
}

// Function to modify user information
void modifyUser() {
    std::string username, newPassword;
    std::cout << "Enter your username: ";
    std::cin >> username;

    // Check if the username exists
    if (!isUsernameExists(username)) {
        std::cout << "Username does not exist." << std::endl;
        return;
    }

    std::cout << "Enter your new password: ";
    std::cin >> newPassword;

    // Update the password for the specified user
    for (auto& user : users) {
        if (user.username == username) {
            user.password = newPassword;
            break;
        }
    }

    std::cout << "Password updated successfully!" << std::endl;
}

// Function to delete user account
void deleteUser() {
    std::string username;
    std::cout << "Enter your username: ";
    std::cin >> username;

    // Check if the username exists
    if (!isUsernameExists(username)) {
        std::cout << "Username does not exist." << std::endl;
        return;
    }

    // Remove the user from the vector
    for (auto it = users.begin(); it != users.end(); ++it) {
        if (it->username == username) {
            users.erase(it);
            break;
        }
    }

    std::cout << "Account deleted successfully!" << std::endl;
}

// Function to display all users
void displayUsers() {
    std::cout << "All Users:" << std::endl;
    for (const auto& user : users) {
        std::cout << "Username: " << user.username << std::endl;
        std::cout << "Password: " << user.password << std::endl;
        std::cout << "------------------------" << std::endl;
    }
}