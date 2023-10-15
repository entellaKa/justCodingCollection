#include <stdio.h>
int main(){
    int N, K, answer = 0;
    scanf("%d %d",&N, &K);
    int result;
    for (result = 0; ; result++, N++){
        int cnt = 0;
        int t = N;
        while(t > 0){
            if (t%2==1){
                cnt++;
            }
            t/=2;
        }
        if (K>=cnt)
            break;
    }
    printf("%d", result);

	return 0;
}
