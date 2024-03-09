#include <iostream>
#include <cmath>

using namespace std;

int calc(int x){
    return log(x)*10;
}

int main() {
    char matrix [500][500];


    for(int i =0; i<500; i++){
        for(int j=0; j<500; j++){
            if (j == calc(i)){
                matrix[i][j] = 1;
            }
            else matrix[i][j] = 0;            
        }
    }

    for(int j=499; j>=0; j--){
        for(int i=0; i<500; i++){
            if (matrix[i][j] == 1) cout << "#";
            else cout << " ";
        }
        cout << "\n";
    }
    
    getchar();

}
