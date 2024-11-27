/*
Compile:
    Command: gcc simple_POC.c

Vulnerable:
    Command: ./a.out
    Output:  secret

Not vulnerable:
    Command: LD_PRELOAD=./libffmallocnpmt.so ./a.out
    Output:  Segmentation fault

*/

#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char *greeting;

void create_custom_greeting(char * msg) {
    // greeting = malloc(strlen(msg));
    greeting = mmap(NULL, strlen(msg), PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANON, -1, 0);
    strcpy(greeting, msg);
}

void print_custom_greeting() {
    printf("%s\n", greeting);
}

void remove_custom_greeting() {
    // free(greeting);
    munmap(greeting, strlen(greeting));
}

char *secret_message;

void set_secret_message(char * msg) {
    // secret_message = malloc(strlen(msg));
    secret_message = mmap(NULL, strlen(msg), PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANON, -1, 0);
    strcpy(secret_message, msg);
}

int main() {
    // Create public variable
    create_custom_greeting("Hello!");

    // Destroy public variable
    remove_custom_greeting();

    // Make secret variable
    set_secret_message("secret");
    
    // Print public variable
    print_custom_greeting();
}
