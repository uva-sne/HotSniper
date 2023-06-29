#include "sim_api.h"
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    printf("Start main function\n");
    SimRoiStart();

    // SimUser(0x124) returns the current simulation time in femto s (10E-16)
    long int current_time = SimUser(0x124, 1); // timer registed as 0x124
    printf("main() started at: %ld ns\n", current_time / 1000000);

    for (int i = 0; i < 50; i++) {
        int sum = 0;
        // Do some dummy work
        for (int j = 0; j < 2000; j++) {
            sum += j;
        }

        current_time = SimUser(0x124, 1);
        printf("Current time is: %ld ns\n", current_time / 1000000);
    }

    printf("End main function\n");

    current_time = SimUser(0x124, 1);
    printf("main() finishing at: %ld ns\n", current_time / 1000000);

    SimRoiEnd();
    return 0;
}
