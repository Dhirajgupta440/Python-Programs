#include<iostream>
using namespace std;
int isPrime(int n){
    if(n==0 || n==1){
        return 0;
    }
    for(int  i=2; i<=n/2; i++){
        if(n%i==0){
            return 0;
        }
    }
    return -1;

}
int main(){
    int n,result;
    cout<<"Enter any number : ";
    cin>>n;
    result=isPrime(n);
    if(result = 0){
        cout<<"Not Prime";
    }
    else{
        cout<<"Prime number";
    }
}