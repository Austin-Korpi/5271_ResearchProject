#include<unistd.h>
#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define SCALE 1000
#define STATS_FILE "memory_stats_with_custom_implementation.txt"


void log_memory_stats(const char* stage) {
    FILE* proc_file = fopen("/proc/self/status", "r");
    FILE* stats_file = fopen(STATS_FILE, "a");

    if (!proc_file || !stats_file) {
        perror("Error opening files");
        exit(EXIT_FAILURE);
    }

    fprintf(stats_file, "=== Memory Stats at %s ===\n", stage);
    char line[256];
    while (fgets(line, sizeof(line), proc_file)) {
        if (strstr(line, "VmSize") || strstr(line, "VmRSS") || strstr(line, "VmData")) {
            fprintf(stats_file, "%s", line);
        }
    }
    fprintf(stats_file, "\n");

    fclose(proc_file);
    fclose(stats_file);
}

void main() {

  log_memory_stats("Inital State");  
  // Mass mapping stress test
  void* addr[SCALE];
  for (int i = 0; i < SCALE; i++) {
    addr[i] = mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANON, -1, 0);
  }

  log_memory_stats("After Mass Mapping");
  
  // Mass unmapping stress test
  for (int i = 0; i < SCALE; i++) {
    munmap(addr[i], sizeof(int)); 
  }

  log_memory_stats("After Mass Unmapping");
  
  // Mass combined stress test
  for (int i = 0; i < SCALE; i++) {
    addr[i] = mmap(NULL, sizeof(int), PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANON, -1, 0);
    munmap(addr[i], sizeof(int));
  }

  log_memory_stats("After Combined Test");

  printf("Done\n");
}