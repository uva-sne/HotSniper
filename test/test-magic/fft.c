#include "sim_api.h"
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    printf("Start main function\n");

    SimRoiStart();

    SimNamedMarker(4, "begin");

    if (SimUser(0x123, 1) == 0) {
        printf("SimUser 1 return value was 0\n");
    }

    long int result_value = SimUser(0x124, 1);
    printf("SimUser2 return value %ld\n", result_value);

    for (int i = 0; i < 100; i++) {
        int sum = 0;
        for (int j = 0; j < 1000; j++) {
            sum += j; // dummy work
        }
        result_value = SimUser(0x124, 1);
        printf("SimUser2 return value %ld\n", result_value);
        printf("sum: %d\n", sum);
    }
    SimNamedMarker(5, "end");


    printf("End main function\n");

    result_value = SimUser(0x124, 1);
    printf("End time: %ld\n", result_value / 1000000);
    SimRoiEnd();
    return 0;
}
