#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
int main(){char b[4096]; ssize_t n=(sprintf(b,"/proc/%d/exe",getpid()),readlink(b,b,sizeof(b)-1)); if(n>=0){b[n]=0;puts(b);}else{printf("errno=%d %s\n",errno,strerror(errno));} return n<0;}
