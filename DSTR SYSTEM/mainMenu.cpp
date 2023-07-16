// Group 5 - DSTR
// Ericko Bayu Listyo Suherman TP062715
// Neysa Nataniella Uganda TP062285
// Tiffany Gracia Damanik TP064328
// Kenta Itakura Tp061160

/* READ ME TO RUN CODE
RUN THESE IN THE TERMINAL TO RUN THE CODE
g++ -c signLog.cpp -o signLog.o
g++ -c sort.cpp -o sort.o
g++ -c linearSearch.cpp -o linearSearch.o
g++ -c binarySearch.cpp -o binarySearch.o
g++ -c feedback.cpp -o feedback.o
g++ -c favorite.cpp -o favorite.o
g++ -c mainMenu.cpp -o mainMenu.o

g++ signLog.o sort.o mainMenu.o linearSearch.o binarySearch.o feedback.o favorite.o -o program

./program
*/


#include <iostream>
#include <string>
#include "signLog.h"
#include "sort.h"
#include "linearSearch.h"
#include "binarySearch.h"
#include "feedback.h"
#include "favorite.h"

using namespace std;

class user {
    public:
    void normalUser(){
    int choice;

    do {
        cout << "----------------------------------\n";
        cout << "WELCOME TO UNIVERSITY RANKING LIST\n";
        cout << "(Normal User)\n";
        cout << "----------------------------------\n";
        cout << "1. Sign Up\n";
        cout << "2. Display Universities\n";
        cout << "3. Quicksort Ascending Alphabetically\n";
        cout << "4. Mergesort Descending Alphabetically\n";
        cout << "5. Linear Search\n";
        cout << "6. Binary Search\n";
        cout << "7. University Name List\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                signUp();
                break;
            case 2:
                displayList();
                break;
            case 3:
                quickSort();
                break;
            case 4:
                mergeSort();
                break;
            case 5:
                cin.ignore();
                linearUniSearch();
                break;
            case 6:
                cin.ignore();
                binarySearch();
                break;
            case 7:
                displayName();
                break;    
            case 8:
                cout << "Goodbye!" << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
                break;
        }

        cout << endl;
    } while (choice != 8);
}

    void registeredUser(){
        int choice;
        sampleData();
        
        do {
            cout << "----------------------------------\n";
            cout << "WELCOME TO UNIVERSITY RANKING LIST\n";
            cout << "(Registered User)\n";
            cout << "----------------------------------\n";
            cout << "1. Display Universities\n";
            cout << "2. Bubblesort ArScore, FsrScore, ErScore\n";
            cout << "3. Linear Location Search\n";
            cout << "4. Save University\n";
            cout << "5. View Saved University\n";
            cout << "6. Send Feedbacks\n";
            cout << "7. Read Feedbacks\n";
            cout << "8. Log Out\n";
            cout << "Enter your choice: ";
            cin >> choice;

            switch (choice) {
                case 1:
                    displayList();
                    break;
                case 2:
                    bubbleSort();
                    break;
                case 3:
                    cin.ignore();
                    linearUniSearch();
                    break;
                case 4:
                    saveFavorite();
                    break;
                case 5:
                    printFavoritesByUsername();
                    break;
                case 6:
                    sendFeedback();
                    break;
                case 7:
                    displayAllFeedbacks();
                    break;
                case 8:
                    cout << "Goodbye!" << endl;
                    break;    
                default:
                    cout << "Invalid choice. Please try again." << endl;
                    break;
            }

            cout << endl;
        } while (choice != 8);

    }

    void adminUser(){
        int choice;
        sampleData();

        do {
            cout << "----------------------------------\n";
            cout << "THIS IS ADMIN MENU\n";
            cout << "----------------------------------\n";
            cout << "1. Display Users\n";
            cout << "2. Modify Users\n";
            cout << "3. Delete Users\n";
            cout << "4. View Feedbacks\n";
            cout << "5. Reply Feedbacks\n";
            cout << "6. Summarize\n";
            cout << "7. Log Out\n";
            cout << "Enter your choice: ";
            cin >> choice;

            switch (choice) {
                case 1:
                    displayUsers();
                    break;
                case 2:
                    modifyUser();
                    break;
                case 3:            
                    deleteUser();
                    break;
                case 4:
                    displayAllFeedbacks();
                    break;
                case 5:
                    reply();
                    break;
                case 6:
                    countOccurrences();
                    break;
                case 7:
                    cout << "Good Bye!\n" << endl;
                    break;
                default:
                    cout << "Invalid choice. Please try again.\n";
                    break;
            }

            std::cout << std::endl;
        } while (choice != 7);
    }
};



int main() {
    int choice;
    user Menu;
    defaultUser();

    do {
        cout << "----------------------------------\n";
        cout << "WELCOME!\n";
        cout << "----------------------------------\n";
        cout << "1. Guest User\n";
        cout << "2. Member Login\n";
        cout << "3. Admin\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Going to Guest Menu~\n";
                Menu.normalUser();
                break;
            case 2:
                if (logIn() == true){
                    cout << "Going to login Menu!\n";
                    Menu.registeredUser();
                } else{
                    cout << "Try again\n";
                }
                break;
            case 3:
                cout << "Going to Admin Menu!\n";
                Menu.adminUser();
                break;
            case 4:
                cout << "Goodbye!" << endl;
                break; 
            default:
                cout << "Invalid choice. Please try again.\n";
                break;
        }

        cout << endl;
    } while (choice != 4);

    return 0;
}