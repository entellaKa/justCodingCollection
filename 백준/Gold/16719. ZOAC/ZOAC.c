#include <stdio.h>
#include <string.h>

int main(){
    char s[101];
    int t[101] = {0,};
    scanf("%s", &s);
    
    int l = strlen(s);
    int t_l = l;
    for (int i = 0; i < l; i++){
        int n = 0;
        int j;
        for (j = t_l-1; t[j] == 0 && j > -1; j--);
        j++;
        
        int c = j;
        for (int k = j; k < t_l; k++)
            if (s[k] < s[c])
                c = k;
        
        t[c] = 1;
        
        for (int i = 0; i < l; i++)
            if (t[i] == 1) printf("%c", s[i]);
        printf("\n");
        
        while(t[t_l-1] == 1) 
            t_l--;
    }
	return 0;
}