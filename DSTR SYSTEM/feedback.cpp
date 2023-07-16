#include <iostream>
#include <string>
#include <ctime>
#include "feedback.h"

struct Feedback {
    std::string username;
    std::string institution;
    std::string feedback;
    std::string feedbackDate;
    std::string reply;
};

struct Node {
    Feedback feedback;
    Node* next;
};

// Function to get current date and time as a string
std::string getCurrentDateTime() {
    time_t now = time(0);
    char* dt = ctime(&now);
    return dt;
}

Node* head = nullptr; // Global head pointer for the linked list

// Function to send feedback
void sendFeedback() {
    Feedback newFeedback;
    std::cout << "Enter your username: ";
    std::getline(std::cin >> std::ws, newFeedback.username);
    std::cout << "Enter your institution: ";
    std::getline(std::cin >> std::ws, newFeedback.institution);
    std::cout << "Enter your feedback: ";
    std::getline(std::cin >> std::ws, newFeedback.feedback);
    std::cout << " ";
    newFeedback.feedbackDate = getCurrentDateTime();

    // Validate input
    if (newFeedback.username.empty() || newFeedback.institution.empty() ||
        newFeedback.feedback.empty() || newFeedback.feedbackDate.empty()) {
        std::cout << "Feedback fields cannot be empty. Please try again." << std::endl;
        return;
    }

    Node* newNode = new Node;
    newNode->feedback = newFeedback;
    newNode->next = nullptr;

    // If the list is empty, make the new node the head
    if (head == nullptr) {
        head = newNode;
    } else {
        // Find the last node in the list
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }

        // Add the new node at the end
        current->next = newNode;
    }

    std::cout << "Feedback sent successfully!" << std::endl;
}

// Function to display all feedbacks
void displayAllFeedbacks() {
    if (head == nullptr) {
        std::cout << "No feedback available." << std::endl;
        return;
    }

    Node* current = head;
    int count = 0;

    std::cout << "All feedbacks:" << std::endl;
    while (current != nullptr) {
        std::cout << "Feedback #" << count << ":" << std::endl;
        std::cout << "Username: " << current->feedback.username << std::endl;
        std::cout << "Institution: " << current->feedback.institution << std::endl;
        std::cout << "Feedback: " << current->feedback.feedback << std::endl;
        std::cout << "Feedback Date: " << current->feedback.feedbackDate << std::endl;
        std::cout << "Reply: " << current->feedback.reply << std::endl;
        std::cout << "---------------------------------" << std::endl;

        current = current->next;
        count++;
    }
}

// Function to reply to feedback by index
void replyToFeedbackByIndex(int index) {
    if (head == nullptr) {
        std::cout << "No feedback available." << std::endl;
        return;
    }

    Node* current = head;
    int count = 0;

    // Find the feedback node at the specified index
    while (current != nullptr && count < index) {
        current = current->next;
        count++;
    }

    if (current == nullptr) {
        std::cout << "Invalid feedback index." << std::endl;
        return;
    }

    std::cout << "Enter your reply: ";
    std::getline(std::cin >> std::ws, current->feedback.reply);
    std::cout << "Reply sent successfully!" << std::endl;
}

void reply(){
    std::cout << "Enter the index of the feedback you want to reply to: ";
    int index;
    std::cin >> index;
    replyToFeedbackByIndex(index);
}