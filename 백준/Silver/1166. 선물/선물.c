#include <stdio.h>
int main(){
    int n,l,w,h;
    double left = 0, right= 1000000000, mid;
    scanf("%d %d %d %d", &n, &l, &w, &h);
    for(int i = 0; i < 10000; i++){
        mid = (left+right)/2;
        if(((long)(l/mid))*((long)(w/mid))*((long)(h/mid)) < n) right=mid;
		else left=mid;
    }
    printf("%.10lf",left);
}