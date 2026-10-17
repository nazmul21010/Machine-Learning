#include<bits/stdc++.h>
using namespace std;

int main(){

cout<<"Enter the income : ";

double income,tax=0.0;
cin>>income;

if(income==0 && income<=250000)
{
    tax=0;
}
else if(income<=500000)
{
    tax=income*0.1;
}
else if(income<=100000){
     tax=income*0.2;
}
else if(income>100000){
     tax=income*0.3;
}

cout<<tax;
    return 0;
}