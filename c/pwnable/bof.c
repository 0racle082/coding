#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void func(int key){
	char overflowme[32];
	printf("overflow me:");
	gets(overflowme);
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}
