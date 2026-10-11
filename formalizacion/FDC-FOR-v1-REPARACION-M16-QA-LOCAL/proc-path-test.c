#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
int main(){char b[4096]; ssize_t n=readlink("/proc/self/exe",b,sizeof(b)-1); if(n>=0){b[n]=0;puts(b);}else{printf("errno=%d %s\n",errno,strerror(errno));} return n<0;}
