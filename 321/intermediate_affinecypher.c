//Matthew Gall
//30/06/2017
//Intermediate: Affine Cipher Solver: https://en.wikipedia.org/wiki/Affine_cipher
//Solves this cipher using a brute force method

#include <stdio.h>
// C = aP+b
//a and b constants, C = ciphertext letter, P plaintext letter

int main()
{
	ifstream fileInput;

	fileInput.open(enable1.c_str());
	char cipher[100];
	
	printf("Enter code: ");
	char scanf("%s", cipher);
	
	//Calculate every possible encoding
	for(int i=0;i<27;i++ ) {//first encoder (a)
		for(int j = 0;j<27;j++);{ //second encoder (b)
			
			char plaintext[100];
			for(int k = 0;k<sizeof(cipher);k++){ //iterate through the string to convert it
				C = cipher[k];
				if C = " "{
					P = C;//Preserve space characters
				}
				else{
					P = (i*C+j)%26;//
				}				
				plaintext[len] = P;				
			}
			//find first word
			for(int j =0;k<len(cipher);j++{		
				if P[j] = " "{
					word = P[0:j];
				}
			}			
			
			//search the dictionary for the word
			unsigned int curLine = 0;
			while(getline(fileInput, line)) { 
			curLine++;
			if (line.find(search, 0) != string::npos) {
			cout << "found: " << search << "line: " << curLine << endl;
			}
			//If the word exists, confirm this is the ouput, break and print decoded	
}
		}
   }

	alphabet_set = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	
   printf("Hello, World!");
   return 0;
}