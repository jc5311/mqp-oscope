#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define MAX_DATA_POINTS 1024
#define PI 3.14159265

//global vars
double sample_data[MAX_DATA_POINTS][MAX_DATA_POINTS];



void main(int argc, char* argv[]){
	//generate some sample data using sign
	for (int i = 0; i < MAX_DATA_POINTS; i++){
		for (int j = 0; j < MAX_DATA_POINTS; j++){
			//use sinusoid
			double rads = ((2 * PI) / MAX_DATA_POINTS) * i;
			//store it in two dimensional array
			sample_data[i][j] = sin(rads);
			printf("sample_data[%d][%d] = %f\n", i, j, sample_data[i][j]);
		}
		
	}
	//pass it to std out
	

	return;
}