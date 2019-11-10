#include<stdio.h>

int atoi(char c){
	return c - '0';
}

int calculate(char  a[], int len){
    if (len == 1)
            return atoi(a[0]);
		
	int value;
	
	if (len == 3){
		char opt = a[1];
		switch(opt){
			case '+': 
				value = atoi(a[0]) + atoi(a[2]);
				break;
			case '-': 
				value = atoi(a[0]) - atoi(a[2]);
				break;				
			case 'x': 
				value = atoi(a[0]) * atoi(a[2]);
				break;
			default: 
				value = atoi(a[0]) / atoi(a[2]);
		}
		return value;
	}
	
	if (len <= 0)
			return 0;

    int num_index = 0;
    int opt_index = 1;
    value = atoi(a[num_index * 2]);
    char opt = a[opt_index * 2 - 1];
    opt_index++;
    num_index++;
	
    if(opt == 'x'){
            value *= atoi(a[2 * num_index]);
            a[2 * num_index] = value + '0';
            return calculate(&a[2 * num_index], len - 2);
    }

    if(opt == '/'){
            value /= atoi(a[2 * num_index]);
            a[2 * num_index] = value + '0';
            return calculate(&a[2 * num_index], len - 2);
    }
	
	
    if(opt == '+'){
		char opt = a[opt_index * 2 - 1];
		if(opt == 'x' || opt == '/'){
			value += calculate(&a[2 * num_index], len - 2);
			return value;
		} else {
			value += atoi(a[2 * num_index]);
            a[2 * num_index] = value + '0';
            return calculate(&a[2 * num_index], len - 2);
		}
	}
	
	if(opt == '-'){
		char opt = a[opt_index * 2 - 1];
		if(opt == 'x' || opt == '/'){
			value -= calculate(&a[2 * num_index], len - 2);
			return value;
		} else {
			value -= atoi(a[2 * num_index]);
            a[2 * num_index] = value + '0';
            return calculate(&a[2 * num_index], len - 2);
		}
	}	
	return 0;
}
		
	int main(){
		int num;
		scanf("%d", &num);
		char a[10];
		for(int i = 0; i < num; i++){
			scanf("%s", a);
			int result = calculate(a, 7);
			if(result == 24)
				printf("Yes\n");
			else
				printf("No\n");
		}
		return 0;
	}